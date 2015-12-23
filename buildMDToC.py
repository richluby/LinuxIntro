#!/usr/bin/python

import sys, argparse

if "darwin" in sys.platform:
	from Foundation import *
	from AppKit import *

# set clipboard contents
def setClipboard(contents):
	if "darwin" in sys.platform:
		board = NSPasteboard.generalPasteboard()
		board.declareTypes_owner_([NSStringPboardType], None)
		casted = NSString.stringWithString_(str(contents))
		newData = casted.nsstring().dataUsingEncoding_(NSASCIIStringEncoding)
		board.setData_forType_(newData, NSStringPboardType)

def appendLocation(line, lineNum, numTabs):
	numDots = LEN_LINE - (len(line) + len(str(lineNum)) + (numTabs*TAB_WIDTH))
	#for i in xrange(0, numDots):
	#	line += CONT_CHAR
	return line + "".join([CONT_CHAR for i in xrange(0, numDots)]) +  str(lineNum)

if __name__ == "__main__":
	# continuation character
	global CONT_CHAR
	#the number of characters per ToC line
	global LEN_LINE
	# boolean to determine if the continuation character should be printed
	global PRINT_CONT_CHAR
	# the width of the tab character
	global TAB_WIDTH
	parser = argparse.ArgumentParser(description="Builds a ToC for a Markdown file based on the headers.")
	parser.add_argument("-c", help="defines the character to use between the heading and the line number", default=".")
	parser.add_argument("-w", help="the max width of the ToC", default=90, type=int)
	parser.add_argument("-p", help="force printing the ToC to stdout", default=False, action="store_true")
	parser.add_argument("-t", help="the width of a tab", type=int, default=4)
	parser.add_argument("--no-continuation", help="creates only linked headings, without line numbers or continuation characters", default=False, action="store_true")
	parser.add_argument("fileName", help="the name of the Markdown file for which to create a ToC")
	args = dict()
	if (len(sys.argv) < 2): # argv[0] is program name, and does not count
		parser.parse_args(["-h"])
	else:
		args = parser.parse_args()
		CONT_CHAR = args.c
		LEN_LINE = args.w
		PRINT_CONT_CHAR = args.p
		TAB_WIDTH = args.t
		PRINT_CONT_CHAR = not args.no_continuation
	tocLine = ""
	lastIndex = -1
	i = 1
	tocBuffer = []
	f = open(args.fileName)
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
			tocBuffer.append(appendLocation(tocLine, i, lastIndex-1) + "  \n" if PRINT_CONT_CHAR else tocLine + "  \n")
			tocCounter += 1
			lastIndex = -1
	tocBuffer = ''.join(tocBuffer)
	if not (args.p) and "darwin" in sys.platform:
		setClipboard(tocBuffer)
		print "\nTOC copied to system clipboard.\n" 
	else :
		print str(tocBuffer)
