from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import urllib2, sys, re
import ssl
import datetime
import json
from string import maketrans

class RTSPlugin(WillPlugin):

    @respond_to("rts totalRevenue please")
    def say_rts_will(self, message):
	today = datetime.date.today()
	SERVER = 'URLTHATYOULIKE'
	authinfo = urllib2.HTTPPasswordMgrWithDefaultRealm()
	# realm, SERVER variable, username, password
	authinfo.add_password(None, SERVER, 'username', 'superpassword')
	# this 'fixes' certificate warnings and ignores them
	ssl._create_default_https_context = ssl._create_unverified_context
	page = 'HTTPS://'+SERVER+'/rest/orders/'+ str(today) +'/URITHATYOULIKE/daily?nocache=1447950892975'
	handler = urllib2.HTTPBasicAuthHandler(authinfo)
	myopener = urllib2.build_opener(handler)
	opened = urllib2.install_opener(myopener)
	output = urllib2.urlopen(page)
	# the page opened is in json format so load it adn then search for strings matching EXCL and TOTAL
	data = json.load(output)  
	for item in data:
  	    if item['inclusiveOrExclusive'] == "EXCL" and item['aggregationType'] == "TOTAL":
		# add euro symbol in front of our number (json object totalRevenue)
        	print('\xe2\x82\xac')+str(item['totalRevenue']) 
		# reply with euro symbol, our totalRevenue number with commas after the 1000 (,) but translate the commas back into european dots/decimals
		self.reply(message, ('\xe2\x82\xac{:,}'.format(item['totalRevenue']).translate(maketrans(',.','.,')))) 
