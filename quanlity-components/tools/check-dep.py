#!/usr/bin/python3

import os, sys

"""
Script for checking dependence
"""

def __usage():
    print("""
    Usage:

        python3 check_deps.py workspace_root_path commitlint

    """)


def __check_node_module(module_name: str, workspace_root_path: str) -> bool:
    """
    Check whether the [workspace_root_path]/node_modules/[module_name] directory exists locally
    """
    node_modules_path = os.path.join(workspace_root_path, 'node_modules')
    module_path = os.path.join(node_modules_path, module_name)
    if not os.path.exists(node_modules_path):
        return False
    if not os.path.exists(module_path):
        return False
    return True


def check_mode(workspace_root_path: str, module_name: str ) -> int:
    result = __check_node_module(module_name, workspace_root_path)
    if result:
        print("check %s suc -------- %s existed !!!"%(module_name, module_name) )
    else:
        print("Missing node module %s  -------- need download !!!"%(module_name) )
    return 0 if result else 1


def main(argv):
    if len(argv) != 2:
        __usage()
        return -1
    else:
        return check_mode(argv[0], argv[1])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))