class PythonFileBuilder:
	STEPS_NEED_TO_FIRST_LINE = 4

	def buildFile(self, code, filePrefix):
		code = self.__addTabToNewLines(code)
		code = self.__addWrapperFunction(code)
		code = self.__addFrameGetter(code)
		code = self.__addCallForWrapperFunction(code)
		newFilePath = self.__createUserCodeFile(code, filePrefix)
		return newFilePath

	def getPdcInstructions(self, stepNumber):
		
		#instructions = "import sys;;"
		instructions = "step;;" * (stepNumber + self.STEPS_NEED_TO_FIRST_LINE)
		instructions = instructions + "getFramesAndVars();;list"
		print instructions
		return instructions

	def __addTabToNewLines(self, code):
		return code.replace('\n', '\n\t')

	def __addWrapperFunction(self, code):
		return '\ndef WrapperFunction():\n\t' + code

	def __addCallForWrapperFunction(self, code):
		return code + "\nWrapperFunction()"

	def __addFrameGetter(self, code):
		frameGetter = 'import sys, inspect'
		frameGetter += '\ndef getFramesAndVars():'
		#frameGetter += '\n\tsys.exc_traceback'
		frameGetter += '\n\tbase = sys._getframe(0)'
		frameGetter += '\n\tf = base.f_back'
		frameGetter += '\n\tstart_flag = True'
		frameGetter += '\n\twhile f:'
		frameGetter += '\n\t\tif start_flag:'
		frameGetter += '\n\t\t\tprint "B3G1N"'
		frameGetter += '\n\t\tprint f.f_code.co_name'
		#frameGetter += '\n\t\tprint inspect.stack()[0][3]'
		#frameGetter += '\n\t\tprint "Local Vars:\\n\\t"'
		frameGetter += '\n\t\tprint f.f_locals'
		frameGetter += '\n\t\tf = f.f_back'
		frameGetter += '\n\t\tstart_flag=False'
		frameGetter += '\n\tprint "Local Vars:\\n\\t"'
		return frameGetter + code

	def __createUserCodeFile(self, code, filePrefix):
		fullFilePath = filePrefix + 'CodeFile.py'
		try:
			codeFile = open(fullFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()
		return fullFilePath