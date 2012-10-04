from capstone.UserCode import UserCodeManager

class UserManager:
	userCodeManagers = None;

	def __init__(self):
		self.userCodeManagers = {}

	def createUserCodeManager(self, user, userCode, unitTests):
			self.userCodeManagers[user] = UserCodeManager.UserCodeManager(user, userCode, unitTests)

	def executeStepInUserCode(self, user):
		return self.userCodeManagers[user].executeStepInUserCode()

	def runTestsOnUserCode(self, user):
		return self.userCodeManagers[user].runTestsOnUserCode()