import io, pdb, re
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
	currentLineInUserCode = None

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

	def executeEntireUserCode(self):
		numLines = self.__lineCount()
		i = 0
		while i < numLines :
			self.stepNumber = self.stepNumber + 1
			self.__runFile()
			i = i + 1
		return self.__resultOfStepInUserCode()

	def runTestsOnUserCode(self):
		testRunner = TestRunner.TestRunner(self.userID, self.userCode, self.unitTests)
		return testRunner.getResults()

	def __lineCount(self):
		lineCount = 0
		for character in self.userCode:
			if character == '\n':
				lineCount += 1
		return lineCount + 1

	def __runFile(self):
		PythonLib.ensureDirectoryExists(self.USER_FILE_PATH)
		outputFromDebugger = open(self.USER_FILE_PATH + self.userID + 'ResultFile.txt', 'w+')
		inputForDebugger = io.StringIO(unicode(self.pythonFileBuilder.getPdcInstructions(self.stepNumber)))
		#print str(self.pythonFileBuilder.getPdcInstructions(self.stepNumber))
		debugger = pdb.Pdb(completekey='tab', stdin=inputForDebugger, stdout=outputFromDebugger)
		self.userCodeException = ''
		try:
			debugger.run('import ' + self.userCodeFilePath, {}, {})
			fileParser = FileParser.FileParser(self.USER_FILE_PATH + self.userID + 'ResultFile.txt')
			self.currentLineInUserCode = fileParser.get_current_line()
		except Exception, e:
			self.userCodeException = PythonLib.parseExceptionMessage(e)
			# Exception line number is off by one
			self.currentLineInUserCode = PythonLib.parseExceptionLineNumber(e)-1
		finally:
			outputFromDebugger.close()
			inputForDebugger.close()

	def __resultOfStepInUserCode(self):
		fileParser = FileParser.FileParser(self.USER_FILE_PATH + self.userID + 'ResultFile.txt')
		userStepResult = {}
		userStepResult['exception'] = self.userCodeException
		userStepResult['lineNumber'] = self.currentLineInUserCode
		userStepResult['localVars'] = fileParser.get_local_vars()
		pdbOutput= fileParser.parse_for_current_frame()
		rawOutputString = pdbOutput.replace('\n\r','\\n\\r')
		#rawOutputString = rawOutputString.replace('{','')
		#rawOutputString = rawOutputString.replace('}','')
		#rawOutputString = rawOutputString.replace(':','=')
		rawOutputString = re.sub(r'\<function.*\>', 'function def', rawOutputString)
		#formatOutString = rawOutputString.replace(', ', '\r')
		userStepResult['stackInfo'] = rawOutputString
		return userStepResult