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


_pkg = "geo"


def get_events(tag = None, page = None, limit = None, long = None, lat = None, location = None, distance = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_metro_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_hype_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_hype_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_unique_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_unique_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_weekly_chart_list(metro):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_metros(country = None):
    data = request_auto(_pkg)
    return data["metros"]


def get_top_artists(country, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_top_tracks(country, page = None, limit = None, location = None):
    data = request_auto(_pkg)
    return data["toptracks"]
