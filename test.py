#https://github.com/pythoncapstone/capstone.git
import pprint
import pdb
import os
from threading import Thread

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
	myfunction = userID.userFunctionWrapper()
	try:
		Thread(target=myfunction, args=('MyStringHere',1)).start()
	except Exception, errtxt:
		print errtxt
	print "##############"
		


	print "\nwrapper scope\n"
	pprint.pprint(locals())

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())


