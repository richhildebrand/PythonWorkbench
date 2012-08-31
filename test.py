#https://github.com/pythoncapstone/capstone.git
import pprint

a = "mike"
b = 5
c = "corey"

def testFunction():
	rich = "richard"
	print "\nttestFunction scope\n"
	pprint.pprint(locals())

testFunction()

print "\nglobal scope\n"

pprint.pprint(locals())