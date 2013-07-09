#
# A Last.fm API interface.
# Copyright (C) 2013  Ð�Ð¸ÐºÐ¾Ð»Ð° Ð’ÑƒÐºÐ¾Ñ�Ð°Ð²Ñ™ÐµÐ²Ð¸Ñ›
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


class Album(Package):
    def add_tags(self, artist, album, tags):
        self.app.request_auto()
    
    
    def get_buy_links(self, country, artist = None, album = None, mbid = None, autocorrect = None):
        data = self.app.request_auto()
        return data["affiliations"]
    
    
    def get_info(self, artist = None, album = None, username = None, autocorrect = None, lang = None, mbid = None):
        data = self.app.request_auto()
        return data["album"]
    
    
    def get_shouts(self, artist = None, album = None, page = None, autocorrect = None, mbid = None):
        data = self.app.request_auto()
        return data["shouts"]
    
    
    def get_tags(self, artist = None, album = None, user = None, autocorrect = None, mbid = None):
        data = self.app.request_auto()
        return data["tags"]
    
    
    def get_top_tags(self, artist = None, album = None, autocorrect = None, mbid = None):
        data = self.app.request_auto()
        return data["toptags"]
    
    
    def remove_tag(self, tag, artist, album):
        self.app.request_auto()
    
    
    def search(self, album, page = None, limit = None):
        data = self.app.request_auto()
        return data["results"]
