# coding=utf-8

#
# A Last.fm API interface.
# Copyright (C) 2013  Никола "hauzer" Вукосављевић
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
#


from lfm.package import Package


class Venue(Package):
    def get_events(self, venue, festivalsonly = None):
        data = self.app.request_auto()
        return data["events"]
    
    
    def get_past_events(self, venue, page = None, limit = None, festivalsonly = None):
        data = self.app.request_auto()
        return data["events"]
    
    
    def search(self, venue, page = None, limit = None, country = None):
        data = self.app.request_auto()
        return data["results"]
