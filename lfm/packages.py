import lfm.api as api
import lfm.data as data


class Album(api.Package):
    def add_tags(self, album, tags):
        pass
    
    def get_buy_links(self, album, country, autocorrect = None):
        pass
    
    def get_info(self, album, user = None, autocorrect = None, lang = None):
        pass
    
    def get_shouts(self, album, page = None, autocorrect = None):
        pass

    def get_tags(self, album, username = None, autocorrect = None):
        pass
    
    def get_top_tags(self, album, autocorrect = None):
        pass
    
    def remove_tag(self, album, tag):
        pass
    
    def search(self, album, page = None, limit = None):
        pass
        
        
# class Artist(Package):
    # @api.method
    # def add_tags(self, artist, tags):
        # pass
        
    # @api.method
    # def get_corrections(self, artist):
        # pass
        
    # @api.method
    # def get_events(self, artist, page = None, limit = None, autocorrect = None, festivalsonly = None):
        # pass
        
    # @api.method
    # def get_info(self, artist, username = None, autocorrect = None, lang = None):
        # pass
        
    # @api.method
    # def get_past_events(self, artist, page = None, limit = None, autocorrect = None):
        # pass
        
    # @api.method
    # def get_podcast(self, artist, autocorrect = None):
        # pass
        
    # @api.method
    # def get_shouts(self, artist, page = None, limit = None, autocorrect = None):
        # pass
        
    # @api.method
    # def get_similar(self, artist, limit = None, autocorrect = None):
        # pass
        
    # @api.method
    # def get_tags(self, artist, user = None, autocorrect = None):
        # pass
        
    # @api.method
    # def get_top_albums(self, artist, page = None, limit = None, autocorrect = None):
        # pass
        
    # @api.method
    # def get_top_fans(self, artist, autocorrect = None):
        # pass
        
    # @api.method
    # def get_top_tags(self, artist, autocorrect = None):
        # pass
        
    # @api.method
    # def get_top_tracks(self, artist, page = None, limit = None, autocorrect = None):
        # pass
        
    # @api.method
    # def remove_tag(self, artist, tag):
        # pass
        
    # @api.method
    # def search(self, artist, page = None, limit = None):
        # pass
        
    # @api.method
    # def share(self, artist, recipient, message = None, public = None):
        # pass
        
    # @api.method
    # def shout(self, artist, message):
        # pass
        
        
class Auth(api.Package):
    @api.returns(data.Session)
    def get_mobile_session(self, username, password):
        pass
    
    @api.returns(data.Token)
    def get_token(self):
        pass
    
    @api.returns(data.Session)
    def get_session(self, token):
        pass
    
    @api.helper
    def get_url(self, callback):
        return "http://www.last.fm/api/auth/?api_key={}&cb={}".format(self.app.key, callback)
    

# @api.package
# class Chart(Package):        
    # @api.method
    # def get_hyped_artists(self, page = None, limit = None):
        # pass
        
    # @api.method
    # def get_hyped_tracks(self, page = None, limit = None):
        # pass
        
    # @api.method
    # def get_loved_tracks(self, page = None, limit = None):
        # pass
        
    # @api.method
    # def get_top_artists(self, page = None, limit = None):
        # pass
        
    # @api.method
    # def get_top_tags(self, page = None, limit = None):
        # pass
        
    # @api.method
    # def get_top_tracks(self, page = None, limit = None):
        # pass
    
                
# @api.package
# class Event(Package):        
    # @api.method
    # def attend(self, event, status):
        # pass
            
    # @api.method
    # def get_attendees(self, event, page = None, limit = None):
        # pass
            
    # @api.method
    # def get_info(self, event):
        # pass
            
    # @api.method
    # def get_shouts(self, event, page = None, limit = None):
        # pass
            
    # @api.method
    # def share(self, event, recipient, message = None, public = None):
        # pass
            
    # @api.method
    # def shout(self, event, message):
        # pass
        
                
