#!/usr/bin/env python
# -*- coding: utf-8 -*
# gohook @ Python
# Functions: WebHook自动部署代码
# Created By HavenShen on 2016-04-05,Version 0.1

import comm_log
import subprocess
import json
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

#监听端口
define("port", default=8765, help="run on the given port", type=int)
#日志输出
define("log", default=comm_log.get_logging('gohook'))
#希望自动部署项目路径
file_path = '/home/wwwroot/xxx'

def cd_path():
	cmd = ['cd',file_path]
	p = subprocess.Popen(cmd,cwd=file_path)
	p.wait()

def pull():
	cmd = ['git','pull']
	p = subprocess.Popen(cmd,cwd=file_path)
	p.wait()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('get done.')

	def post(self):
		data = tornado.escape.json_decode(self.request.body)
		if data['token'] == 'gohook':
			cd_path()
			pull()
			options.log.info('git pull done.')
		else:
			options.log.info('git pull error.[token is false]')

		self.write('post done.')

application = tornado.web.Application([
	(r"/gohook", MainHandler),
])

if __name__ == "__main__":
	application.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
