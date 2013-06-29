from lfm import lfm


pkg = "radio"


def get_playlist(bitrate = None, rtp = None, discovery = None, speed_multiplier = None, buylinks = None):
    data = lfm.request_auto(pkg)
    return data["playlist"]


def search(name):
    data = lfm.request_auto(pkg)
    return data["stations"]


def tune(station, lang = None):
    data = lfm.request_auto(pkg)
    return data["station"]
