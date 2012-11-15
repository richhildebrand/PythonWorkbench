import re
class FileParser:
	LOCAL_VAR_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
	CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
	TRACE_DISPATCH_MATCHER = re.compile(r'trace_dispatch')
	ALL_RIGHTS_MATCHER = re.compile(r'All Rights Reserved')
	MODULE_MATCHER = re.compile(r'B3G1N')
	DEFAULT_MATCHER = re.compile(r'default')
	local_vars = ''
	current_line = None
	trace_dispatch = ''

	def __init__(self, filename):
		self.__parse_file(filename)

	def get_local_vars(self):
		dirtyString1 = self.local_vars
		return dirtyString1

	def get_current_line(self):
		#adjust for extra inserted line
		return int(self.current_line)-14

	def __parse_file(self, filename):
		infile = open(filename, 'r')
		flag = None
		flag2 = None
		for line in infile:
			if self.TRACE_DISPATCH_MATCHER.match(line):
				flag = True
			elif self.ALL_RIGHTS_MATCHER.match(line):
				flag = False
			if flag == True:
				self.trace_dispatch += line
			if self.MODULE_MATCHER.match(line):
				flag2 = True
			elif self.DEFAULT_MATCHER.match(line):
				flag2 = False
			if (flag2 == True and self.LOCAL_VAR_LINE_MATCHER.match(line)):
				self.local_vars += line
			isLineToExecute = self.CURRENT_LINE_MATCHER.match(line)
			if isLineToExecute:
				 self.current_line = isLineToExecute.group(1)
		infile.close()

	def parse_for_current_frame(self):
		dirtyString2 = self.trace_dispatch
		print dirtyString2
		return dirtyString2
		
	def clean_up(self, dirtyStrings):
		cleanerString = re.sub(r'\<.*\>', '\(\)', dirtyStrings)
		cleanString = re.sub(r'\,\s+', '\\\n\\\r', cleanerString)
		return cleanString
