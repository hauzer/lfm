from lfm.lfm import request_auto


_pkg = "radio"


def get_playlist(bitrate = None, rtp = None, discovery = None, speed_multiplier = None, buylinks = None):
    data = request_auto(_pkg)
    return data["playlist"]


def search(name):
    data = request_auto(_pkg)
    return data["stations"]


def tune(station, lang = None):
    data = request_auto(_pkg)
    return data["station"]
