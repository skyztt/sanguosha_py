import os

import sys


class ProGenerator(object):
    def __init__(self):
        super().__init__()
        self.pyFiles = list()
        self.uiFiles = list()
        proDir = sys.path[0]
        proDirName = os.path.basename(proDir)
        
        self.proFile = proDir + "/" + proDirName + ".pro"        
        self.tsFile = os.path.relpath(proDir + "/" + proDirName + ".ts")
        print(self.proFile)
        
    def addFiles(self, files):
        for file in files:
            relPath = os.path.relpath(file)
            if relPath.endswith(".py") or relPath.endswith(".pyw"):
                self.pyFiles.append(relPath)
            elif relPath.endswith(".ui"):
                self.uiFiles.append(relPath)
                
    def outWithTarget(fileOut, strTarget, files):
        if len(files) != 0:
            fileOut.write(strTarget)
            bFirst = True
            for file in files:
                if not bFirst:
                    fileOut.write("\\\n" + " " * len(strTarget))
                fileOut.write(file)
                bFirst = False
            fileOut.write("\n")
        
    def outFile(self):
        with open(self.proFile, 'w') as f:
            ProGenerator.outWithTarget(f, "FORMS = ", self.uiFiles)
            ProGenerator.outWithTarget(f, "SOURCES = ", self.pyFiles)           
            ProGenerator.outWithTarget(f, "TRANSLATIONS = ", [self.tsFile])


def addDir(dirPath, proFileGenerator):
    for parent, dirnames, filenames in os.walk(dirPath):   
        bInIgnoreDir = False
        for ignoreDir in ignoreDirs:
            if parent.__contains__(ignoreDir):
                bInIgnoreDir = True
                break
        if not bInIgnoreDir:
            proFileGenerator.addFiles([parent + "/" + filename for filename in filenames])            

if __name__ == "__main__":
    #os.chdir(os.path.dirname(__file__)) # 当前把生成工具放在工程根目录
    # rootDir = os.path.dirname(__file__)
    os.chdir(sys.path[0])
    rootDir = sys.path[0]
    
    ignoreRootDirs = set((".idea", "font", "resource", os.path.basename(__file__)))
    ignoreDirs = (".idea", "__pycache__")
    
    proFileGenerator = ProGenerator()
    
    rootLevelFiles = os.listdir(rootDir)
    for file in rootLevelFiles:
        if not ignoreRootDirs.__contains__(file):
            filePath = rootDir + "/" + file
            if os.path.isdir(filePath):
                addDir(filePath, proFileGenerator)
            else:
                proFileGenerator.addFiles([filePath])
                
    proFileGenerator.outFile()
    
