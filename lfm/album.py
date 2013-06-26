from . import lfm;

pkg = "album"

def add_tags(artist, album, tags):
    lfm.request(pkg)

def get_buy_links(country, artist = None, album = None, mbid = None, autocorrect = None):
    data = lfm.request(pkg)
    return data["affiliations"]

def get_info(username = None, artist = None, album = None, mbid = None, autocorrect = None, lang = None):
    data = lfm.request(pkg)
    return data["album"]

def get_shouts(artist = None, album = None, mbid = None, autocorrect = None, page = None):
    data = lfm.request(pkg)
    return data["shouts"]

def get_tags(artist = None, album = None, mbid = None, autocorrect = None, user = None):
    data = lfm.request(pkg)
    return data["tags"]

def get_top_tags(artist = None, album = None, mbid = None, autocorrect = None):
    data = lfm.request(pkg)
    return data["toptags"]

def remove_tag(tag, artist, album):
    data = lfm.request(pkg)

def search(album, page = None, limit = None):
    data = lfm.request(pkg)
    return data["results"]
