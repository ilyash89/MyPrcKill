#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

########## IMPORT ###########
import pymysql
import logging

########## GLOBAL ##############
logging.basicConfig(filename='MyPrcKill.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


####### CONFIG
conn = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='', charset='utf8')
timeout = 60

######### PROGRAM ###########

cur = conn.cursor()
cur.execute('SHOW FULL PROCESSLIST;')
LL = []
for r in cur:
    li=list(r)
    if li[1]=='root' and li[5]>timeout: 
	LL.append(li)

for l in LL:
    cur.execute('KILL ' + str(l[0])+ ';')
    #print(l[7])
    logging.info('QUERY="'+str(l[7])+ '" EXEC_TIME='+str(li[5]))
cur.close()
