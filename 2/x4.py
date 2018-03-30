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


import x2
import x3

xxx = [ 
        {'A':'no'                ,'X':'FT ID',              },
        {'A':'cat_l0'            ,'X':'Category',           },
        {'A':'cat_l1'            ,'X':'Component',          },
        {'A':'cat_l2'            ,'X':'Module',             },
        {'A':'headline'          ,'X':'Title',              },
        {'A':'description'       ,'X':'Description',        },
        {'A':'source'            ,'X':'Requirement From',   },
        {'A':'develop_source'    ,'X':'Develop Source',     },
        {'A':'fpm'               ,'X':'Feature PM',         },
        {'A':'for_customer'      ,'X':'For Customer',       },
        {'A':'label'             ,'X':'Label',              },
        ]
    
def analyze_main_map(main_map):

    LIST_X  = []#上传下载使用这个数据
    MAP_XA = {}#上传下载使用这个数据
    
    for node in main_map:
        if node['X']:
            LIST_X.append(node['X'])
            MAP_XA.update({node['X']:node['A']})
    
    return LIST_X,MAP_XA


LIST_X,MAP_XA = analyze_main_map(xxx)
print LIST_X
print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print MAP_XA
