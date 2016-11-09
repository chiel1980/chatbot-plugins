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

@sopel.module.commands('nsstoring')
def nsstoring(bot, trigger):
    SERVER = 'webservices.ns.nl'
    USERNAME = 'mve@pragmasec.nl'
    TOKEN = '***YOURTOKENHERE***'
    authinfo = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # realm, SERVER variable, username, password
    authinfo.add_password(None, SERVER, USERNAME, TOKEN)
    page = 'HTTP://'+SERVER+'/ns-api-storingen?station=ut'
    handler = urllib2.HTTPBasicAuthHandler(authinfo)
    myopener = urllib2.build_opener(handler)
    opened = urllib2.install_opener(myopener)
    output = urllib2.urlopen(page)
    bot.reply(output.read())
