# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:45:03 2018

@author: gigabyte
"""

import csv

category = input()

with open('TED_TAGS_Guillaume2.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') # good point by @paco
     for row in reader:
         nb = row[0]
         for field in row:
              if field == category:
                  print ("is in talk/lecture " + str(nb))
