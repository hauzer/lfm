import inspect, requests, hashlib, json
from . import exceptions


class App:
    key     = None
    secret  = None
    sk      = None

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def activate(self):
        global app
        app = self

# The currently active application
app = App("", "")
api_root = "https://ws.audioscrobbler.com/2.0/"


def request(pkg, method, params):
    """
    Makes an API request.

    pkg   : The name of the package in which the method resides.
    method: The method's name.
    params: A dictionary of parameters to be sent.

    returns: A JSON response.

    """

    print(app.key)
    print(app.secret)

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
