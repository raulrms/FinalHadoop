#!/usr/bin/env python

import sys  
(name, lastid) = (None,None)
for line in sys.stdin:
	(id, fall, year, reclat,reclong) = line.split(',') 
	if lastid == id:
		print '%s\t%s\t%s' % (name, reclat, reclong)
