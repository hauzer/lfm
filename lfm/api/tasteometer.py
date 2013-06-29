from lfm import lfm


pkg = "tasteometer"


def compare(type1, value1, type2, value2, limit = None):
    data = lfm.request_auto(pkg)
    return data["comparison"]


def compare_group():
    pass
