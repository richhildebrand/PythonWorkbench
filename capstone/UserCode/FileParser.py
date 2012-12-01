﻿import re
class FileParser:
	CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
	FRAME_BEFORE_USER_CODE = "trace_dispatch"
	FRAME_AFTER_USER_CODE = "<module>"
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
		return int(self.current_line)-8

	def get_functions_including_vars(self):
		del self.functions_including_their_vars[self.FRAME_BEFORE_USER_CODE]
		del self.functions_including_their_vars[self.FRAME_AFTER_USER_CODE]
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
				if self.__is_user_code_function(function_Name):
					self.functions_including_their_vars[function_Name] = self.__get_var_dictionary(local_vars)
		except Exception, e:
			print e

	def __get_var_dictionary(self, local_Vars):
		#TODO: This will work similar to building the function dictionary
		#created inside  __check_For_Function_Name_And_Local_Vars
		return local_Vars

	def __is_user_code_function(self, function_Name):
		return self.__has_trace_dispatch_function(function_Name) and self.__does_not_have_module_function()
		
	def __has_trace_dispatch_function(self, function_Name):
		return function_Name == self.FRAME_BEFORE_USER_CODE or	self.FRAME_BEFORE_USER_CODE in self.functions_including_their_vars

	def __does_not_have_module_function(self):
		return not self.FRAME_AFTER_USER_CODE in self.functions_including_their_vars