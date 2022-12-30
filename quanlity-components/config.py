#!/usr/bin/python3

"""
功能配置
"""

import os
import sys
import shutil

config = {
    "pre-commit-tasks-group":
    {
        "pre_msg" : "echo !!!!!----pre-commit----!!!!",
        "trans_coding" : 
        {
            "enable": True, #是否开启文件自动转码
            "cmd": "python3 ./quanlity-components/tasks/code-convert.py ./quanlity-components"
        },
        "code_format" : 
        {
            "enable" : True, # #是否开启代码格式化
            "mode" : "1",      # 1:git diff增量,2:文件增量
            "cmd" : "python3 ./quanlity-components/tasks/code-format.py"
        },
        "code_static_check" : 
        {
            "enable" : True, #是否开启代码静态检测
            "cmd" : "python3 ./quanlity-components/tasks/code-static-check.py"
        }
    },

    "commit-msg-tasks-group":
    {    
        "commit_message_check" : 
        {
            "enable" : True, #是否开启git提交信息检测
            "cmd" : "npx --no -- commitlint --edit",
        }
    },

    "post-commit-tasks-group":
    {
        "changelog_update" : 
        {
            "enable" : True, #是否开启changlog自动生成
            "cmd" : "python3 ./quanlity-components/tasks/update-changelog.py ./"
        }
    }
}

line_feed = "\n"
if sys.platform == 'darwin':
    pass
elif sys.platform == 'win32':
    # line_feed = "\n\r"
    pass

def remove_task(hook_file, hook_content):
    with open(hook_file) as f, open(hook_file+"output_", "w") as f_out:
        for l in f:
            if hook_content not in l.strip():
                f_out.write(l)
    shutil.copymode(hook_file, hook_file+"output_")
    os.remove(hook_file)
    os.rename(hook_file+"output_", hook_file)

def task_existed(hook_file, hook_content) -> bool :
    exist = False
    with open(hook_file) as f:
        for l in f:
            if hook_content in l.strip():
                exist = True
    return exist

def add_independent_task(hook_file, hook_content):
    '''
    独立不耦合的任务默认添加在文件尾
    '''
    if not task_existed(hook_file, hook_content):
        with open(hook_file) as f, open(hook_file+"output_", "w") as f_out:
            for l in f:
                f_out.write(l)
            else:
                f_out.write(hook_content)
                f_out.write(line_feed)
        shutil.copymode(hook_file, hook_file+"output_")
        os.remove(hook_file)
        os.rename(hook_file+"output_", hook_file)

def add_pre_commit_task(hook_file, hook_content):
    '''
    有时序关系的任务按时序
    默认时序从前到后 转码->格式化->静态检测。
    '''
    if hook_content == config["pre-commit-tasks-group"]["code_format"]["cmd"]:
        remove_task(hook_file, hook_content)
        mode = " " + config["pre-commit-tasks-group"]["code_format"]["mode"]
        if not task_existed(hook_file, config["pre-commit-tasks-group"]["code_static_check"]["cmd"]):
            add_independent_task(hook_file, hook_content+mode)
        else :
            with open(hook_file) as f, open(hook_file+"output_", "w") as f_out:
                task_list = f.readlines()
                task_list.insert(task_list.index(config["pre-commit-tasks-group"]["code_static_check"]["cmd"]+line_feed), hook_content+mode+line_feed)
                for i in task_list:
                    f_out.write(i)
            shutil.copymode(hook_file, hook_file+"output_")
            os.remove(hook_file)
            os.rename(hook_file+"output_", hook_file)
    else :
        if not task_existed(hook_file, hook_content):
            if hook_content == config["pre-commit-tasks-group"]["code_static_check"]["cmd"]:
                add_independent_task(hook_file, hook_content)
            elif hook_content == config["pre-commit-tasks-group"]["trans_coding"]["cmd"]:
                with open(hook_file) as f, open(hook_file+"output_", "w") as f_out:
                    task_list = f.readlines()
                    task_list.insert(task_list.index(config["pre-commit-tasks-group"]["pre_msg"]+line_feed)+1, hook_content+line_feed)
                    for i in task_list:
                        f_out.write(i)
                shutil.copymode(hook_file, hook_file+"output_")
                os.remove(hook_file)
                os.rename(hook_file+"output_", hook_file)

if __name__ == '__main__':
    #pre-commit-tasks-group
    if not config["pre-commit-tasks-group"]["trans_coding"]["enable"]:
        remove_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["trans_coding"]["cmd"])
        print("**unenable!** trans_coding")
    else :
        add_pre_commit_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["trans_coding"]["cmd"])
        print("**enable!**   trans_coding")
    
    if not config["pre-commit-tasks-group"]["code_format"]["enable"]:
        remove_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["code_format"]["cmd"])
        print("**unenable!** code_format")
    else :
        add_pre_commit_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["code_format"]["cmd"] )
        print("**enable!**   code_format")

    if not config["pre-commit-tasks-group"]["code_static_check"]["enable"]:
        remove_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["code_static_check"]["cmd"])
        print("**unenable!** code_static_check")
    else :
        add_pre_commit_task("./.husky/pre-commit", config["pre-commit-tasks-group"]["code_static_check"]["cmd"])
        print("**enable!**   code_static_check")

    #commit-msg-tasks-group
    if not config["commit-msg-tasks-group"]["commit_message_check"]["enable"]:
        remove_task("./.husky/commit-msg", config["commit-msg-tasks-group"]["commit_message_check"]["cmd"])
        print("**unenable!** commit_message_check")
    else :
        add_independent_task("./.husky/commit-msg", config["commit-msg-tasks-group"]["commit_message_check"]["cmd"])
        print("**enable!**   commit_message_check")

    #post-commit-tasks-group
    if not config["post-commit-tasks-group"]["changelog_update"]["enable"]:
        remove_task("./.husky/post-commit", config["post-commit-tasks-group"]["changelog_update"]["cmd"])
        print("**unenable!** changelog_update")
    else :
        add_independent_task("./.husky/post-commit", config["post-commit-tasks-group"]["changelog_update"]["cmd"])
        print("**enable!**   changelog_update")
    