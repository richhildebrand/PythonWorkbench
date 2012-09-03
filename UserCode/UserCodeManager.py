import sys, io, pdb
import PythonFileBuilder
import CustomIOManager
from PythonLib import PythonLib

class UserCodeManager:
	USER_FILE_PATH = "UserFiles/"
	pythonFileBuilder = None
	userCodeFilePath = None
	stepNumber = None
	userCode = None
	userID = None

	def __init__(self, userID, userCode):
		self.stepNumber = 0
		self.userID = userID
		self.userCode = userCode
		self.pythonFileBuilder = PythonFileBuilder.PythonFileBuilder()
		self.userCodeFilePath =	self.pythonFileBuilder.buildFile(self.userCode, self.userID)
		
	def executeUserCode(self):
		self.stepNumber = self.stepNumber + 1
		self.__runFile()

	def __runFile(self):
		PythonLib.ensureDirectoryExists(self.USER_FILE_PATH)
		outputFromPDB = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'w+')
		inputForPDB = io.StringIO(self.pythonFileBuilder.getPdcInstructions(self.stepNumber))

		customIOManager = CustomIOManager.CustomIOManager()
		customIOManager.setCustomIO(inputForPDB, outputFromPDB)
		try:
			#thread.start_new_thread(pdb.run, ('import ' + self.userID + 'CodeFile', {}, locals()))
			#Thread(target=pdb.run, args=('import ' + self.userID + 'CodeFile', {}, locals())).start()
			pdb.run('import ' + self.userCodeFilePath, {}, {})
		finally:
			customIOManager.cleanUpCustomIO()