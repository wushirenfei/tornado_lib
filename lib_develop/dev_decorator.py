# -*- coding: utf-8 -*-
import json
import tornado.web
from tornado.ioloop import IOLoop
from tornado.options import options, define
from tornado.httpserver import HTTPServer
from tornado import gen
# from common.data_type import ObjectDict
from get_url_params import get_url_params

import functools

define('port', default=8080, type=int)

def sub_company(fun):

    @functools.wraps(fun)
    def wrapper(self, *args, **kwargs):
        # print(args[0].params)
        # args[0].params.sub_company = 'obj' if args[0].params.did else None
        print(self.params)
        return fun(self, *args, **kwargs)

    return wrapper


class MyHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.params = get_url_params(self.request.arguments)
        #

    @gen.coroutine
    @sub_company
    def get(self):
        print(self.params)
        self.write('hello world! -- {}')


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/index', MyHandler),
    ])
    server = HTTPServer(app)
    server.listen(options.port)
    IOLoop.instance().start()