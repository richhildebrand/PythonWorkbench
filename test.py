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

	seth = 'a = "tom"'
	seth2 = 'a + "ben"'
	#empty set limits globals
	exec(seth) in {}, locals()
	result = eval(seth2, {}, locals())
	
	print seth
	print result

	print "\nwrapper scope\n"
	pprint.pprint(locals())

wrapperFunction()

print "\nglobal scope\n"
pprint.pprint(locals())