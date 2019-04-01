# -*- coding: utf-8 -*-
from __future__ import unicode_literals
k=5
for i in range(1,5):
	for j in range (1,8):
		if (i+j==5) or i == 4 or j-i==3:
			print "*",
			
		else :
			print " ",
	print 