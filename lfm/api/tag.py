from lfm.lfm import request_auto


_pkg = "tag"


def get_info(artist = None, mbid = None, lang = None):
    data = request_auto(_pkg)
    return data["tag"]


def get_similar(tag):
    data = request_auto(_pkg)
    return data["similartags"]


def get_top_albums(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topalbums"]


def get_top_artists(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_top_tags():
    data = request_auto(_pkg)
    return data["toptags"]


def get_top_tracks(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_weekly_artist_chart(tag, from_ = None, to = None, limit = None):
    data = request_auto(_pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(tag):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_search(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["results"]
