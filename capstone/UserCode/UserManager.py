from capstone.UserCode import UserCodeManager

class UserManager:
	userCodeManager = None;

	# For multiple users
	# Will check for a current user object, and delete it before making a new one
	def createUserCodeManager(self, user, code):
		self.userCodeManager = UserCodeManager.UserCodeManager(user, code)

	# For multiple users
	# Will find the correct userCodeManage to step into
	def executeStepInUserCode(self, user):
		return self.userCodeManager.executeStepInUserCode()