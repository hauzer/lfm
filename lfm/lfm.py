import inspect, requests, hashlib, json


class App:
    key     = None
    secret  = None
    sk      = None

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret


# The currently active application
app = App("", "")
api_root = "https://ws.audioscrobbler.com/2.0/"


def sign(params):
    """
    Generates an API signature, which is needed for authorized API requests.

    params: A dictionary of all parameters intended to be sent with an API request.

    returns: An API signature.

    """

    # Parameters are alphabetically sorted by their key, and then concatenated
    # in a keyvalue manner. The application's secret is appended afterwards,
    # the whole thing is UTF-8 encoded, and then md5() hashed, hex digest of it
    # being the signature. The parameter "format" isn't included in the calculation.

    # Keys excluded from the calculation
    forbid_keys = ["format"]

    concat_params = ""
    for key in sorted(list(params)):
        if key not in forbid_keys:
            concat_params += key + params[key]

    concat_params += app.secret

    sig = hashlib.md5(concat_params.encode('utf-8')).hexdigest()
    
    return sig


def request(pkg, method, params):
    """
    Makes an API request.

    pkg   : The name of the package in which the method resides.
    method: The method's name.
    params: A dictionary of parameters to be sent.

    returns: A JSON response.

    """

    params.update({"api_key": app.key,
                   "method": pkg + "." + method,
                   "sk": app.sk,
                   "format": "json"})

    # Remove keys with a value of None.
    params = dict((key, params[key]) for key in params if params[key] is not None)

    # A dictionary of to-string converters, as required by the API.
    conv = { bool: lambda x: "1" if x else "0" }
    
    for key in params:
        valtype = type(params[key])

        if valtype in conv:
            params[key] = conv[valtype](params[key])

        else:
            params[key] = str(params[key])

    params["api_sig"] = sign(params)

    print(str(params) + "\n")

    resp = requests.post(api_root, params)
    data = json.loads(resp.text)

    print(str(data) + "\n\n")

    return data


def request_auto(pkg, special_params = None, method = None):
    """
    An automated version of request(), designed to reduce repetitive code.

    This function will generate the API method and API request parameters from its
    calling function's signature. The caller's name, stripped of underscores,
    is used as the API method. The caller's argument names are parameter keys,
    and argument values are parameter values. Argument names are stripped of
    trailing underscores, to permit use of keywords.
    special_params can be used to override any parameter, and add any number of
    additional ones.

    pkg                  : The name of the package in which the method resides.
    special_params = None: Additional or modified parameters to be used.
    method         = None: The method's name.

    returns: A JSON response.

    """

    frame_record = inspect.stack()[1]

    if(method is None):
        method = frame_record[3].replace("_", "")

    args, _, _, locals = inspect.getargvalues(frame_record[0])

    params = dict([(arg, locals[arg]) for arg in args])

    if(special_params is not None):
        params.update(special_params)

    params = dict([(key.rstrip('_'), params[key]) for key in params])

    return request(pkg, method, params)
