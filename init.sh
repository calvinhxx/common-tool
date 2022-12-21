#!/bin/bash

# !!!!!!!! run this script by root !!!!!!!!

ComponentsPath="./quanlity-components"

###### init dependences ######
#---------init npm package dependences---------#
# create npm package manage
npm init -y

# init husky
python3 $ComponentsPath/Tools/check-dep.py ./ husky
if [ $? == 1 ]
then
    npm install --save-dev husky 
    npx husky install
    npx husky add .husky/pre-commit  "echo !!!!!----pre-commit----!!!!"
    npx husky add .husky/commit-msg  "echo !!!!!----commit-msg----!!!!"
    npx husky add .husky/post-commit "echo !!!!!----post-commit----!!!!"
fi

# init commitlint
python3 $ComponentsPath/Tools/check-dep.py ./ @commitlint
if [ $? == 1 ]
then
    npm install --save-dev @commitlint/{config-conventional,cli}
fi

# init clang-format
npm list -g | grep clang-format
if [ $? == 1 ]
then
    npm install -g clang-format
    ls -al .clang-format
    if [ $? == 1 ]
    then
        clang-format -style=Google -dump-config > .clang-format
    fi
fi

# init gitmoji-changelog
# gitmoji-changelog must be install in global
npm list -g | grep gitmoji-changelog
if [ $? == 1 ]
then
    npm install -g gitmoji-changelog
fi

# #---------init npm package dependences---------#

####---------init python package dependences---------#
pip3 list | grep chardet
if [ $? == 1 ]
then
    pip3 install chardet
fi
# init cpplint
pip3 list | grep cpplint
if [ $? == 1 ]
then
    pip3 install cpplint
fi
####---------init python package dependences---------#


###### add task ######
#---pre-commit hook task
# add file-code-convert task
cat .husky/pre-commit | grep "python3 "$ComponentsPath"/tasks/code-convert.py"
if [ $? == 1 ]
then
    npx husky add .husky/pre-commit "python3 "$ComponentsPath"/tasks/code-convert.py $ComponentsPath"
fi
# add code-format task
cat .husky/pre-commit | grep "python3 "$ComponentsPath"/tasks/code-format.py"
if [ $? == 1 ]
then
    npx husky add .husky/pre-commit "python3 "$ComponentsPath"/tasks/code-format.py"
fi
# add code-static-check task
cat .husky/pre-commit | grep "python3 "$ComponentsPath"/tasks/code-static-check.py"
if [ $? == 1 ]
then
    npx husky add .husky/pre-commit "python3 "$ComponentsPath"/tasks/code-static-check.py"
fi
#---commit-msg hook task
# add git-commit-message-check task
cat .husky/commit-msg | grep "npx --no -- commitlint --edit ${1}"
if [ $? == 1 ]
then
    npx husky add .husky/commit-msg "npx --no -- commitlint --edit ${1}"
fi
#---post-commit hook task
# add changelog task
cat .husky/post-commit | grep "python3 "$ComponentsPath"/tasks/update-changelog.py"
if [ $? == 1 ]
then
    npx husky add .husky/post-commit "python3 "$ComponentsPath"/tasks/update-changelog.py ./"
fi

#---load user config
python3 $ComponentsPath/config.py