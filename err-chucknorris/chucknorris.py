from datetime import datetime
import logging
import sys
import urllib2
import json

from config import CHATROOM_PRESENCE
from feedparser import parse

if sys.version_info.major <= 2:
    from BeautifulSoup import BeautifulSoup
else:
    from bs4 import BeautifulSoup

# Backward compatibility
from errbot.version import VERSION
from errbot.utils import version2array
if version2array(VERSION) >= [1,6,0]:
    from errbot import botcmd, BotPlugin
else:
    from errbot.botplugin import BotPlugin
    from errbot.jabberbot import botcmd


__author__ = 'mvanes'

class ChuckNorrisPlugin(BotPlugin):
     """Example 'Hello, world!' plugin for Errbot"""

     @botcmd
     def chucknorris_joke(self, msg, args):
         req = urllib2.Request("http://api.icndb.com/jokes/random")
         full_json = urllib2.urlopen(req).read()
         full = json.loads(full_json)
         return full['value']['joke']
