from lfm import lfm


_pkg = "radio"


def get_playlist(bitrate = None, rtp = None, discovery = None, speed_multiplier = None, buylinks = None):
    data = lfm.request_auto(_pkg)
    return data["playlist"]


def search(name):
    data = lfm.request_auto(_pkg)
    return data["stations"]


def tune(station, lang = None):
    data = lfm.request_auto(_pkg)
    return data["station"]
