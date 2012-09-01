import pprint
import pdb
import sys
def userFunctionWrapper():
	instructions = open("PdbInstructions.txt")
	sys.stdin = instructions
	sys.stdout = open("bobResultFile.txt", "w+")
	#for line in instructions:
	#	print line
	pdb.set_trace()
	userA = 3
	userB = 4
	userC = userA + userB

userFunctionWrapper()