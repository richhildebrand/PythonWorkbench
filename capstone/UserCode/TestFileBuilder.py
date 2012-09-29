class TestFileBuilder
	methodBody = None
	methodCalls = None
	testFilePath = None

	def __init__(self, userID, methodBody, methodCalls):
		self.methodBody = methodBody
		self.methodCalls = methodCalls
		self.testFilePath = userID + 'TestFile'

	def getResults(self):
		#methodCallResults = {}
		#for method in self.methodCalls:
			#self.__buildFile(self.methodBody, method)
			#try:
				#methodCallResults[method] = self.__runTestFile
			#except:
				#methodCallResults[method] = e
		#return methodCallResults

	def __buildFile(self, methodBody, methodCall):
		code = self.methodBody
		code += '\nreturn '+ methodCall
		self.__createUserTestFile(code)

	def __runTestFile(self):
		#iWish = 'import ' + self.testFilePath
		

	def __createUserCodeFile(self, code, filePrefix):
		try:
			codeFile = open(self.testFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()