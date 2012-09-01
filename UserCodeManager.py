import sys
class UserCodeManager:
	def __init__(self, userID, userCode):
		self.userID = userID
		self.userCode = userCode
	
	def executeUserCode(self):
		self.__createUserCodeFile()
		self.__runFile()

	def __createUserCodeFile(self):
		try:
			userCodeFile = open(self.userID+'CodeFile.py', 'w+')
			userCodeFile.write(self.userCode)
		finally:
			userCodeFile.close()

	def __runFile(self):
		#try:
		#sys.stdin = 'PdbInstructions.txt'
		#resultFile = open(self.userID + 'ResultFile.txt', 'w+')
		#sys.stdout = resultFile
		exec('import ' + self.userID + 'CodeFile', {}, {})

	#def returnUserCode():
	#	return userID + 'ResultFile.txt'