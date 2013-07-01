from lfm.lfm import request_auto


_pkg = "chart"


def get_hyped_artists(page = None, limit = None):
    data = request_auto(_pkg)
    return data["artists"]


def get_hyped_tracks(page = None, limit = None):
    data = request_auto(_pkg)
    return data["tracks"]


def get_loved_tracks(page = None, limit = None):
    data = request_auto(_pkg)
    return data["tracks"]


def get_top_artists(page = None, limit = None):
    data = request_auto(_pkg)
    return data["artists"]


def get_top_tags(page = None, limit = None):
    data = request_auto(_pkg)
    return data["tags"]


def get_top_tracks(page = None, limit = None):
    data = request_auto(_pkg)
    return data["tracks"]
