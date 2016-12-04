#!/usr/bin/env python

import sys  
for line in sys.stdin:
 (name, id, recclass, mass) = line.split(',') 
 if recclass == 'H5':
    print '%s\t%s' % (name, id)
