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


_pkg = "tag"


def get_info(artist = None, mbid = None, lang = None):
    data = request_auto(_pkg)
    return data["tag"]


def get_similar(tag):
    data = request_auto(_pkg)
    return data["similartags"]


def get_top_albums(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topalbums"]


def get_top_artists(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_top_tags():
    data = request_auto(_pkg)
    return data["toptags"]


def get_top_tracks(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_weekly_artist_chart(tag, limit = None, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(tag):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_search(tag, page = None, limit = None):
    data = request_auto(_pkg)
    return data["results"]
