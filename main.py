#!/usr/bin/env python

# [START imports]
import os
import urllib

import json
import logging

import jinja2
import webapp2
import urllib
import httplib2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render({}))


class PressKit(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/press-kit.html')
        self.response.write(template.render({}))


class KinkyChat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/kinky-chat.html')
        self.response.write(template.render({}))


class SendEmail(webapp2.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        logging.info('data is %s', data)
        http = httplib2.Http()
        http.add_credentials('api', 'key-3c814b3e71553c0c5962f321abf437f9')
        url = 'https://api.mailgun.net/v3/sandbox9f37f33e9cea4b4dbc3d092a6eb7b6e6.mailgun.org/messages'
        data = {
            'from': 'PISS-OFF Mailgun <postmaster@sandbox9f37f33e9cea4b4dbc3d092a6eb7b6e6.mailgun.org>',
            'to': 'PISS-OFF! <pissoffbrooklyn@gmail.com>',
            'subject': data['subject'],
            'text': data['text']
        }
        resp, content = http.request(url, 'POST', urllib.urlencode(data))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/index.*', MainPage),
    ('/press-kit.*', PressKit),
    ('/kinky-chat.*', KinkyChat),
    ('/send-email', SendEmail)
], debug=True)
