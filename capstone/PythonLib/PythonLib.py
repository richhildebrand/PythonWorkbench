import os

def ensureDirectoryExists(path):
    direcotryName = os.path.dirname(path)
    if not os.path.exists(direcotryName):
        os.makedirs(direcotryName)