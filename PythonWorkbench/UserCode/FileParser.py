import re
class FileParser:
	CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
	FRAME_BEFORE_USER_CODE = "trace_dispatch"
	FRAME_AFTER_USER_CODE = "<module>"
	functions_including_their_vars = None
	frame_depth = None
	local_vars = ''
	current_line = None
	wrapper_Function_Counter = 0 #if 0 by EOF, then it is end of user code

	def __init__(self, filename):
		self.functions_including_their_vars = {}
		self.varsIncludingTheirValues = {}
		self.frame_depth = 1
		self.__parse_file(filename)
		

	def get_local_vars(self):
		return self.local_vars

	def get_current_line(self):
		#adjust for extra inserted line
		return int(self.current_line)-8

	def get_functions_including_vars(self):
		if self.__has_trace_dispatch_function(""):
			del self.functions_including_their_vars[self.FRAME_BEFORE_USER_CODE]
		if not self.__does_not_have_module_function(""):
			del self.functions_including_their_vars[self.FRAME_AFTER_USER_CODE]
		return self.functions_including_their_vars

	#parses through the file. if the wrapper function counter is equal to 0, then the file parser knows its the EOF for the code.
	def __parse_file(self, filename):
		infile = open(filename, 'r')
		self.wrapper_Function_Counter = 0
		for line in infile:
			self.__check_For_Function_Name_And_Local_Vars(line)
			self.__check_For_Current_Line_Number(line)
		infile.close()

	def __check_For_Current_Line_Number(self, line):
		contains_Line_Number = self.CURRENT_LINE_MATCHER.match(line)
		if contains_Line_Number:
			self.current_line = contains_Line_Number.group(1)

	def __check_For_Function_Name_And_Local_Vars(self, line):
		try: # startswtih doesn't precheck string length
			if line.startswith('FunctionName==='):
				function_Name = line.split('===')[1];		
				local_vars = line.split('===')[2];
				if self.__is_user_code_function(function_Name):
					framedepth = str(self.frame_depth).zfill(3) + ") "
					self.frame_depth += 1
					self.functions_including_their_vars[framedepth + function_Name] = self.__get_var_dictionary(local_vars)
		except Exception, e:
			print "\n\n__check_For_Function_Name_And_Local_Vars = " + str(e) + "\n\n"

	def __get_var_dictionary(self, local_Vars):
		local_Vars = local_Vars.replace("LocalVars:", "");
		local_Vars = local_Vars.replace("{", "");
		local_Vars = local_Vars.replace("}", "");
		local_Vars = local_Vars.replace("'", "");
		local_Vars = local_Vars.replace(" ", "");
		local_Vars = local_Vars.replace(":", "=");

		return local_Vars
	
	def __is_user_code_function(self, function_Name):
		return self.__has_trace_dispatch_function(function_Name) and self.__does_not_have_module_function(function_Name)
		
	def __has_trace_dispatch_function(self, function_Name):
		shouldAddUserFunction = self.FRAME_BEFORE_USER_CODE in self.functions_including_their_vars
		if (function_Name == self.FRAME_BEFORE_USER_CODE):
			self.functions_including_their_vars[function_Name] = "Remove Me"
		return	shouldAddUserFunction

	def __does_not_have_module_function(self, function_Name):
		if (function_Name == self.FRAME_AFTER_USER_CODE):
		 	self.functions_including_their_vars[function_Name] = "Remove Me"
		return not self.FRAME_AFTER_USER_CODE in self.functions_including_their_vars