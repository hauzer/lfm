# A Last.fm API interface.
# Copyright (C) 2013  Никола Вукосављевић
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lfm.lfm import request_auto, classes_to_arrays


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
    request_auto(_pkg)


def ban(artist, track):
    request_auto(_pkg)


def get_buy_links(country, artist = None, track = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["affiliations"]


def get_corrections(artist, track):
    data = request_auto(_pkg)
    return data["corrections"]


def get_fingerprint_metadata(fingerprintid):
    data = request_auto(_pkg)
    return data["tracks"]


def get_info(artist = None, track = None, username = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["track"]


def get_shouts(artist = None, track = None, page = None, limit = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["shouts"]


def get_similar(artist = None, track = None, limit = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["similartracks"]


def get_tags(artist = None, track = None, user = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["tags"]


def get_top_fans(artist = None, track = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["topfans"]


def get_top_tags(artist = None, track = None, autocorrect = None, mbid = None):
    data = request_auto(_pkg)
    return data["toptags"]


def love(artist, track):
    request_auto(_pkg)


def remove_tag(artist, track, tag):
    request_auto(_pkg)


def scrobble(scrobbles):
    params = classes_to_arrays(scrobbles)
    scrobbles = None

    data = request_auto(_pkg, params)

    return data["scrobbles"]


def search(track, artist = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["results"]


def share(artist, track, recipient, message = None, public = None):
    request_auto(_pkg)


def unban(artist, track):
    request_auto(_pkg)


def unlove(artist, track):
    request_auto(_pkg)


def update_now_playing(artist, track, album = None, duration = None, tracknumber = None, albumartist = None, \
                       mbid = None, context = None):
    data = request_auto(_pkg)
    return data["nowplaying"]
