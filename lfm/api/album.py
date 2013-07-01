from lfm.lfm import request_auto

_pkg = "album"


def add_tags(artist, album, tags):
    data = request_auto(_pkg)


def get_buy_links(country, artist = None, album = None, mbid = None, autocorrect = None):
    data = request_auto(_pkg)
    return data["affiliations"]


def get_info(username = None, artist = None, album = None, mbid = None, autocorrect = None, lang = None):
    data = request_auto(_pkg)
    return data["album"]


def get_shouts(artist = None, album = None, mbid = None, autocorrect = None, page = None):
    data = request_auto(_pkg)
    return data["shouts"]


def get_tags(artist = None, album = None, mbid = None, autocorrect = None, user = None):
    data = request_auto(_pkg)
    return data["tags"]


def get_top_tags(artist = None, album = None, mbid = None, autocorrect = None):
    data = request_auto(_pkg)
    return data["toptags"]


def remove_tag(tag, artist, album):
    data = request_auto(_pkg)


def search(album, page = None, limit = None):
    data = request_auto(_pkg)
    return data["results"]
