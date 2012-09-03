import sys

class CustomIOManager():
	DEFAULT_STDIN = sys.stdin
	DEFAULT_STDOUT = sys.stdout

	def cleanUpCustomIO(self):
		self.__closeCustomIO()
		self.__restoreDefaultIO()

	def setCustomIO(seslf, newInput, newOutput):
		sys.stdin = newInput
		sys.stdout = newOutput

	def __restoreDefaultIO(self):
		sys.stdin = self.DEFAULT_STDIN
		sys.stdout = self.DEFAULT_STDOUT

	def __closeCustomIO(self):
		sys.stdin.close()
		sys.stdout.close()