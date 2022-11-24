#!/usr/bin/python3

import sys
import subprocess

def runcmd(command) -> int: 
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if ret.stdout != "":
        print(ret.stdout,end="")
    if ret.stderr != "":
        print(ret.stderr,end="")
    if ret.returncode == 0:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    file_filters = "-e '.h' -e '.cpp'"
    cmd1 = "TempCacheFiles=$(git diff --name-only --cached | grep %s | xargs)"%(file_filters)
    cmd2 = '''git restore --staged $(echo "$TempCacheFiles" | tr -d '"')'''
    cmd3 = '''clang-format -i $(echo "$TempCacheFiles" | tr -d '"')'''
    cmd4 = '''git add $(echo "$TempCacheFiles" | tr -d '"')'''
    runcmd(cmd1+" && "+cmd2+" && "+cmd3+" && "+cmd4)