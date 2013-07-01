from lfm.lfm import request_auto


_pkg = "tasteometer"


def compare(type1, value1, type2, value2, limit = None):
    data = request_auto(_pkg)
    return data["comparison"]
