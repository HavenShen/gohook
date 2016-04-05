#!/usr/bin/env python
# -*- coding: utf8 -*-
# comm_log @ Python
# Functions: 自动创建当日备份目录、日志记录、压缩备份文件
# Created By Haven on 2013-11-26,Version 0.1

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='gohook.log',
                    filemode='aw')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
## 
# console = logging.StreamHandler()
# console = setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
def get_logging(name):
    return logging.getLogger(name)