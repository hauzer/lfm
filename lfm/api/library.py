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
    request_auto(_pkg)


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
    request_auto(_pkg)


def remove_artist(artist):
    request_auto(_pkg)


def remove_scrobble(artist, track, timestamp):
    request_auto(_pkg)


def remove_track(artist, track):
    request_auto(_pkg)
