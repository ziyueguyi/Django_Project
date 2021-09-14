# -*- coding:utf-8 -*-
# @文件名称  :db_sqlite
# @项目名称  :Django_Project.py
# @软件名称  :PyCharm
# @创建时间  : 2021-09-14 8:40
# @用户名称  :DELL
import os
import sqlite3
from Django_Project.settings import DATABASES

sqlite3.connect(DATABASES['default']['NAME'])
