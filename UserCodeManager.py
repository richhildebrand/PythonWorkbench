import sys
import PythonFileBuilder

class UserCodeManager:
	def __init__(self, userID, userCode):
		self.userID = userID
		self.userCode = userCode
	
	def executeUserCode(self):
		self.__createUserCodeFile()
		self.__runFile()

	def __createUserCodeFile(self):
		pythonFileBuilder = PythonFileBuilder.PythonFileBuilder(self.userCode)
		self.userCode = pythonFileBuilder.buildFile()
		try:
			userCodeFile = open(self.userID+'CodeFile.py', 'w+')
			userCodeFile.write(self.userCode)
		finally:
			userCodeFile.close()

	def __runFile(self):
		#these will change during exec; should be moved out if possible
		defaultStdin = sys.stdin
		defaultStdout = sys.stdout
		try:
			exec('import ' + self.userID + 'CodeFile', {}, {})
		except:
			print "needed to catch hard brake from pdb"
		finally:
			sys.stdin = defaultStdin
			sys.stdout = defaultStdout