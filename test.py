#https://github.com/pythoncapstone/capstone.git
import pprint
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
	userID.userFunctionWrapper()

	print "\nwrapper scope\n"
	pprint.pprint(locals())

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())