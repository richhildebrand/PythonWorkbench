#https://github.com/pythoncapstone/capstone.git
import pprint
import pdb
import os
import thread

def wrapperFunction():

	a = "mike"
	b = 5
	c = "corey"

	def testFunction():
		rich = "richard"
		print "\ntestFunction scope\n"
		pprint.pprint(locals())

	testFunction()

	#userCode = "import " + "userID.txt" 
	#eval(userCode, {}, locals())
	print "##############"
	import userID

	thread.start_new_thread(userID.userFunctionWrapper())

	print "##############"
		


	print "\nwrapper scope\n"
	pprint.pprint(locals())

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())


