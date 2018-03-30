# -*- coding: utf-8 -*- 
#!/usr/bin/python
import MySQLdb
from datetime import datetime, timedelta,date
import time

import calendar

import pdb
import json
import binascii

import xlrd

import chardet
import re
import pickle

user = {"a":0}

class my_class():  
    def __init__(self):
        print "x2 init()"
 
    def run(self):
		print "x2 run()----------------------"
		global user
		user = {"a":2}
		print "------------------------------"
		
		