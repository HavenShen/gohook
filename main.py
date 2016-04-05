#!/usr/bin/env python
# -*- coding: utf-8 -*
# wikisoo @ Python
# Functions: 微信公众平台接口
# Created By HavenShen on 2013-11-29,Version 0.1

import comm_log
import time
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

#监听端口
define("port", default=8765, help="run on the given port", type=int)
#日志输出
define("log", default=comm_log.get_logging('gohook'), help="TOKEN", type=str)


class MainHandler(tornado.web.RequestHandler):
    #get请求，验证微信接口
    def get(self):
        #输出log
        options.log.info('loginfo:done')
        #验证成功返回
        self.write('done')

    #post请求各种微信post提交过来的消息
    def post(self):
        #输出日志
        options.log.info('loginfo:done')
        self.write('done')


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(options.port)
    print 'ok'
    tornado.ioloop.IOLoop.instance().start()
