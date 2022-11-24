#!/usr/bin/python3

import os
import sys
import subprocess

def runcmd(command) -> int: 
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if ret.stdout != "":
        print(ret.stdout,end="")
    if ret.stderr != "":
        print(ret.stderr,end="")

def determine_suffix(file):
    suffix = os.path.splitext(file)[-1]
    # print(suffix, type(suffix))
    if  suffix== (".c") or suffix == (".h") or suffix == (".c++") or suffix == (".h++") or suffix == (".cc") or suffix == (".cpp"):
        return True
    else:
        return False

if __name__ == '__main__':
    cmd_getcached = '''git diff --name-only --cached | tr -d '"' | xargs '''
    ret = subprocess.run(cmd_getcached,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if ret.returncode == 0:
        if ret.stdout != "":
            list = ret.stdout.replace("\n","").split(" ")
            for file in list:
                if determine_suffix(file):
                    runcmd("git restore --staged %s"%(file))
                    runcmd("clang-format -i  %s"%(file))
                    runcmd("git add  %s"%(file))
                else:
                    pass
            sys.exit(0)
        else:
            sys.exit(0)
    else:
        print(ret.stdout,ret.stderr)
        sys.exit(-1)