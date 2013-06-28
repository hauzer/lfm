import inspect, requests, hashlib, json


class App:
    key     = ""
    secret  = ""
    sk      = ""

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret


app = App("", "")
api_root = "https://ws.audioscrobbler.com/2.0/"


def sign(params):
    forbid_keys = [None, "format"]

    concat_params = "".join([key + params[key] for key in sorted(list(params)) if key not in forbid_keys]) \
                  + app.secret

    sig = hashlib.md5(concat_params.encode('utf-8')).hexdigest()
    
    return sig


def request(pkg, method, params):
    conv = {bool: lambda x: "1" if x else "0"}
    
    params = dict([(key, conv[type(params[key])](params[key])) if type(params[key]) in conv \
                   else (key, str(params[key])) for key in params])

    params.update({"api_key": app.key,
                   "method": pkg + "." + method,
                   "sk": app.sk,
                   "format": "json"})

    params["api_sig"] = sign(params)

    resp = requests.post(api_root, params)
    data = json.loads(resp.text)

    print(data)

    return data


def request_auto(pkg, special_params = None, method = None):
    frame_record = inspect.stack()[1]

    if(method is None):
        method = frame_record[3].replace("_", "")

    args, _, _, locals = inspect.getargvalues(frame_record[0])

    params = dict([(arg, locals[arg]) for arg in args])

    if(special_params is not None):
        params.update(special_params)

    params = dict([(key.rstrip('_'), params[key]) for key in params])

    return request(pkg, method, params)
