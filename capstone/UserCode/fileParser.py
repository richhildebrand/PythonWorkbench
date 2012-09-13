#!/usr/bin/env
import re

def parser(fileName):
    directory = "../../UserFiles/"
    infile = open(directory+fileName, 'r')
    code_line = re.compile(r'(\d)(.*)')
    call_line = re.compile(r'(^--Call--)')
    return_line = re.compile(r'(^--Return--)')

    #line_number = re.compile('^ \d')
    lines_hash = {}
    line_counter = 0
    for line in infile:
        print line_counter
        #for code_line in (1..100):
        ##if code_line.match(line):
        #code_line = re.compile("  (\d)(*)")
        #cod = re.match("([^ \d].*)", line)
        if code_line.match(line):
               # lines_hash[
                print("line number")
                print(code_line.group(0))
                print("Code: ")
                print(code_line.group(1))
        if call_line.match(line):
          print "matched call line: "
          print line
        if return_line.match(line):
          print "matched return line: "
          print line
        line_counter = line_counter + 1

def main():
	parser('hasMethodsResultFile.txt')
if __name__ == "__main__": main()