# @api.package
# class Geo(Package):            
    # @api.method
    # def get_events(self, tag = None, page = None, limit = None, long = None,
                   # lat = None, location = None, distance = None, festivalsonly = None):
        # pass
                
    # @api.method
    # def get_metro_artist_chart(self, metro, country, page = None, limit = None,
                               # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_hype_artist_chart(self, metro, country, page = None, limit = None,
                                    # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_hype_track_chart(self, metro, country, page = None, limit = None,
                                   # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_track_chart(self, metro, country, page = None, limit = None,
                              # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_unique_artist_chart(self, metro, country, page = None, limit = None,
                                      # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_unique_track_chart(self, metro, country, page = None, limit = None,
                                     # start = None, end = None):
        # pass
                
    # @api.method
    # def get_metro_weekly_chart_list(self, metro):
        # pass
                
    # @api.method
    # def get_metros(self, country = None):
        # pass
                
    # @api.method
    # def get_top_artists(self, country, page = None, limit = None):
        # pass
                
    # @api.method
    # def get_top_tracks(self, country, page = None, limit = None, location = None):
        # pass
        
                
# @api.package
# class Group(Package):            
    # @api.method
    # def get_hype(self, group):
        # pass
                
    # @api.method
    # def get_members(self, group, page = None, limit = None):
        # pass
                
    # @api.method
    # def get_weekly_album_chart(self, group, from_ = None, to = None):
        # pass
                
    # @api.method
    # def get_weekly_artist_chart(self, group, from_ = None, to = None):
        # pass
                
    # @api.method
    # def get_weekly_chart_list(self, group):
        # pass
                
    # @api.method
    # def get_weekly_track_chart(self, group, from_ = None, to = None):
        # pass
        
                
# @api.package
# class Library(Package):                
    # @api.method
    # def add_album(self, album_list):
        # pass
                    
    # @api.method
    # def add_artist(self, artists):
        # pass
                    
    # @api.method
    # def add_track(self, track):
        # pass
                    
    # @api.method
    # def get_albums(self, user, artist, limit = None, page = None):
        # pass
                    
    # @api.method
    # def get_artists(self, user, limit = None, page = None):
        # pass
                    
    # @api.method
    # def get_tracks(self, user, album, limit = None, page = None):
        # pass
                    
    # @api.method
    # def remove_album(self, album):
        # pass
                    
    # @api.method
    # def remove_artist(self, artist):
        # pass
                    
    # @api.method
    # def remove_scrobble(self, track, timestamp):
        # pass
                    
    # @api.method
    # def remove_track(self, track):
        # pass
        
                
# @api.package
# class Playlist(Package):                    
    # @api.method
    # def add_track(self, playlistid, track):
        # pass
                        
    # @api.method
    # def create(self, title = None, description = None):
        # pass
        
                
# @api.package
# class Radio(Package):                        
    # @api.method
    # def get_playlist(self, bitrate = None, rtp = None, discovery = None, speed_multiplier = None, buylinks = None):
        # pass
                            
    # @api.method
    # def search(self, name):
        # pass
                            
    # @api.method
    # def tune(self, station, lang = None):
        # pass
        
                
# @api.package
# class Tag(Package):                        
    # @api.method
    # def get_info(self, tag, lang = None):
        # pass
                            
    # @api.method
    # def get_similar(self, tag):
        # pass
                            
    # @api.method
    # def get_top_albums(self, tag, page = None, limit = None):
        # pass
                            
    # @api.method
    # def get_top_artists(self, tag, page = None, limit = None):
        # pass
                            
    # @api.method
    # def get_top_tags(self):
        # pass
                            
    # @api.method
    # def get_top_tracks(self, tag, page = None, limit = None):
        # pass
                            
    # @api.method
    # def get_weekly_artist_chart(self, tag, limit = None, from_ = None, to = None):
        # pass
                            
    # @api.method
    # def get_weekly_chart_list(self, tag):
        # pass
                            
    # @api.method
    # def get_search(self, tag, page = None, limit = None):
        # pass
        
                
# @api.package
# class Tasteometer(Package):                            
    # @api.method
    # def compare(self, type1, value1, type2, value2, limit = None):
        # pass
        
                
