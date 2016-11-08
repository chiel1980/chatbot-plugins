import sopel.module
from datetime import datetime
import logging
import sys
import urllib2
import json
from feedparser import parse

if sys.version_info.major <= 2:
    from BeautifulSoup import BeautifulSoup
else:
    from bs4 import BeautifulSoup

@sopel.module.commands('chucknorris')
def chucknorris_joke(bot, trigger):
    req = urllib2.Request("http://api.icndb.com/jokes/random")
    full_json = urllib2.urlopen(req).read()
    full = json.loads(full_json)
    #return full['value']['joke']
    bot.reply(full['value']['joke'])
