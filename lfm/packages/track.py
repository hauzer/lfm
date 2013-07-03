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

from lfm.package import Package
from lfm.util import classes_to_arrays


class Scrobble:
    artist          = None
    track           = None
    timestamp       = None
    album           = None
    duration        = None
    mbid            = None
    tracknumber     = None
    albumartist     = None
    streamid        = None
    chosenbyuser    = None
    context         = None

    def __init__(self, artist, track, timestamp, album = None, duration = None, mbid = None, \
                 tracknumber = None, albumartist = None, streamid = None, chosenbyuser = None, \
                 context = None):
        self.artist         = artist
        self.track          = track
        self.timestamp      = timestamp
        self.album          = album
        self.duration       = duration
        self.mbid           = mbid
        self.tracknumber    = tracknumber
        self.albumartist    = albumartist
        self.streamid       = streamid
        self.chosenbyuser   = chosenbyuser


__pkg = "track"


class Track(Package):
    def add_tags(self, artist, track, tags):
        self.app.request_auto(__pkg)
    
    
    def ban(self, artist, track):
        self.app.request_auto(__pkg)
    
    
    def get_buy_links(self, country, artist = None, track = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["affiliations"]
    
    
    def get_corrections(self, artist, track):
        data = self.app.request_auto(__pkg)
        return data["corrections"]
    
    
    def get_fingerprint_metadata(self, fingerprintid):
        data = self.app.request_auto(__pkg)
        return data["tracks"]
    
    
    def get_info(self, artist = None, track = None, username = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["track"]
    
    
    def get_shouts(self, artist = None, track = None, page = None, limit = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["shouts"]
    
    
    def get_similar(self, artist = None, track = None, limit = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["similartracks"]
    
    
    def get_tags(self, artist = None, track = None, user = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["tags"]
    
    
    def get_top_fans(self, artist = None, track = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["topfans"]
    
    
    def get_top_tags(self, artist = None, track = None, autocorrect = None, mbid = None):
        data = self.app.request_auto(__pkg)
        return data["toptags"]
    
    
    def love(self, artist, track):
        self.app.request_auto(__pkg)
    
    
    def remove_tag(self, artist, track, tag):
        self.app.request_auto(__pkg)
    
    
    def scrobble(self, scrobbles):
        params = classes_to_arrays(scrobbles)
        scrobbles = None
    
        data = self.app.request_auto(__pkg, params)
    
        return data["scrobbles"]
    
    
    def search(self, track, artist = None, page = None, limit = None):
        data = self.app.request_auto(__pkg)
        return data["results"]
    
    
    def share(self, artist, track, recipient, message = None, public = None):
        self.app.request_auto(__pkg)
    
    
    def unban(self, artist, track):
        self.app.request_auto(__pkg)
    
    
    def unlove(self, artist, track):
        self.app.request_auto(__pkg)
    
    
    def update_now_playing(self, artist, track, album = None, duration = None, tracknumber = None, albumartist = None, \
                           mbid = None, context = None):
        data = self.app.request_auto(__pkg)
        return data["nowplaying"]
