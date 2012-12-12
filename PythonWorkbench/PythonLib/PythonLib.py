import os

def ensureDirectoryExists(path):
    direcotryName = os.path.dirname(path)
    if not os.path.exists(direcotryName):
        os.makedirs(direcotryName)
def parseExceptionMessage(e):
	try:
		segments = str(e).split("(")
		return segments[0]
	except:
		return str(e)

def parseExceptionLineNumber(e):
	try:
		segments = str(e).split("line ")
		lineNumber = segments[1].split(")")
		return int(lineNumber[0])
	except:
		return -1

def startsWith(doesMyString, thisString):
	try: 
		return doesMyString.startswith(thisString)
	except:
		return False