class PythonFileBuilder:
	STEPS_NEED_TO_FIRST_LINE = 6

	def buildFile(self, code, filePrefix):
		code = self.__addTabToNewLines(code)
		code = self.__addWrapperFunction(code)
		code = self.__addFrameGetter(code)
		code = self.__addCallForWrapperFunction(code)
		newFilePath = self.__createUserCodeFile(code, filePrefix)
		return newFilePath

	def getPdcInstructions(self, stepNumber):
		instructions = "step;;" * (stepNumber + self.STEPS_NEED_TO_FIRST_LINE)
		instructions = instructions + "getFramesAndVars();;list"
		return instructions

	def __addTabToNewLines(self, code):
		return code.replace('\n', '\n\t')

	def __addWrapperFunction(self, code):
		return '\ndef GlobalScope():\n\t' + code

	def __addCallForWrapperFunction(self, code):
		return code + "\nGlobalScope()"

	def __addFrameGetter(self, code):
		frameGetter = 'import sys, inspect, linecache'
		frameGetter += '\ndef getFramesAndVars():'
		frameGetter += '\n\tbase = sys._getframe(0)'
		frameGetter += '\n\tf = base.f_back'
		frameGetter += '\n\twhile f.f_back:'
		frameGetter += '\n\t\tprint "FunctionName===" + str(f.f_code.co_name) + "===LocalVars: " + str(f.f_locals)'
		frameGetter += '\n\t\tf = f.f_back'
		return frameGetter + code

	def __createUserCodeFile(self, code, filePrefix):
		fullFilePath = filePrefix + 'CodeFile.py'
		try:
			codeFile = open(fullFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()
		return fullFilePath