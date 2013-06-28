from lfm import lfm

class Token:
    token = ""

    def __init__(self, token):
        self.token = token

    def get_url(self):
        return "http://www.last.fm/api/auth/?api_key=" + lfm.app.key + "&token=" + self.token


pkg = "auth"

def get_mobile_session(username, password):
    data = lfm.request_auto(pkg)
    return data["session"]


def get_session(token):
    data = lfm.request_auto(pkg)
    return data["session"]


def get_token():
    data = lfm.request_auto(pkg)

    token = Token(data["token"])
    return token
