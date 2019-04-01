# -*- coding: utf-8 -*-
from __future__ import unicode_literals
for i in range(1,5):
    for j in range(1,5):
    	if (i+j>4):
    		print "*",
    		for k in range(1,2):
    			if (i+j>5):
    				print "*",
    	else:
    		print " ",
    print
