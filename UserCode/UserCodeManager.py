import sys, io, pdb
import PythonFileBuilder
from PythonLib import PythonLib

class UserCodeManager:
	USER_FILE_PATH = "UserFiles/"

	def __init__(self, userID, userCode):
		self.pythonFileBuilder = PythonFileBuilder.PythonFileBuilder()
		self.stepNumber = 0
		self.userCode = userCode
		self.userID = userID
		self.__onInit()

	def executeUserCode(self):
		self.stepNumber = self.stepNumber + 1
		self.__runFile()

	def __onInit(self):
		self.userCodeFilePath =	self.pythonFileBuilder.buildFile(self.userCode, self.userID)

	def __runFile(self):
		defaultStdin = sys.stdin
		defaultStdout = sys.stdout
		sys.stdin = io.StringIO(self.pythonFileBuilder.getPdcInstructions(self.stepNumber))
		PythonLib.ensureDirectory(self.USER_FILE_PATH)
		sys.stdout = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'w+')
		try:
			#thread.start_new_thread(pdb.run, ('import ' + self.userID + 'CodeFile', {}, locals()))
			#Thread(target=pdb.run, args=('import ' + self.userID + 'CodeFile', {}, locals())).start()
			pdb.run('import ' + self.userCodeFilePath, {}, {})
		finally:
			sys.stdin.close()
			sys.stdout.close()
			sys.stdin = defaultStdin
			sys.stdout = defaultStdout
