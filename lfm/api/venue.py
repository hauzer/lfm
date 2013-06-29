from lfm import lfm


_pkg = "venue"


def get_events(venue, festivalsonly = None):
    data = lfm.request_auto(_pkg)
    return data["events"]


def get_past_events(venue, page = None, limit = None, festivalsonly = None):
    data = lfm.request_auto(_pkg)
    return data["events"]


def search(venue, page = None, limit = None, country = None):
    data = lfm.request_auto(_pkg)
    return data["results"]
