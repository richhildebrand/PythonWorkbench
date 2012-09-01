import UserCodeManager


injectPDB = '\nsys.stdin = open("PdbInstructions.txt")'
injectPDB = injectPDB + '\nsys.stdout = open("bobResultFile.txt", "w+")'
injectPDB = injectPDB + '\npdb.set_trace()'

userCodeImports = '\nimport sys\nimport pprint\nimport pdb'
defineUserCodeWrapper = '\ndef userCodeWrapper():'
callUserCodeWrapper = '\nuserCodeWrapper()'

userID = 'bob'


userCode = '\nprint "hello world"\nprint "line2"'
userCode = userCode + '\na=3\nb=4\nc = a + b'
userCode = userCode + injectPDB
userCode = userCode + '\nprint a\nprint b\nprint c'
#because python, thats why.
userCode = userCode.replace('\n', '\n\t')

fullFile = userCodeImports + defineUserCodeWrapper + userCode + callUserCodeWrapper

userCodeManager = UserCodeManager.UserCodeManager(userID, fullFile)
userCodeManager.executeUserCode()