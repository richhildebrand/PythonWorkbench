import re
class FileParser:
    #import re

        LOCAL_VAR_LINE_MATCHER = re.compile(r'^\{(.*)\}$')
        CURRENT_LINE_MATCHER = re.compile(r'(\d)+\s+->')
        local_vars = None
        current_line = None

    def __init__(self, filename):
        self.parse_file(filename)

    def get_local_vars(self, local_var_string):
        print local_var_string
        return local_var_string

    def get_current_line(self, current_line):
        print current_line
        return current_line

    def __parse_file(self, filename):
        try:
            infile = open(filename, 'r')
            for line in infile:
                #print line
                if self.LOCAL_VAR_LINE_MATCHER.match(line):
                    this.local_vars += line

                if self.CURRENT_LINE_MATCHER.match(line):
                    current_line = self.CURRENT_LINE_MATCHER.groups(0)
        finally:
            infile.close()
