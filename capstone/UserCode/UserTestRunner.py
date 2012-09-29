import TestFileBuilder

class UserTestRunner
	TestFileBuilder = None
	userTestFilePath = None

	def __init__(self, userID, methodBody, methodCalls)
		self.TestFileBuilder = TestFileBuilder.TestFileBuilder()
		self.userTestFilePath =	self.TestFileBuilder.buildFile(self.userCode, self.userID)