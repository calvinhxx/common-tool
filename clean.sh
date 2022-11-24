#!/bin/bash

# !!!!!!!! run this script by root !!!!!!!!
echo "!!!---Confirm Clean All?---enter(y/n)---!!!"
read x
# now check if $x is "y"
if [ "$x" != "y" ]; then
    exit 1
fi

###### clean dependences ######
#---------clean npm package dependences---------#
npm uninstall husky
npm uninstall @commitlint

npm uninstall -g gitmoji-changelog
npm uninstall -g clang-format
#---------clean npm package dependences---------#

####---------clean python package dependences---------#
echo "y" | pip3 uninstall chardet
echo "y" | pip3 uninstall cpplint
####---------clean python package dependences---------#

###### clean products ######
rm -rf .husky
rm -rf node_modules
rm -rf package-lock.json
rm -rf package.json
rm -rf CHANGELOG.md
###### clean products ######

