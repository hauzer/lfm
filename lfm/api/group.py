from lfm.lfm import request_auto


_pkg = "group"


def get_hype(group):
    data = request_auto(_pkg)
    return data["weeklyartistchart"]


def get_members(group, page = None, limit = None):
    data = request_auto(_pkg)
    return data["members"]


def get_weekly_album_chart(group, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklyalbumchart"]


def get_weekly_artist_chart(group, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(group):
    data = request_auto(_pkg)
    return data["weeklychartlist"]


def get_weekly_track_chart(group, from_ = None, to = None):
    data = request_auto(_pkg)
    return data["weeklytrackchart"]
