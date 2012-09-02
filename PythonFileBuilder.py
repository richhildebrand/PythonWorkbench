class PythonFileBuilder:
		def __init__(self, code):	
			self.code = code

		def buildFile(self):
			self.__injectPdbCode()
			self.__addTabToNewLines()
			self.__addWrapperFunction()
			self.__addImports()
			self.__addCallForWrapperFunction()
			return self.code

		def __addTabToNewLines(self):
			self.code = self.code.replace('\n', '\n\t')

		def __addImports(self):
			self.code = 'import sys\nimport pprint\nimport pdb' + self.code

		def __addWrapperFunction(self):
			self.code = '\ndef WrapperFunction():\n\t' + self.code

		def __addCallForWrapperFunction(self):
			self.code = self.code + "\nWrapperFunction()"

		def __injectPdbCode(self):
			PdbCode = ';sys.stdin = open("PdbInstructions.txt")'
			PdbCode = PdbCode + ';sys.stdout = open("bobResultFile.txt", "w+")'
			PdbCode = PdbCode + ';pdb.set_trace()'
			self.code = self.code.replace('replaceMeWithPdbCode', PdbCode)