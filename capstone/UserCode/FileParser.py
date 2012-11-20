import re
class FileParser:
	LOCAL_VAR_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
	CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
	TRACE_DISPATCH_MATCHER = re.compile(r'trace_dispatch')
	ALL_RIGHTS_MATCHER = re.compile(r'All Rights Reserved')
	#Unique char sequence that marks begining of stack output
	BEGIN_MATCHER = re.compile(r'B3G1N')
	DEFAULT_MATCHER = re.compile(r'default')
	local_vars = ''
	current_line = None
	trace_dispatch = ''

	def __init__(self, filename):
		self.__parse_file(filename)

	def get_local_vars(self):
		local_var_string = self.local_vars
		return local_var_string

	def get_current_line(self):
		#adjust for extra inserted line
		return int(self.current_line)-13

	def __parse_file(self, filename):
		infile = open(filename, 'r')
		user_code_line_flag = None #flag set when "trace_dispatch" is matched
		flag2 = None
		for line in infile:
			if self.TRACE_DISPATCH_MATCHER.match(line):
				user_code_line_flag = True
			elif self.ALL_RIGHTS_MATCHER.match(line):
				user_code_line_flag = False
			if user_code_line_flag == True:
				self.trace_dispatch += line
			if self.BEGIN_MATCHER.match(line):
				flag2 = True
			elif self.DEFAULT_MATCHER.match(line):
				flag2 = False
			if (flag2 == True and self.LOCAL_VAR_LINE_MATCHER.match(line)):
				self.local_vars += line
			is_line_to_execute = self.CURRENT_LINE_MATCHER.match(line)
			if is_line_to_execute:
				 self.current_line = is_line_to_execute.group(1)
		infile.close()

	def parse_for_current_frame(self):
		frame_string = self.trace_dispatch
		#json_frame_dict = build_json(frame_string)
		return frame_string
		
	def clean_up(self, dirtyStrings):
		cleanerString = re.sub(r'\<.*\>', '\(\)', dirtyStrings)
		cleanString = re.sub(r'\,\s+', '\\\n\\\r', cleanerString)
		return cleanString
	
	#def build_json(self, frame_string):
		
		
