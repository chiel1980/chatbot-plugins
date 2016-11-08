from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import urllib2
import json

class ChuckNorrisPlugin(WillPlugin):

    @respond_to("chuck joke please")
    def say_chucknorris_will(self, message):
        req = urllib2.Request("http://api.icndb.com/jokes/random")
        full_json = urllib2.urlopen(req).read()
        full = json.loads(full_json)
        print full['value']['joke']
        self.reply(message, full['value']['joke'])
