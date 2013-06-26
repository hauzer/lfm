import inspect, requests, hashlib, json

class App:
    key = ""
    secret = ""
    sk = ""

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def activate(self):
        global app
        app = self


app = None
api_root = "https://ws.audioscrobbler.com/2.0/"


def request(pkg):
    frame_record = inspect.stack()[1]
    method = frame_record[3].replace("_", "")
    _, _, _, params = inspect.getargvalues(frame_record[0])

    params.update({"api_key": app.key,
                   "method": pkg + "." + method,
                   "sk": app.sk})

    concat_params = ""
    for key in sorted(list(params)):
        if(params[key] != None):
            if(type(params[key] == list)):
                value = ",".join(params[key])
            else:
                value = params[key]

            concat_params += key + value
    concat_params += app.secret

    sig = hashlib.md5(concat_params.encode('utf-8')).hexdigest()
    params["api_sig"] = sig
    params["format"] = "json"

    resp = requests.post(api_root, params)
    data = json.loads(resp.text)

    return data
