from lfm.lfm import request_auto


_pkg = "playlist"


def add_track(playlistid, artist, track):
    request_auto(_pkg)


def create(title = None, description = None):
    request_auto(_pkg)
    