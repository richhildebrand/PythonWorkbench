#https://github.com/pythoncapstone/capstone.git
import pprint
import pdb
import os
from threading import Thread

def wrapperFunction():

	a = "mike"
	b = 5
	c = "corey"

	print "\nwrapper scope\n"
	pprint.pprint(locals())

	print "##### Call UserID #####"
	#os.system()

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())


