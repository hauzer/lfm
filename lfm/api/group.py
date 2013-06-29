from lfm import lfm


pkg = "group"


def get_hype(group):
    data = lfm.request(pkg)
    return data["weeklyartistchart"]


def get_members(group, page = None, limit = None):
    data = lfm.request(pkg)
    return data["members"]


def get_weekly_album_chart(group, from_ = None, to = None):
    data = lfm.request(pkg)
    return data["weeklyalbumchart"]


def get_weekly_artist_chart(group, from_ = None, to = None):
    data = lfm.request(pkg)
    return data["weeklyartistchart"]


def get_weekly_chart_list(group):
    data = lfm.request(pkg)
    return data["weeklychartlist"]


def get_weekly_track_chart(group, from_ = None, to = None):
    data = lfm.request(pkg)
    return data["weeklytrackchart"]
