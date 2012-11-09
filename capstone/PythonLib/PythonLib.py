import os

def ensureDirectoryExists(path):
    direcotryName = os.path.dirname(path)
    if not os.path.exists(direcotryName):
        os.makedirs(direcotryName)
def parseExceptionMessage(e):
	segments = str(e).split("(")
	return segments[0]

def parseExceptionLineNumber(e):
	segments = str(e).split("line ")
	lineNumber = segments[1].split(")")
	return lineNumber[0]