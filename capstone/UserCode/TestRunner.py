class TestRunner:
	methodBody = None
	unitTests = None

	def __init__(self, userID, methodBody, unitTests):
		self.methodBody = methodBody
		self.unitTests = unitTests

	def getResults(self):
		tests = self.unitTests.split('\n')
		testResults = {}
		for test in tests:
			if  len(str(test)) > 0:
				try:
					testResults[test] = self.__runTest(self.methodBody, test)
					print "test result = " + testResults[test]
				except Exception, e:
					print e
					testResults[test] = e
		return testResults

	def __runTest(self, methodBody, unitTest):
		code = self.methodBody
		code += '\ntheResultOfThisUnitTestIsEqualTo = ' + unitTest
		compiledCode = compile(code, 'deletemeResultFile', 'exec')
		exec(compiledCode)
		return str(theResultOfThisUnitTestIsEqualTo)