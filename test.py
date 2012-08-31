import pprint

print "Hello world"

a = "mike"
b = 5
c = "corey"

def test():
	rich = "richard"
	print "fine indent"
	pprint.pprint(locals())
test()

print "\nsecond scope\n"

pprint.pprint(locals())