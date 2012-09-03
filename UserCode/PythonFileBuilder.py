class PythonFileBuilder:
	LINES_ADDED_WHEN_BUILDING_FILE = 5

	def __init__(self, code):	
		self.code = code

	def buildFile(self):
		self.__addTabToNewLines()
		self.__addWrapperFunction()
		self.__addCallForWrapperFunction()
		return self.code

	def __addTabToNewLines(self):
		self.code = self.code.replace('\n', '\n\t')

	def __addWrapperFunction(self):
		self.code = 'def WrapperFunction():\n\t' + self.code

	def __addCallForWrapperFunction(self):
		self.code = self.code + "\nWrapperFunction()"
	
	def getPdcInstructions(self, stepNumber):
		instructions = "step;;" * (stepNumber + self.LINES_ADDED_WHEN_BUILDING_FILE)
		instructions = instructions + "locals()"
		return instructions