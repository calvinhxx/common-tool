#!/usr/bin/python3

#因ide不能很好的支持某种类型的文件的批量转码写个小工具方便开发。

import os,sys
import chardet
import traceback

def __usage():
    print("""
    Usage:

        python3 file-code-convert-script.py path1 [path2] [path3]....

    """)

def convert_content( filename, in_enc = "GBK", out_enc="UTF8" ):  #GBK/GBK2312 -> UTF8
    print( filename + " to utf-8!")
    content = open(filename,'rb').read()
    new_content = content.decode(in_enc).encode(out_enc)
    open(filename, 'wb').write(new_content)
    print("convert done" + filename)

def determine_suffix(file):
    suffix = os.path.splitext(file)[-1]
    # print(suffix, type(suffix))
    if  suffix== (".c") or suffix == (".h") or suffix == (".c++") or suffix == (".h++") or suffix == (".cc") or suffix == (".cpp"):
        return True
    else:
        return False

def determine_extensions(file):
    #TODO 用正则表达式优化、扩展编码的类型
    content = open(file,'rb').read()
    result = chardet.detect(content)#通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
    # print(result)
    if result.get('encoding') == "GB2312":
        return True
    else:
        return False

def convert(path):
    try:
        # print("file:" + path)
        if determine_suffix(path):
            if determine_extensions(path):
                convert_content(path)
            else:
                # raise Exception("文件编码格式不匹配")
                pass
        else:
            # raise Exception("文件后缀不匹配")
            pass
    except Exception as e:
        traceback.print_exc()
        
def explore(path):
    for path_ in path:
        if os.path.isfile(path_):
            convert(path_)
        elif os.path.isdir(path_):
            for root, dirs, files in os.walk(path_):
                for file in files:
                    file_ = os.path.join(root, file)
                    convert(file_)
                    
def main():
    if len(sys.argv) <= 1:
        __usage()
        return -1
    else:
        return explore(sys.argv[1:])

if __name__ == "__main__":
    main()