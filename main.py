import sys
from UserCode import UserCodeManager

userOne = 'noMethods'

simpleCode = 'print "line 1"\nprint "line2"\n'
simpleCode = simpleCode + 'a=3\nb=4\nc = a + b\n'
simpleCode = simpleCode + 'print a\nprint b\nprint c'

userCodeManager = UserCodeManager.UserCodeManager(userOne, simpleCode)
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()

userTwo = 'hasMethods'

methodCode = 'tim="Tim"\ndef hello(name):\n\treturn "Hello " + name\n'
methodCode = methodCode + 'tim = hello(tim)\nseth = "Seth"\nseth= hello(seth)'

userCodeManager = UserCodeManager.UserCodeManager(userTwo, methodCode)
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()