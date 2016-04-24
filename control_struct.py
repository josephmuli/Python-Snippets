#!/usr/bin/env python2

#a control structure us any kind of statement that can change the path of 
# the code's execution

import sys 	#used for sys.exit function

int_condition = 5

if int_condition < 6:
	sys.exit("int_condition must be >=6")
else:
	print("int_condition was >= 6 - continuing")
