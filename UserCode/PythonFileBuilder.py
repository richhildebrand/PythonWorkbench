class PythonFileBuilder:
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