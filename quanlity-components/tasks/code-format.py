#!/usr/bin/python3

import os
import sys
import subprocess

def __usage():
    print("""
    Usage:
    
    python3 code-format.py mode[1:git diff增量, 2:文件增量]
    
    """)

def runcmd(command) -> int: 
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if ret.stdout != "":
        print(ret.stdout,end="")
    if ret.stderr != "":
        print(ret.stderr,end="")
        sys.exit(-1)

def determine_suffix(file):
    suffix = os.path.splitext(file)[-1]
    # print(suffix, type(suffix))
    if  suffix== (".c") or suffix == (".h") or suffix == (".c++") or suffix == (".h++") or suffix == (".cc") or suffix == (".cpp"):
        return True
    else:
        return False

def getcachesfilelist() -> list:
    sh = True
    if sys.platform == 'darwin':
        sh = True
    elif sys.platform == 'win32':
        sh = False
    ret = subprocess.run("git diff --name-only --cached",shell=sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    return ret.stdout.split("\n")

def main(argv):
    if len(argv) != 1:
        __usage()
        sys.exit(-1)
    else:
        list = getcachesfilelist()
        for file in list:
            if determine_suffix(file):
                mode = argv[0]
                if mode == "1":
                    runcmd("git restore --staged %s"%(file))
                    runcmd("git add  %s"%(file))
                    runcmd("git clang-format %s"%(file))
                    runcmd("git add  %s"%(file))  
                elif mode == "2":
                    runcmd("git restore --staged %s"%(file))
                    runcmd("clang-format -i  %s"%(file))
                    runcmd("git add  %s"%(file))
            else:
                pass
        sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])

