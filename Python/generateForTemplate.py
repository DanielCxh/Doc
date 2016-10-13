#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import threading

#--------------------------------------------#
class GenerateThread (threading.Thread):
	def __init__(self, threadID, name, dirPath):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.dirPath = dirPath

	def run(self):
		pass
#--------------------------------------------#

#--------------------------------------------#
def checkSysArg():
	if ( len(sys.argv) <= 1 ):
		print("Warning : Please entry the mode name!")
	elif ( sys.argv[1] == '-h' or sys.argv[1]  == '-help' or sys.argv[1]  == '--help'):
		showHelpDoc()
	elif ( sys.argv[1]  == '-e' ):
		showExample()
	elif ( sys.argv[1]  == '-g' ):
		if ( len(sys.argv) <= 2 ):
			print("Warning : Please entry the mode name!")
			pass
		else:
			global g_modeName
			g_modeName = sys.argv[2]
			doScriptAction()
	else:
		print("Invalid command, please use '-h' to show help doc")
#--------------------------------------------#

#--------------------------------------------#
# Show help document
#--------------------------------------------#
def showHelpDoc():
	print("#-----------------HELP DOC--------------------#")
	print("# Please put this file to root directory      #")
	print("# All the templete file show be writable      #")
	print("# -h : Show help doc                          #")
	print("# -e : Show an example                        #")
	print("# -g : Generate                               #")
	print("#---------------------------------------------#")
#--------------------------------------------#

#--------------------------------------------#
# Show example
#--------------------------------------------#
def showExample():
	print("eg:\n")
	print("python %s -g ModeName" %(__file__))
#--------------------------------------------#

#--------------------------------------------#
# Get ll the files that below to the directory
#--------------------------------------------#
def getAllFiles(path):
	allFilePath = []
	for root, dirs, files in os.walk(path):
	    #print("Root = ", root, "dirs = ", dirs, "files = ", files)
	    for f in files:
	    	#print(os.path.join(root, f))
	    	allFilePath.append(os.path.join(root, f))
	return allFilePath
#--------------------------------------------#

#--------------------------------------------#
# This method used to generate file form templete
# Will modify the templete files directry
#--------------------------------------------#
def generateFiles(path, filePaths, replaceName):
	tmpFileInfo = []

	for filePath in filePaths:
		if FILE_TYPE_PY in filePath:
			continue
		elif FILE_TYPE_CPP in filePath:
			pass
		elif FILE_TYPE_H in filePath:
			pass
		else:
			continue

		#filePath = os.path.join(path, oneFile)
		f = open(filePath, 'r')

		for line in f.readlines():
			tmpLine = line
			tmpFileInfo.append(tmpLine.replace(DEFAULT_STR_Xxx, replaceName.capitalize()).replace(DEFAULT_STR_XXX, replaceName.upper()))
		
		f.close()

		f = open(filePath, 'w')

		for line in tmpFileInfo:
			f.write(line)

		f.close()

		# Rename file #
		oldFullFilePath = filePath
		newFullFilePath = filePath.replace(DEFAULT_STR_Xxx, replaceName.capitalize())
		if ( oldFullFilePath == newFullFilePath ):
			print("%s --> PASS" % oldFullFilePath)
			pass
		else:
			os.rename(oldFullFilePath, newFullFilePath)
			print("%s --> %s" %(oldFullFilePath, newFullFilePath))
		
		# Clear temp info #
		tmpFileInfo = []
	print("Generate completed!")
#--------------------------------------------#

#--------------------------------------------#
def doScriptAction():
	currentPath = os.getcwd()
	g_allFiles = getAllFiles(currentPath)
	generateFiles(currentPath, g_allFiles, g_modeName)
#--------------------------------------------#



DEFAULT_STR_XXX = 'XXX'
DEFAULT_STR_Xxx = 'Xxx'
FILE_TYPE_PY = '.py'
FILE_TYPE_H = '.h'
FILE_TYPE_CPP = '.cpp'

g_modeName = ''
g_allFiles = []

checkSysArg()