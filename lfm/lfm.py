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


import lfm.api as api
import lfm.packages as packages


class App(api.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.album       = packages.Album(self)
        # self.artist      = ArtistPackage(self)
        self.auth        = packages.Auth(self)
        # self.chart       = ChartPackage(self)
        # self.event       = EventPackage(self)
        # self.geo         = GeoPackage(self)
        # self.group       = GroupPackage(self)
        # self.library     = LibraryPackage(self)
        # self.playlist    = PlaylistPackage(self)
        # self.radio       = RadioPackage(self)
        # self.tag         = TagPackage(self)
        # self.tasteometer = TasteometerPackage(self)
        # self.track       = TrackPackage(self)
        # self.user        = UserPackage(self)
        # self.venue       = VenuePackage(self)
