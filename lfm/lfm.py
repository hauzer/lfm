# A Last.fm API interface.
# Copyright (C) 2013  Никола Вукосављевић
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import hashlib
import json
import inspect
import sqlite3
import time
from . import exceptions

class App:
    key     = None
    secret  = None
    sk      = None
    db      = None

    def __init__(self, key, secret, db):
        global app
        
        self.key = key
        self.secret = secret
        self.db = db
        
        if app is None:
            self.activate()

    def activate(self):
        global app
        app = self


# The currently active application
app = None
api_root = "https://ws.audioscrobbler.com/2.0/"

request_interval        = 300
request_avg_interval    = 5
max_requests            = request_interval / request_avg_interval


def request(pkg, method, params):
    """
    Makes an API request.

    pkg   : The name of the package in which the method resides.
    method: The method's name.
    params: A dictionary of parameters to be sent.

    returns: A JSON response.

    """

    try:
        dbconn = sqlite3.connect(app.db)

    except TypeError:
        pass
    
    else:
        dbcur = dbconn.cursor()
        time_now = int(time.time())
        can_request = True
        
        try:
            dbcur.execute("create table timestamps (timestamps integer)")
            
        except sqlite3.OperationalError:
            dbcur.execute("delete from timestamps where timestamps < ?", (time_now - request_interval,))
            dbcur.execute("select count(timestamps) from timestamps")

            if dbcur.fetchone()[0] >= max_requests:
                can_request = False
        
        if can_request:
            dbcur.execute("insert into timestamps (timestamps) values (?)", (time_now,))
        
        dbconn.commit()
        dbcur.close()
        dbconn.close()
        
        if not can_request:
            raise exceptions.RateLimitExceeded("Exceeded the limit of one request per five seconds over five minutes.")
        

    params.update({"api_key": app.key,
                   "method": pkg + "." + method,
                   "sk": app.sk,
                   "format": "json"})

    # Remove keys with a value of None.
    params = dict((key, params[key]) for key in params if params[key] is not None)
    
    # Convert all objects to strings, as expected by the API
    for key in params.copy():
        if isinstance(params[key], bool):
            if params[key]:
                params[key] = "1"
            else:
                params[key] = "0"

        elif not isinstance(params[key], str):
            try:
                params[key] = ",".join(params[key])

            except TypeError:
                params[key] = str(params[key])
            
    params["api_sig"] = sign(params)
            
    resp = requests.post(api_root, params)
    data = json.loads(resp.text)
    
    try:
        raise exceptions.codes[data["error"]](data["message"])
    except KeyError:
        pass

    return data


def request_auto(pkg, special_params = None, method = None):
    """
    An automated version of request(), designed to reduce repetitive code.

    This function will generate the API method and API request parameters from its
    calling function's signature. The caller's name, stripped of underscores,
    is used as the API method. The caller's argument names are parameter keys,
    and argument values are parameter values. Argument names are stripped of
    trailing underscores, to permit use of keywords.
    special_params can be used to override any parameter, and add or change any
    number of additional ones.

    pkg                  : The name of the package in which the method resides.
    special_params = None: Additional or modified parameters to be used.
    method         = None: The method's name.

    returns: A JSON response.

    """

    frame_record = inspect.stack()[1]

    if(method is None):
        method = frame_record[3].replace("_", "")

    args, _, _, locals_ = inspect.getargvalues(frame_record[0])

    params = dict([(arg, locals_[arg]) for arg in args])

    if(special_params is not None):
        params.update(special_params)

    params = dict([(key.rstrip('_'), params[key]) for key in params])

    return request(pkg, method, params)


def sign(params):
    """
    Generates an API signature, which is needed for authorized API requests.

    params: A dictionary of all parameters intended to be sent with an API request.

    returns: An API signature.

    """

    # Parameters are alphabetically sorted by their key, and then concatenated
    # in a keyvalue manner. The application's secret is appended afterwards,
    # the whole thing is UTF-8 encoded, and then md5() hashed, hex digest of it
    # being the signature. Some parameters mustn't be included in the calculation.

    # Keys excluded from the calculation
    forbid_keys = ["format"]

    concat_params = ""
    for key in sorted(list(params)):
        if key not in forbid_keys:
            concat_params += key + params[key]

    concat_params += app.secret

    sig = hashlib.md5(concat_params.encode('utf-8')).hexdigest()
    
    return sig


def to_array(xs, key):
    array = {}

    for i, x in enumerate(xs):
        array[key + "[" + str(i) + "]"] = x

    return array


def to_arrays(xs, keys):
    arrays = {}

    for x, key in zip(list(zip(*xs)), keys):
        arrays.update(to_array(x, key))

    return arrays


def class_to_arrays(klas, i = 0):
    attrs = [(key, value) for key, value in inspect.getmembers(klas)
                    if not callable(value) and not(key.startswith("__") and key.endswith("__"))]
    
    arrays = {}
    for key, value in attrs:
        arrays[key + "[" + str(i) + "]"] = value

    return arrays

def classes_to_arrays(klasses):
    arrays = {}
    for i, klas in enumerate(klasses):
        arrays.update(class_to_arrays(klas, i))

    return arrays

def get_token_url(token):
    """
    Returns the authentication page of a token.

    """

    return "http://www.last.fm/api/auth/?api_key=" + app.key + "&token=" + token
