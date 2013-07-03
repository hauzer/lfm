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


_pkg = "auth"


def get_mobile_session(username, password):
    data = request_auto(_pkg)
    return data["session"]


def get_session(token):
    data = request_auto(_pkg)
    return data["session"]


def get_token():
    data = request_auto(_pkg)
    return data["token"]
