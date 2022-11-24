#!/usr/bin/python3

import sys
import subprocess

CPPLINTARG = "--filter=-legal/copyright,\
                        -whitespace/line_length,\
                        -build/include_what_you_use,\
                        -build/include,\
                        -whitespace/blank_line,-whitespace/ending_newline,\
                        -build/header_guard,-readability/streams,\
                        -whitespace/parens,-whitespace/operators,\
                        -build/storage_class,\
                        -whitespace/labels,\
                        -build/c++11"

def runcmd(command) -> int: 
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if ret.returncode == 0:
        sys.exit(0)
    else:
        print(ret.stdout,ret.stderr)
        sys.exit(1)

if __name__ == '__main__':
    file_filters = "-e '.h' -e '.cpp'"
    runcmd("cpplint %s $(git diff --name-only --cached | grep %s | xargs)"%(CPPLINTARG.replace(" ",""), file_filters))