# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 17:21:53 2017

@author: xiaomeng.yang
"""
import pandas as pd 
from pyhive import presto

cursor = presto.connect(host='presto-master-lb.prod.hulu.com', port = 8080, 
                        catalog = 'hive', username = 'xiaomeng.yang@hulu.com').cursor()
cursor.execute('select * from zzz_emma_genre_16H1_2 limit 10')
result = cursor.fetchall()
result

df = pd.DataFrame(result, columns = ['userid','genre', 'rnk', 'dependency_ratio', 'cumu_ratio'])