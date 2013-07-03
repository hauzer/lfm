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


_pkg = "event"


def attend(event, status):
    request_auto(_pkg)


def get_attendees(event, page = None, limit = None):
    data = request_auto(_pkg)
    return data["attendees"]


def get_info(event):
    data = request_auto(_pkg)
    return data["event"]


def get_shouts(event, page = None, limit = None):
    data = request_auto(_pkg)
    return data["shouts"]


def share(event, recipient, message = None, public = None):
    request_auto(_pkg)


def shout(event, message):
    request_auto(_pkg)
