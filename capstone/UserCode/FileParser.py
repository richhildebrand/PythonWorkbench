import re
class FileParser:
	CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
	functions_including_their_vars = None
	local_vars = ''
	current_line = None

	def __init__(self, filename):
		self.functions_including_their_vars = {}
		self.__parse_file(filename)

	def get_local_vars(self):
		return self.local_vars

	def get_current_line(self):
		#adjust for extra inserted line
		return int(self.current_line)-13

	def get_functions_including_vars(self):
		print "Number of functions=" + str(len(self.functions_including_their_vars))
		return self.functions_including_their_vars

	def __parse_file(self, filename):
		print "\n\nSTART __parse_file"
		infile = open(filename, 'r')
		for line in infile:
			self.__check_For_Function_Name_And_Local_Vars(line)
			self.__check_For_Current_Line_Number(line)
		infile.close()
		print "\n\nEND __parse_file"

	def __check_For_Current_Line_Number(self, line):
		contains_Line_Number = self.CURRENT_LINE_MATCHER.match(line)
		if contains_Line_Number:
			self.current_line = contains_Line_Number.group(1)

	def __check_For_Function_Name_And_Local_Vars(self, line):
		try: # startswtih doesn't precheck string length
			if line.startswith('FunctionName='):
				segments = line.split('===')
				function_Name = segments[1];
				local_vars = segments[2];
				print "\n\nFunction Name= " + function_Name
				print "LocalVars= " + local_vars
				self.functions_including_their_vars[function_Name] = local_vars
				print "Number of functions=" + str(len(self.functions_including_their_vars))
		except Exception, e:
			catchException = e