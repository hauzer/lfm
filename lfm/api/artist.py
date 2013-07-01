from lfm.lfm import request_auto


_pkg = "artist"


def add_tags(artist, tags):
    data = request_auto(_pkg)


def get_corrections(artist):
    data = request_auto(_pkg)
    return data["corrections"]


def get_events(artist = None, mbid = None, autocorrect = None, page = None, limit = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_info(artist = None, mbid = None, lang = None, autocorrect = None, username = None):
    data = request_auto(_pkg)
    return data["artist"]


def get_past_events(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["events"]


def get_podcast(artist = None, mbid = None, autocorrect = None):
    data = request_auto(_pkg)
    return data["rss"]


def get_shouts(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["shouts"]


def get_similar(artist = None, mbid = None, autocorrect = None, limit = None):
    data = request_auto(_pkg)
    return data["similarartists"]


def get_tags(artist = None, mbid = None, autocorrect = None, user = None):
    data = request_auto(_pkg)
    return data["tags"]


def get_top_albums(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topalbums"]


def get_top_fans(artist = None, mbid = None, autocorrect = None):
    data = request_auto(_pkg)
    return data["topfans"]


def get_top_tags(artist = None, mbid = None, autocorrect = None):
    data = request_auto(_pkg)
    return data["toptags"]


def get_top_tracks(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def remove_tag(artist, tag):
    data = request_auto(_pkg)


def search(artist, page, limit):
    data = request_auto(_pkg)
    return data["results"]


def share(artist, recipient, message = None, public = None):
    data = request_auto(_pkg)


def shout(artist, message):
    data = request_auto(_pkg)
