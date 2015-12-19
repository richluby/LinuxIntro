#!/usr/bin/python

import sys

#the number of characters per ToC line
LEN_LINE = 90 
#the number of chars reserved for line numbers in the ToC
NUM_CHARS = 4
# continuation character
CONT_CHAR = "."

if "darwin" in sys.platform:
	from Foundation import *
	from AppKit import *

if (len(sys.argv) < 2):
	print "usage: buildMDToc.py <file name>"
	exit(1)


# set clipboard contents
def setClipboard(contents):
	if "darwin" in sys.platform:
		board = NSPasteboard.generalPasteboard()
		board.declareTypes_owner_([NSStringPboardType], None)
		casted = NSString.stringWithString_(str(contents))
		newData = casted.nsstring().dataUsingEncoding_(NSASCIIStringEncoding)
		board.setData_forType_(newData, NSStringPboardType)

def appendLocation(line, lineNum):
	numDots = LEN_LINE - (len(line) + len(str(lineNum)))
	#for i in xrange(0, numDots):
	#	line += CONT_CHAR
	return line + "".join(["." for i in xrange(0, numDots)]) +  str(lineNum)

if __name__ == "__main__":
	if (len(sys.argv) < 1):
		print "usage: buildMDToC <path to MD file>"
		exit(1)
	tocLine = ""
	lastIndex = -1
	i = 1
	tocBuffer = []
	f = open(sys.argv[1])
	lines = f.readlines()
	line = ""
	tocCounter = 1 # i keeps track of the current line number
	for i in xrange(0, len(lines)):
		line = lines[i]
		if line[0] == "#":
			lastIndex = 0
			for j in xrange(0, len(line)):
				if (line[j] != "#"):
					lastIndex = j
					break
			tocLine = line[lastIndex+1:].strip()
			tocLine = "\t"*(lastIndex-1) + "[" + tocLine + "](#" + tocLine.lower().replace(" ", "-") + ")"
			tocBuffer.append(appendLocation(tocLine, i) + "  \n")
			tocCounter += 1
			lastIndex = -1
	tocBuffer = ''.join(tocBuffer)
	if "darwin" in sys.platform:
		setClipboard(tocBuffer)
		print "\nTOC copied to system clipboard.\n" 
	else :
		print str(tocBuffer)