# @api.package
# class Track(Package):                            
    # @api.method
    # def add_tags(self, track, tags):
        # pass
                                
    # @api.method
    # def ban(self, artist, track):
        # pass
                                
    # @api.method
    # def get_buy_links(self, track, country, autocorrect = None):
        # pass
                                
    # @api.method
    # def get_corrections(self, track):
        # pass
                                
    # @api.method
    # def get_fingerprint_metadata(self, fingerprintid):
        # pass
                                
    # @api.method
    # def get_info(self, track, username = None, autocorrect = None):
        # pass
                                
    # @api.method
    # def get_shouts(self, track, page = None, limit = None, autocorrect = None):
        # pass
    
    # def get_similar(self, track, limit = None, autocorrect = None):
        # pass
                                
    # @api.method
    # def get_tags(self, track, user = None, autocorrect = None):
        # pass
                                
    # @api.method
    # def get_top_fans(self, track, autocorrect = None):
        # pass
                                
    # @api.method
    # def get_top_tags(self, track, autocorrect = None):
        # pass
                                
    # @api.method
    # def love(self, track):
        # pass
                                
    # @api.method
    # def remove_tag(self, track, tag):
        # pass
                                
    # @api.method
    # def scrobble(self, scrobbles):
        # pass
                                
    # @api.method
    # def search(self, track, artist = None, page = None, limit = None):
        # pass
                                
    # @api.method
    # def share(self, artist, track, recipient, message = None, public = None):
        # pass
                                
    # @api.method
    # def unban(self, artist, track):
        # pass
                                
    # @api.method
    # def unlove(self, artist, track):
        # pass
                                
    # @api.method
    # def update_now_playing(self, artist, track, album = None, duration = None, \
                           # mbid = None, tracknumber = None, albumartist = None, \
                           # context = None):
        # pass
        
                
# @api.package
# class User(Package):                            
    # @api.method
    # def get_artist_tracks(self, user, artist, page = None, starttimestamp = None, endtimestamp = None):
        # pass
                                
    # @api.method
    # def get_banned_tracks(self, user, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_events(self, user, page = None, limit = None, festivalsonly = None):
        # pass
                                
    # @api.method
    # def get_friends(self, user, page = None, limit = None, recenttracks = None):
        # pass
                                
    # @api.method
    # def get_info(self, user = None):
        # pass
                                
    # @api.method
    # def get_loved_tracks(self, user, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_neighbours(self, user, limit = None):
        # pass
                                
    # @api.method
    # def get_new_releases(self, user, userecs = None):
        # pass
                                
    # @api.method
    # def get_past_events(self, user, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_personal_tags(self, user, tag, taggingtype, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_playlists(self, user):
        # pass
                                
    # @api.method
    # def get_recent_stations(self, user, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_recent_tracks(self, user, extended = None, page = None, limit = None, from_ = None, to = None):
        # pass
                                
    # @api.method
    # def get_recommended_artists(self, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_recommended_events(self, page = None, limit = None, latitude = None, longitude = None, festivalsonly = None):
        # pass
                                
    # @api.method
    # def get_shouts(self, user, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_top_albums(self, user, period = None, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_top_artists(self, user, period = None, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_top_tags(self, user, limit = None):
        # pass
                                
    # @api.method
    # def get_top_tracks(self, user, period = None, page = None, limit = None):
        # pass
                                
    # @api.method
    # def get_weekly_album_chart(self, user, from_ = None, to = None):
        # pass
                                
    # @api.method
    # def get_weekly_artist_chart(self, user, from_ = None, to = None):
        # pass
                                
    # @api.method
    # def get_weekly_chart_list(self, user):
        # pass
                                
    # @api.method
    # def get_weekly_track_chart(self, user, from_ = None, to = None):
        # pass
                                
    # @api.method
    # def shout(self, user, message):
        # pass
        
                
# @api.package
# class Venue(Package):                                
    # @api.method
    # def get_events(self, venue, festivalsonly = None):
        # pass
                                    
    # @api.method
    # def get_past_events(self, venue, page = None, limit = None, festivalsonly = None):
        # pass
                                    
    # @api.method
    # def search(self, venue, page = None, limit = None, country = None):
        # pass
        