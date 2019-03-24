import sys


def to_string(arr):
    res = ''
    for item in arr:
        res += str(item) + ' or '
    return res.strip(' or ')


def search_key(key):
    for item in sys.argv:
        if item.find(key) >= 0:
            return True
    return False


def show_help():
    exit('fe')