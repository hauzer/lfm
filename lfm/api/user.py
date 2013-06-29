from lfm import lfm


_pkg = "user"


def get_artist_tracks(user, artist, page = None, starttimestamp = None, endtimestamp = None):
    data = lfm.request_auto(_pkg)
    return data["artisttracks"]


def get_banned_tracks(user, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["bannedtracks"]


def get_events(user, page = None, limit = None, festivalsonly = None):
    data = lfm.request_auto(_pkg)
    return data["events"]


def get_friends(user, page = None, limit = None, recenttracks = None):
    data = lfm.request_auto(_pkg)
    return data["friends"]


def get_info(user = None):
    data = lfm.request_auto(_pkg)
    return data["user"]


def get_loved_tracks(user, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["lovedtracks"]


def get_neighbours(user, limit = None):
    data = lfm.request_auto(_pkg)
    return data["neighbours"]


def get_new_releases(user, userecs = None):
    data = lfm.request_auto(_pkg)
    return data["albums"]


def get_past_events(user, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["events"]


def get_personal_tags(user, tag, taggingtype, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["taggings"]


def get_playlists(user):
    data = lfm.request_auto(_pkg)
    return data["playlists"]


def get_recent_stations(user, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["recentstations"]


def get_recent_tracks(user, extended = None, page = None, limit = None, from_ = None, to = None):
    data = lfm.request_auto(_pkg)
    return data["recenttracks"]


def get_recommended_artists(page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["recommendations"]


def get_recommended_events(page = None, limit = None, latitude = None, longitude = None, festivalsonly = None):
    data = lfm.request_auto(_pkg)
    return data["events"]


def get_shouts(user, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["shouts"]


def get_top_albums(user, period = None, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["topalbums"]


def get_top_artists(user, period = None, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["topartists"]


def get_top_tags(user, limit = None):
    data = lfm.request_auto(_pkg)
    return data["toptags"]


def get_top_tracks(user, period = None, page = None, limit = None):
    data = lfm.request_auto(_pkg)
    return data["toptracks"]


def get_weekly_album_chart(user, from_ = None, to = None):
    data = lfm.request_auto(_pkg)
    return data["weeklyalbumchart"]


def get_weekly_artist_chart(user, from_ = None, to = None):
    data = lfm.request_auto(_pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(user):
    data = lfm.request_auto(_pkg)
    return data["weeklychartlist"]


def get_weekly_track_chart(user, from_ = None, to = None):
    data = lfm.request_auto(_pkg)
    return data["weeklytrackchart"]


def shout(user, message):
    data = lfm.request_auto(_pkg)
