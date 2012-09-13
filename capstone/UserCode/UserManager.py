from capstone.UserCode import UserCodeManager

class UserManager:
	userCodeManagers = None;

	def __init__(self):
		self.userCodeManagers = {}

	def createUserCodeManager(self, user, code):
			self.userCodeManagers[user] = UserCodeManager.UserCodeManager(user, code)

	def executeStepInUserCode(self, user):
		return self.userCodeManagers[user].executeStepInUserCode()