from lfm import lfm


class Scrobble:
    artist          = None
    track           = None
    timestamp       = None
    album           = None
    duration        = None
    mbid            = None
    track_number    = None
    album_artist    = None
    streamid        = None
    chosen_by_user  = None
    context         = None

    def __init__(self, artist, track, timestamp):
        self.artist     = artist
        self.track      = track
        self.timestamp  = timestamp


pkg = "track"


def add_tags(artist, track, tags):
    params = {"tags": ",".join(tags)}
    data = lfm.request_auto(pkg, params)


def ban(artist, track):
    data = lfm.request_auto(pkg)


def get_buy_links(country, artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["affiliations"]


def get_corrections(artist, track):
    data = lfm.request_auto(pkg)
    return data["corrections"]


def get_fingerprint_metadata(fingerprintid):
    data = lfm.request_auto(pkg)
    return data["tracks"]


def get_info(artist = None, track = None, username = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["track"]


def get_shouts(artist = None, track = None, page = None, limit = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["shouts"]


def get_similar(artist = None, track = None, limit = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["similartracks"]


def get_tags(artist = None, track = None, user = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["tags"]


def get_top_fans(artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["topfans"]


def get_top_tags(artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(pkg)
    return data["toptags"]


def love(artist, track):
    data = lfm.request_auto(pkg)


def remove_tag(artist, track, tag):
    data = lfm.request_auto(pkg, params)


#def scrobble(scrobbles):
