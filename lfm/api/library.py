from lfm.lfm import request_auto, to_array, to_arrays


_pkg = "library"


def add_album(albums):
    params = to_arrays(albums, ["artist", "album"])
    albums = None

    data = request_auto(_pkg, params)
    return data["albums"]


def add_artist(artists):
    params = to_array(artists, "artist")
    artists = None

    data = request_auto(_pkg, params)
    return data["artists"]


def add_track(artist, track):
    data = request_auto(_pkg)


def get_albums(user, artist, limit = None, page = None):
    data = request_auto(_pkg)
    return data["albums"]


def get_artists(user, limit = None, page = None):
    data = request_auto(_pkg)
    return data["artists"]


def get_tracks(user, artist, album, limit = None, page = None):
    data = request_auto(_pkg)
    return data["tracks"]


def remove_album(artist, album):
    data = request_auto(_pkg)


def remove_artist(artist):
    data = request_auto(_pkg)


def remove_scrobble(artist, track, timestamp):
    data = request_auto(_pkg)


def remove_track(artist, track):
    data = request_auto(_pkg)
