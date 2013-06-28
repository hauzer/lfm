from lfm import lfm

pkg = "artist"


def add_tags(artist, tags):
    params = {"tags": ",".join(tags)}
    data = lfm.request_auto(pkg, params)


def get_corrections(artist):
    data = lfm.request_auto(pkg)
    return data["corrections"]


def get_events(artist = None, mbid = None, autocorrect = None, page = None, limit = None, festivalsonly = None):
    data = lfm.request_auto(pkg)
    return data["events"]


def get_info(artist = None, mbid = None, lang = None, autocorrect = None, username = None):
    data = lfm.request_auto(pkg)
    return data["artist"]


def get_past_events(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["events"]


def get_podcast(artist = None, mbid = None, autocorrect = None):
    data = lfm.request_auto(pkg)
    return data["rss"]


def get_shouts(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["shouts"]


def get_similar(artist = None, mbid = None, autocorrect = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["similarartists"]


def get_tags(artist = None, mbid = None, autocorrect = None, user = None):
    data = lfm.request_auto(pkg)
    return data["tags"]


def get_top_albums(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["topalbums"]


def get_top_fans(artist = None, mbid = None, autocorrect = None):
    data = lfm.request_auto(pkg)
    return data["topfans"]


def get_top_tags(artist = None, mbid = None, autocorrect = None):
    data = lfm.request_auto(pkg)
    return data["toptags"]


def get_top_tracks(artist = None, mbid = None, autocorrect = None, page = None, limit = None):
    data = lfm.request_auto(pkg)
    return data["toptracks"]


def remove_tag(artist, tag):
    data = lfm.request_auto(pkg)


def search(artist, page, limit):
    data = lfm.request_auto(pkg)
    return data["results"]


def share(artist, recipient, message = None, public = None):
    data = lfm.request_auto(pkg)


def shout(artist, message):
    data = lfm.request_auto(pkg)
