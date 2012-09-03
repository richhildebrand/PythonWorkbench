class PythonFileBuilder:
	LINES_ADDED_FROM_WRAPPER = 5

	def buildFile(self, code, filePrefix):
		code = self.__addTabToNewLines(code)
		code = self.__addWrapperFunction(code)
		code = self.__addCallForWrapperFunction(code)
		newFilePath = self.__createUserCodeFile(code, filePrefix)
		return newFilePath

	def getPdcInstructions(self, stepNumber):
		instructions = "step;;" * (stepNumber + self.LINES_ADDED_FROM_WRAPPER)
		instructions = instructions + "locals()"
		return instructions

	def __addTabToNewLines(self, code):
		return code.replace('\n', '\n\t')

	def __addWrapperFunction(self, code):
		return 'def WrapperFunction():\n\t' + code

	def __addCallForWrapperFunction(self, code):
		return code + "\nWrapperFunction()"

	def __createUserCodeFile(self, code, filePrefix):
		fullFilePath = filePrefix + 'CodeFile.py'
		try:
			codeFile = open(fullFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()
		return fullFilePath