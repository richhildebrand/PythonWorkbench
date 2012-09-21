import re
class FileParser:
    LOCAL_VAR_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
    CURRENT_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
    local_vars = ''
    current_line = None

    def __init__(self, filename):
        self.__parse_file(filename)

    def get_local_vars(self):
        print self.local_vars
        return self.local_vars

    def get_current_line(self):
        print self.current_line
        return self.current_line

    def __parse_file(self, filename):
        try:
            infile = open(filename, 'r')
            for line in infile:
                #print line
                if self.LOCAL_VAR_LINE_MATCHER.match(line):
                    self.local_vars += line
                
                isLineToExecute = self.CURRENT_LINE_MATCHER.match(line)
                if isLineToExecute:
                     print "found current line"
                     self.current_line = isLineToExecute.group()
        finally:
            infile.close()
