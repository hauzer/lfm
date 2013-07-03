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

from lfm.lfm import request_auto


_pkg = "user"


def get_artist_tracks(user, artist, page = None, starttimestamp = None, endtimestamp = None):
    data = request_auto(_pkg)
    return data["artisttracks"]


def get_banned_tracks(user, page = None, limit = None):
    data = request_auto(_pkg)
    return data["bannedtracks"]


def get_events(user, page = None, limit = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_friends(user, page = None, limit = None, recenttracks = None):
    data = request_auto(_pkg)
    return data["friends"]


def get_info(user = None):
    data = request_auto(_pkg)
    return data["user"]


def get_loved_tracks(user, page = None, limit = None):
    data = request_auto(_pkg)
    return data["lovedtracks"]


def get_neighbours(user, limit = None):
    data = request_auto(_pkg)
    return data["neighbours"]


def get_new_releases(user, userecs = None):
    data = request_auto(_pkg)
    return data["albums"]


def get_past_events(user, page = None, limit = None):
    data = request_auto(_pkg)
    return data["events"]


def get_personal_tags(user, tag, taggingtype, page = None, limit = None):
    data = request_auto(_pkg)
    return data["taggings"]


def get_playlists(user):
    data = request_auto(_pkg)
    return data["playlists"]


def get_recent_stations(user, page = None, limit = None):
    data = request_auto(_pkg)
    return data["recentstations"]


def get_recent_tracks(user, extended = None, page = None, limit = None, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["recenttracks"]


def get_recommended_artists(page = None, limit = None):
    data = request_auto(_pkg)
    return data["recommendations"]


def get_recommended_events(page = None, limit = None, latitude = None, longitude = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_shouts(user, page = None, limit = None):
    data = request_auto(_pkg)
    return data["shouts"]


def get_top_albums(user, period = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topalbums"]


def get_top_artists(user, period = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_top_tags(user, limit = None):
    data = request_auto(_pkg)
    return data["toptags"]


def get_top_tracks(user, period = None, page = None, limit = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_weekly_album_chart(user, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklyalbumchart"]


def get_weekly_artist_chart(user, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(user):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_weekly_track_chart(user, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklytrackchart"]


def shout(user, message):
    request_auto(_pkg)
