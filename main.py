import sys
from UserCode import UserCodeManager

userOne = 'noMethods'
simpleCode = 'a=3\nb=4\nc = a + b\nd = a + b * c'

userCodeManager = UserCodeManager.UserCodeManager(userOne, simpleCode)
print 'Simple Code Example'
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()

userTwo = 'hasMethods'
methodCode = 'tim="Tim"\ndef hello(name):\n\treturn "Hello " + name\n'
methodCode = methodCode + 'tim = hello(tim)\nseth = "Seth"\nseth= hello(seth)'

userCodeManager = UserCodeManager.UserCodeManager(userTwo, methodCode)
print "MethodCode Example"
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()
userCodeManager.executeUserCode()