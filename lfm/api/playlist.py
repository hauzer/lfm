from lfm import lfm


_pkg = "playlist"


def add_track(playlistid, artist, track):
    data = lfm.request_auto(_pkg)


def create(title = None, description = None):
    data = lfm.request_auto(_pkg)
    