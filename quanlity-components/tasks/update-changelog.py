#!/usr/bin/python3

import os
import sys
import subprocess

def __usage():
    print("""
    Usage:

        python3 update-changelog.py workspace_root_path

    """)

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

def main(argv):
    if len(argv) != 1:
        __usage()
        return -1
    else:
        os.chdir(argv[0])
        runcmd('gitmoji-changelog')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))