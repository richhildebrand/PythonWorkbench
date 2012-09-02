import UserCodeManager

userID = 'bob'

userCode = 'print "hello world"\nprint "line2"\n'
userCode = userCode + 'a=3\nb=4\nc = a + b\n'
userCode = userCode + 'print a\nprint b\nprint c'

userCodeManager = UserCodeManager.UserCodeManager(userID, userCode)
userCodeManager.executeUserCode()