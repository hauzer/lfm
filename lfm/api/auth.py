from lfm.lfm import request_auto


_pkg = "auth"


def get_mobile_session(username, password):
    data = request_auto(_pkg)
    return data["session"]


def get_session(token):
    data = request_auto(_pkg)
    return data["session"]


def get_token():
    data = request_auto(_pkg)
    return data["token"]
