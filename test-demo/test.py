#!/usr/bin/env python3

import os
import sys
import subprocess
import chardet

"""
测试脚本
"""

PROJ_WS_ROOT = os.path.dirname(os.path.realpath(os.path.realpath(__file__)+"../../"))
TEST_FILE = PROJ_WS_ROOT + "/test-demo/test.cpp"
CONVERT_TOOL_PATH = PROJ_WS_ROOT + "/quanlity-components/Tools/file-code-convert-script.py"

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
    if sys.platform == 'darwin':
        ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
        if ret.stdout != "":
            print(ret.stdout,end="")
        if ret.stderr != "":
            print(ret.stderr,end="")
    elif sys.platform == 'win32':
        ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if ret.stdout != "":
            print(ret.stdout)
        if ret.stderr != "":
            print(ret.stderr)

if __name__ == '__main__':
    # 编码
    print("!!!!-----------before encode convert---------------!!!!")
    content = open(TEST_FILE,'rb').read()
    result = chardet.detect(content)
    print(result)
    runcmd('python3 %s %s'%(CONVERT_TOOL_PATH,TEST_FILE))
    print("!!!!-----------after encode convert---------------!!!!")
    content = open(TEST_FILE,'rb').read()
    result = chardet.detect(content)
    print(result)
    # 格式化
    print("!!!!-----------before code format file---------------!!!!")
    runcmd('cpplint %s %s'%(CPPLINTARG.replace(" ",""),TEST_FILE))
    runcmd('clang-format -i %s'%(TEST_FILE))
    print("!!!!-----------after code format file---------------!!!!")
    runcmd('cpplint %s %s'%(CPPLINTARG.replace(" ",""),TEST_FILE))
    # Commit
    os.chdir(PROJ_WS_ROOT)
    runcmd('git add test-demo/test.cpp')
    runcmd('git commit -m "不标准提交"')
    runcmd('git commit -m "🎨 Add 标准可以通过的提交"')
    # CL
    os.chdir(PROJ_WS_ROOT)
    runcmd('gitmoji-changelog')
    
