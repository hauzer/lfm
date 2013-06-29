from lfm import lfm
# Used in scrobble()
import inspect


class Scrobble:
    artist          = None
    track           = None
    timestamp       = None
    album           = None
    duration        = None
    mbid            = None
    tracknumber     = None
    albumartist     = None
    streamid        = None
    chosenbyuser    = None
    context         = None

    def __init__(self, artist, track, timestamp, album = None, duration = None, mbid = None, \
                 tracknumber = None, albumartist = None, streamid = None, chosenbyuser = None, \
                 context = None):
        self.artist         = artist
        self.track          = track
        self.timestamp      = timestamp
        self.album          = album
        self.duration       = duration
        self.mbid           = mbid
        self.tracknumber    = tracknumber
        self.albumartist    = albumartist
        self.streamid       = streamid
        self.chosenbyuser   = chosenbyuser


_pkg = "track"


def add_tags(artist, track, tags):
    params = {"tags": ",".join(tags)}
    data = lfm.request_auto(_pkg, params)


def ban(artist, track):
    data = lfm.request_auto(_pkg)


def get_buy_links(country, artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["affiliations"]


def get_corrections(artist, track):
    data = lfm.request_auto(_pkg)
    return data["corrections"]


def get_fingerprint_metadata(fingerprintid):
    data = lfm.request_auto(_pkg)
    return data["tracks"]


def get_info(artist = None, track = None, username = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["track"]


def get_shouts(artist = None, track = None, page = None, limit = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["shouts"]


def get_similar(artist = None, track = None, limit = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["similartracks"]


def get_tags(artist = None, track = None, user = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["tags"]


def get_top_fans(artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["topfans"]


def get_top_tags(artist = None, track = None, autocorrect = None, mbid = None):
    data = lfm.request_auto(_pkg)
    return data["toptags"]


def love(artist, track):
    data = lfm.request_auto(_pkg)


def remove_tag(artist, track, tag):
    data = lfm.request_auto(_pkg, params)


def scrobble(scrobbles):
    params = {}
    for i, scrobble in enumerate(scrobbles):
        attrs = [attr for attr in inspect.getmembers(scrobble) if not(attr[0].startswith("__") and attr[0].endswith("__"))]

        for key, value in attrs:
            params[key + "[" + str(i) + "]"] = value

    
    params["scrobbles"] = None

    data = lfm.request_auto(_pkg, params)

    return data["scrobbles"]


def search(track, artist = None, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["results"]


def share(artist, track, recipient, message = None, public = None):
    params["recipient"] = ",".join(recipient)

    data = lfm.request_auto(_pkg, params)


def unban(artist, track):
    data = lfm.request_auto(_pkg)


def unlove(artist, track):
    data = lfm.request_auto(_pkg)


def update_now_playing(artist, track, album = None, duration = None, tracknumber = None, albumartist = None, \
                       mbid = None, context = None):
    data = lfm.request_auto(_pkg)
    return data["nowplaying"]
