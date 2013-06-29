from lfm import lfm


_pkg = "tasteometer"


def compare(type1, value1, type2, value2, limit = None):
    data = lfm.request_auto(_pkg)
    return data["comparison"]
