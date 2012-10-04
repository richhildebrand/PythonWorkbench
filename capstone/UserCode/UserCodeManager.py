import io, pdb
import PythonFileBuilder
import TestRunner
import FileParser
from capstone.PythonLib import PythonLib
from collections import namedtuple

class UserCodeManager:
	USER_FILE_PATH = "UserFiles/"
	pythonFileBuilder = None
	userCodeFilePath = None
	stepNumber = None
	unitTests = None
	userCode = None
	userID = None
	userCodeException = None

	def __init__(self, userID, userCode, unitTests):
		self.stepNumber = 0
		self.userID = userID
		self.userCode = userCode
		self.unitTests = unitTests
		self.pythonFileBuilder = PythonFileBuilder.PythonFileBuilder()
		self.userCodeFilePath =	self.pythonFileBuilder.buildFile(userCode + '\n' + unitTests, userID)
		
	def executeStepInUserCode(self):
		self.stepNumber = self.stepNumber + 1
		self.__runFile()
		return self.__resultOfStepInUserCode()

	def runTestsOnUserCode(self):
		testRunner = TestRunner.TestRunner(self.userID, self.userCode, self.unitTests)
		return testRunner.getResults()

	def __runFile(self):
		PythonLib.ensureDirectoryExists(self.USER_FILE_PATH)
		outputFromDebugger = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'w+')
		inputForDebugger = io.StringIO(unicode(self.pythonFileBuilder.getPdcInstructions(self.stepNumber)))

		debugger = pdb.Pdb(completekey='tab', stdin=inputForDebugger, stdout=outputFromDebugger)
		self.userCodeException = ''
		
		try:
			debugger.run('import ' + self.userCodeFilePath, {}, {})
		except Exception, e:
			self.userCodeException = e
		finally:
			outputFromDebugger.close()
			inputForDebugger.close()

	def __resultOfStepInUserCode(self):
		# Need replace with actual exception; localVars; lineNumber
		fileParser = FileParser.FileParser(self.USER_FILE_PATH + self.userID + 'ResultFile.txt')
		userStepResult = {}
		userStepResult['exception'] = self.userCodeException
		userStepResult['localVars'] = fileParser.get_local_vars()
		userStepResult['lineNumber'] = fileParser.get_current_line()
		return userStepResult