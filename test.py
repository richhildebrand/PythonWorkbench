#https://github.com/pythoncapstone/capstone.git
import pprint
import pdb
import os
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

	import userID
	#userID.userFunctionWrapper()

	#pdb.run('userID.userFunctionWrapper()')
	print "##############"
	f=os.popen("python userID.py a b c")
	for i in f.readlines():
		print "myresult:",i,
	print "##############"

	print "\nwrapper scope\n"
	pprint.pprint(locals())

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())


