class TestFileBuilder:
	methodBody = None
	methodCalls = None
	testFilePath = None

	def __init__(self, userID, methodBody, methodCalls):
		self.methodBody = methodBody
		self.methodCalls = methodCalls
		self.testFilePath = userID + 'TestFile'

	def getResults(self):
		tests = self.methodCalls.split('\n')
		methodCallResults = {}
		for test in tests:
			if  len(str(test)) > 0:
				self.__buildFile(self.methodBody, test)
				try:
					methodCallResults[test] = self.__runTestFile()
					print 'result'
					print methodCallResults[test]
				except Exception, e:
					print e
					methodCallResults[test] = e
		return methodCallResults

	def __buildFile(self, methodBody, methodCall):
		code = self.methodBody
		code += '\ntheResultOfThisUnitTestIsEqualTo = ' + methodCall
		compiledCode = compile(code, 'deletemeResultFile', 'exec')
		exec(compiledCode)
		print 'answer=' + str(theResultOfThisUnitTestIsEqualTo)
		self.__createUserTestFile(code)

	def __runTestFile(self):
		print "__runTestFile"
		fileToImport = '\'' + self.testFilePath + '\''
		y = "__import__("
		y += fileToImport
		y += ")"
		
		x = 'h'
		return x
		#iWish = 'import ' + self.testFilePath
		
	def __createUserTestFile(self, code):
		try:
			codeFile = open(self.testFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()