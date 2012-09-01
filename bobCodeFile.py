
import sys
import pprint
import pdb
def userCodeWrapper():
	print "hello world"
	print "line2"
	a=3
	b=4
	c = a + b
	sys.stdin = open("PdbInstructions.txt")
	sys.stdout = open("bobResultFile.txt", "w+")
	pdb.set_trace()
	print a
	print b
	print c
userCodeWrapper()