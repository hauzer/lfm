from lfm import lfm


pkg = "event"


def attend(event, status):
    data = lfm.request_auto(pkg)


def get_attendees(event, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["attendees"]


def get_info(event):
    data = lfm.request_auto(pkg)
    return data["event"]


def get_shouts(event, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["shouts"]


def share(event, recipient, message = None, public = None):
    data = lfm.request_auto(pkg)


def shout(event, message):
    data = lfm.request_auto(pkg)
