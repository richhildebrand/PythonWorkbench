import os

def ensureDirectory(path):
    direcotryName = os.path.dirname(path)
    if not os.path.exists(direcotryName):
        os.makedirs(direcotryName)