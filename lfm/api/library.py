from lfm import lfm

pkg = "library"


def add_album(albums):
    params = {}

    for i, album in enumerate(albums):
        istr = "[" + str(i) + "]"

        params["artist" + istr] = album[0]
        params["album" + istr] = album[1]

    params["albums"] = None

    data = lfm.request_auto(pkg, params)
    return data["albums"]
