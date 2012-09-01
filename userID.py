import pprint
def userFunctionWrapper():
	userA = 3
	userB = 4
	userC = userA + userB
	print "\n#############\nStart userFunctionWrapper"
	pprint.pprint(locals())
	print "\n#############\nEnd userFunctionWrapper"