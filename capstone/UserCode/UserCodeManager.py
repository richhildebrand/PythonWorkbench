import io, pdb
import PythonFileBuilder
from capstone.PythonLib import PythonLib
from collections import namedtuple

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
		
	def executeStepInUserCode(self):
		self.stepNumber = self.stepNumber + 1
		self.__runFile()
		return self.__resultOfStepInUserCode()

	def __runFile(self):
		PythonLib.ensureDirectoryExists(self.USER_FILE_PATH)
		outputFromDebugger = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'w+')
		inputForDebugger = io.StringIO(unicode(self.pythonFileBuilder.getPdcInstructions(self.stepNumber)))

		debugger = pdb.Pdb(completekey='tab', stdin=inputForDebugger, stdout=outputFromDebugger)
		try:
			debugger.run('import ' + self.userCodeFilePath, {}, {})
		except Exception, e:
			print e
		finally:
			outputFromDebugger.close()
			inputForDebugger.close()

	def __resultOfStepInUserCode(self):
		# Need replace with actual exception; localVars; lineNumber
		userStepResult = {}
		userStepResult['exception'] = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'r').read()
		userStepResult['localVars'] = "localVars"
		userStepResult['lineNumber'] = 42

		return userStepResult