from lfm.lfm import request_auto


_pkg = "event"


def attend(event, status):
    data = request_auto(_pkg)


def get_attendees(event, page = None, limit = None):
    data = request_auto(_pkg)
    return data["attendees"]


def get_info(event):
    data = request_auto(_pkg)
    return data["event"]


def get_shouts(event, page = None, limit = None):
    data = request_auto(_pkg)
    return data["shouts"]


def share(event, recipient, message = None, public = None):
    data = request_auto(_pkg)


def shout(event, message):
    data = request_auto(_pkg)
