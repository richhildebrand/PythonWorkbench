import sys, io, pdb
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
		defaultStdin = sys.stdin
		defaultStdout = sys.stdout
		sys.stdin = io.StringIO("step")
		sys.stdout = open(self.userID + 'ResultFile.txt', 'w+')
		
		try:
			#thread.start_new_thread(pdb.run, ('import ' + self.userID + 'CodeFile', {}, locals()))
			#Thread(target=pdb.run, args=('import ' + self.userID + 'CodeFile', {}, locals())).start()
			pdb.run('import ' + self.userID + 'CodeFile', {}, {})
		except:
			print "line needed for catch"
		finally:
			sys.stdin.close()
			sys.stdout.close()
			sys.stdin = defaultStdin
			sys.stdout = defaultStdout
