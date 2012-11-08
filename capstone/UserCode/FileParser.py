import re
class FileParser:
    LOCAL_VAR_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
    CURRENT_LINE_MATCHER = re.compile(r'^\s+(\d+)\s+->.*$')
    local_vars = ''
    current_line = None

    def __init__(self, filename):
        self.__parse_file(filename)

    def get_local_vars(self):
        return self.local_vars

    def get_current_line(self):
        #adjust for extra inserted line
        return int(self.current_line)-1

    def __parse_file(self, filename):
        try:
            infile = open(filename, 'r')
            for line in infile:
                #print line
                if self.LOCAL_VAR_LINE_MATCHER.match(line):
                    self.local_vars += line
                
                isLineToExecute = self.CURRENT_LINE_MATCHER.match(line)
                if isLineToExecute:
                     #print "found current line"
                     self.current_line = isLineToExecute.group(1)
        finally:
            infile.close()
