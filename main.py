import UserCodeManager

replaceMeWithPdbCode = 'replaceMeWithPdbCode'

userID = 'bob'

userCode = 'print "hello world"\nprint "line2"'
userCode = userCode + '\na=3\nb=4\nc = a + b'
userCode = userCode + replaceMeWithPdbCode 
userCode = userCode + '\nprint a\nprint b\nprint c'

userCodeManager = UserCodeManager.UserCodeManager(userID, userCode)
userCodeManager.executeUserCode()