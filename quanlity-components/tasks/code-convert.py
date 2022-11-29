#!/usr/bin/python3

import sys
import subprocess

def __usage():
    print("""
    Usage:

        python3 code-convert.py workspace_root_path

    """)

def runcmd(command) -> int: 
    if sys.platform == 'darwin':
        ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
        if ret.stdout != "":
            print(ret.stdout,end="")
        if ret.stderr != "":
            print(ret.stderr,end="")
        if ret.returncode == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    elif sys.platform == 'win32':
        ret = subprocess.run(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if ret.stdout != "":
            print(ret.stdout)
        if ret.stderr != "":
            print(ret.stderr)
        if ret.returncode == 0:
            sys.exit(0)
        else:
            sys.exit(1)

def getcachesfilestr() -> str:
    sh = True
    if sys.platform == 'darwin':
        sh = True
    elif sys.platform == 'win32':
        sh = False
    ret = subprocess.run("git diff --name-only --cached",shell=sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    str = ''
    for x in ret.stdout.split("\n"):
        str = str + " " + x
    return str
    
def main(argv):
    if len(argv) != 1:
        __usage()
        return -1
    else:
        path = argv[0] + "/Tools/file-code-convert-script.py"
        str = getcachesfilestr()
        runcmd('python3 %s %s'%(path,str))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

