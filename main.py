#coding:utf8
import sys
sys.path.append("./lib")
import web
import json
import hashlib

import filesave_lib
import urllib,StringIO

import rediswebpy
import models
import views
import config

import time

from functools import wraps

#web.config.session_parameters['cookie_name'] = 'futoubangid'
#web.config.session_parameters.timeout = 86400*2 #24 * 60 * 60, # 24 hours   in seconds
#web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
#web.config.session_parameters['expired_message'] = 'Session expired'
#web.config.session_parameters['httponly'] = False

#web.config.session_parameters['cookie_domain'] = 'localhost'
#web.config.session_parameters['ignore_expiry'] = True
#web.config.session_parameters['ignore_change_ip'] = True

urls = (
	    '/', 'index',
		'/upload', 'upload',
	)

okbuydb = None
app = web.application(urls, globals())

web.config.debug = False

##session
#if web.config.get('_session') is None:
#	session = web.session.Session(app, rediswebpy.RedisStore(initial_flush=False), initializer={'count': 0})
#	web.config._session = session
#else:
#	session = web.config._session

render = web.template.render('templates/')


class upload():
	def POST(self):
		x = web.input()
		saveFile = filesave_lib.SaveFile()
		saveFile.save_disk_file(StringIO.StringIO(x.myfile))
		return 'OK'

class index:
	def GET(self,name=''):
		return "welcome to upload "

	def POST(self):
		pass

if __name__ == "__main__":
	app.run()
