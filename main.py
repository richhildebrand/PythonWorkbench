import sys
from UserCode import UserCodeManager

userID = 'bob'
stepNumber = 5

userCode = 'print "hello world"\nprint "line2"\n'
userCode = userCode + 'a=3\nb=4\nc = a + b\n'
userCode = userCode + 'print a\nprint b\nprint c'

userCodeManager = UserCodeManager.UserCodeManager(userID, userCode, stepNumber)
userCodeManager.executeUserCode()