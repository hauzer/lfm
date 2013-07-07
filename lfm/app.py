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
from lfm import lfm
from lfm.package import Package
from lfm import exceptions as e
from lfm import packages as pkg

class App:
    album       = None
    artist      = None
    auth        = None
    chart       = None
    event       = None
    geo         = None
    group       = None
    library     = None
    playlist    = None
    radio       = None
    tag         = None
    tasteometer = None
    track       = None
    user        = None
    venue       = None
    
    key     = None
    secret  = None
    db      = None
    sk      = None


    def __init__(self, key, secret, db = None):
        self.album       = pkg.Album(self)
        self.artist      = pkg.Artist(self)
        self.auth        = pkg.Auth(self)
        self.chart       = pkg.Chart(self)
        self.event       = pkg.Event(self)
        self.geo         = pkg.Geo(self)
        self.group       = pkg.Group(self)
        self.library     = pkg.Library(self)
        self.playlist    = pkg.Playlist(self)
        self.radio       = pkg.Radio(self)
        self.tag         = pkg.Tag(self)
        self.tasteometer = pkg.Tasteometer(self)
        self.track       = pkg.Track(self)
        self.user        = pkg.User(self)
        self.venue       = pkg.Venue(self)
        
        self.key = key
        self.secret = secret
        self.db = db


    def can_request(self):
        can = True
        
        try:
            dbconn = sqlite3.connect(self.db)
            
        except TypeError:
            return can
        
        dbcur = dbconn.cursor()
        time_now = int(time.time())
        
        try:
            dbcur.execute("create table timestamps (timestamps integer)")
            
        except sqlite3.OperationalError:
            dbcur.execute("delete from timestamps where timestamps < ?", (time_now - lfm.requests_period,))
            dbcur.execute("select count(timestamps) from timestamps")

            if dbcur.fetchone()[0] >= lfm.max_requests:
                can = False
        
        dbconn.commit()
        dbcur.close()
        dbconn.close()
        
        return can
        

    def log_request(self):
        try:
            dbconn = sqlite3.connect(self.db)
            
        except TypeError:
            raise
        
        dbcur = dbconn.cursor()
        
        try:
            dbcur.execute("create table timestamps (timestamps integer)")
            
        except sqlite3.OperationalError:
            pass
            
        dbcur.execute("insert into timestamps (timestamps) values (?)", (int(time.time()),))
        
        dbconn.commit()
        dbcur.close()
        dbconn.close()


    def sign_request(self, params):
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
    
        concat_params += self.secret
    
        sig = hashlib.md5(concat_params.encode('utf-8')).hexdigest()
        
        return sig


    def request(self, pkg, method, params):
        """
        Makes an API request.
    
        pkg   : The name of the package in which the method resides.
        method: The method's name.
        params: A dictionary of parameters to be sent.
    
        returns: A JSON response.
    
        """
    
        if self.can_request():
            self.log_request()
        else:
            raise e.RateLimitExceeded("Exceeded the limit of one request per five seconds over five minutes.")
    
    
        params.update({"api_key": self.key,
                       "method": pkg + "." + method,
                       "sk": self.sk,
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
                
        params["api_sig"] = self.sign_request(params)
                
        resp = requests.post(lfm.api_root, params)
        data = json.loads(resp.text)
        
        try:
            raise e.codes[data["error"]](data["message"])
        except KeyError:
            pass
    
        return data


    def request_auto(self, special_params = None, pkg = None, method = None):
        """
        An automated version of request(), designed to reduce repetitive code.
    
        This function will generate the API package, method and request parameters from its
        calling function's signature. If the caller is in a class, [self] is automatically removed.
        If the caller is in a class whose parent or ancestor is [lfm.package.Package], then the
        class' name is used as the API package. The caller's name, stripped of underscores,
        is used as the API method. The caller's argument names are parameter keys, and argument
        values are parameter values. Argument names are stripped of trailing underscores,
        to permit use of keywords, such as [from]. [special_params] can be used to override any
        parameter, and add or change any number of additional ones.
    
        pkg            = None: The name of the package in which the method resides.
        special_params = None: Additional or modified parameters to be used.
        method         = None: The method's name.
    
        returns: A JSON response.
    
        """
    
        frame_record = inspect.stack()[1]
    
        if(method is None):
            method = frame_record[3].replace("_", "")
    
        args, _, _, locals_ = inspect.getargvalues(frame_record[0])
        params = dict([(arg, locals_[arg]) for arg in args])
        
        for key, value in params.items():
            if key == "self":
                params[key] = None
                
                if isinstance(value, Package):
                    pkg = value.__class__.__name__
    
        if(special_params is not None):
            params.update(special_params)
    
        params = dict([(key.rstrip('_'), params[key]) for key in params])
    
        return self.request(pkg, method, params)
    