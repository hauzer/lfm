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


_pkg = "venue"


def get_events(venue, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_past_events(venue, page = None, limit = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def search(venue, page = None, limit = None, country = None):
    data = request_auto(_pkg)
    return data["results"]
