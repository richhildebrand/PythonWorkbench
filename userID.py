import pprint
import pdb
def userFunctionWrapper():
	for line in sys.stdin:
		print "printing a line" line

	userA = 3
	userB = 4
	userC = userA + userB

userFunctionWrapper()