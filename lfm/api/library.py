from lfm import lfm


_pkg = "library"


def add_album(albums):
    params = {}

    for i, (artist, album) in enumerate(albums):
        params["artist[" + str(i) + "]"]    = artist
        params["album[" + str(i) + "]"]     = album

    params["albums"] = None

    data = lfm.request_auto(_pkg, params)
    return data["albums"]


def add_artist(artists):
    for i, artist in enumerate(artists):
        params["artist[" + str(i) + "]"]    = artist

    params["artists"] = None

    data = lfm.request_auto(_pkg, params)
    return data["artists"]


def add_track(artist, track):
    data = lfm.request_auto(_pkg)


def get_albums(user, artist, limit = None, page = None):
    data = lfm.request_auto(_pkg)
    return data["albums"]


def get_artists(user, limit = None, page = None):
    data = lfm.request_auto(_pkg)
    return data["artists"]


def get_tracks(user, artist, album, limit = None, page = None):
    data = lfm.request_auto(_pkg)
    return data["tracks"]


def remove_album(artist, album):
    data = lfm.request_auto(_pkg)


def remove_artist(artist):
    data = lfm.request_auto(_pkg)


def remove_scrobble(artist, track, timestamp):
    data = lfm.request_auto(_pkg)


def remove_track(artist, track):
    data = lfm.request_auto(_pkg)
