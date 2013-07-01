from lfm.lfm import request_auto


_pkg = "geo"


def get_events(tag = None, page = None, limit = None, long = None, lat = None, location = None, distance = None, festivalsonly = None):
    data = request_auto(_pkg)
    return data["events"]


def get_metro_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_hype_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_hype_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_unique_artist_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_metro_unique_track_chart(metro, country, page = None, limit = None, start = None, end = None):
    data = request_auto(_pkg)
    return data["toptracks"]


def get_metro_weekly_chart_list(metro):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_metros(country = None):
    data = request_auto(_pkg)
    return data["metros"]


def get_top_artists(country, page = None, limit = None):
    data = request_auto(_pkg)
    return data["topartists"]


def get_top_tracks(country, page = None, limit = None, location = None):
    data = request_auto(_pkg)
    return data["toptracks"]
