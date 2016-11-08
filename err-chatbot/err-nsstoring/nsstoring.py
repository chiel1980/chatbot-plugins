from datetime import datetime
import logging
import sys
import urllib2
#import xml.etree import ElementTree 
import re

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

class NSStoringPlugin(BotPlugin):

     @botcmd
     def nsstoring(self, msg, args):
        SERVER = 'webservices.ns.nl'
        authinfo = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # realm, SERVER variable, username, password
        authinfo.add_password(None, SERVER, 'username', 'token')
        page = 'HTTP://'+SERVER+'/ns-api-storingen?station=Utrecht+Centraal'
        handler = urllib2.HTTPBasicAuthHandler(authinfo)
        myopener = urllib2.build_opener(handler)
        opened = urllib2.install_opener(myopener)
        output = urllib2.urlopen(page)
	return output.read()
