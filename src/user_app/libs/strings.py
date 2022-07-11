"""
libs.string
By default, uses 'en-gb.json' file inside 'strings' folder
"""
import json

default_locale = "en-gb"
cached_strings = {}


def refresh():
    """Refreshing cached_string variable"""
    print('Refreshing ...')
    global cached_strings
    with open(f"strings/{default_locale}.json") as string:
        cached_strings = json.load(string)


def gettext(name):
    return cached_strings[name]


def gettext_message(name):
    return {"message": gettext(name)}


refresh()
