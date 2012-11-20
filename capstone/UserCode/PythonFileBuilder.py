class PythonFileBuilder:
	STEPS_NEED_TO_FIRST_LINE = 5

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
		return '\ndef WrapperFunction():\n\t' + code

	def __addCallForWrapperFunction(self, code):
		return code + "\nWrapperFunction()"

	def __addFrameGetter(self, code):
		frameGetter = 'import sys, inspect'
		frameGetter += '\ndef getFramesAndVars():'
		frameGetter += '\n\tbase = sys._getframe(0)'
		frameGetter += '\n\tf = base.f_back'
		frameGetter += '\n\tstart_flag = True'
		frameGetter += '\n\twhile f.f_back:'
		frameGetter += '\n\t\tif start_flag:'
		frameGetter += '\n\t\t\tprint "B3G1N"'
		frameGetter += '\n\t\tstart_flag=False'
		#frameGetter += '\n\t\tprint f.f_lineno'
		frameGetter += '\n\t\tif((f.f_lineno>=1 and f.f_lineno<49) and ((str(f.f_code.co_name) != "<module>") and (str(f.f_code.co_name) != "executeStepInUserCode") and (str(f.f_code.co_name) != "takeStep"))):'
		frameGetter += '\n\t\t\tprint "\\n{function: " + str(f.f_code.co_name) + ", locals: " + str(f.f_locals) + "}"'
		frameGetter += '\n\t\tf = f.f_back'
		#frameGetter += '\n\tprint "Local Vars:\\n\\t"'
		return frameGetter + code

	def __createUserCodeFile(self, code, filePrefix):
		fullFilePath = filePrefix + 'CodeFile.py'
		try:
			codeFile = open(fullFilePath, 'w+')
			codeFile.write(code)
		finally:
			codeFile.close()
		return fullFilePath