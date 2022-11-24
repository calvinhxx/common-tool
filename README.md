# PC COMMON TOOLS

Talkline_PC 的一些软件基建、质量工程工具

## Getting started

```
#in project workspace root path
sudo ./init.sh
```
### Test Demo
```
#in project workspace root path
python3 ./test-demo/test.py
```

## Content

- [PC COMMON TOOLS](#pc-common-tools)
  - [Getting started](#getting-started)
    - [Test Demo](#test-demo)
  - [Content](#content)
    - [支持平台](#支持平台)
    - [环境依赖](#环境依赖)
        - [Python  依赖](#python--依赖)
        - [Npm 依赖](#npm-依赖)
    - [支持功能](#支持功能)
      - [文件自动转码](#文件自动转码)
      - [代码格式化](#代码格式化)
      - [代码静态检测](#代码静态检测)
      - [git\_commit信息规范检测](#git_commit信息规范检测)
      - [changelog自动生成](#changelog自动生成)

### 支持平台

- [x] `MAC` Passing
- [ ] `windows` Todo

### 环境依赖

- Python `>=3.7`
- Npm `>=8.5.5`

>通过npm/python3完成依赖包管理。
若找不到npm/python3, brew install 或者在官网下载安装包
>

##### Python  依赖

- chardet
- [cpplint](https://github.com/cpplint/cpplint)
  
##### [Npm](https://www.npmjs.com/) 依赖

- [husky](https://github.com/typicode/husky)
- [commitlint](https://github.com/conventional-changelog/commitlint)
- [clang-format](https://clang.llvm.org/docs/ClangFormat.html)
- [gitmoji-changelog](https://github.com/frinyvonnick/gitmoji-changelog)

### 支持功能

- [x] [文件自动转码](#文件自动转码)
- [x] [代码格式化](#代码格式化)
- [x] [代码静态检测](#代码静态检测)
- [x] [git_commit信息规范检测](#git_commit信息规范检测)
- [x] [changelog自动生成](#changelog自动生成)
- [ ] [基于AST代码检测](#基于AST代码检测)
- [ ] [TDD工具](#TDD工具)

#### 文件自动转码
> 处理windows gbk 与 unix utf-8编码问题。确保纳入版本控制文件为utf-8标准编码。
#### 代码格式化
> 选用clang-format工具,在pre-commit hook中自动增量格式化.cpp .h文件为[google style](https://google.github.io/styleguide/cppguide.html)，确保版本库内代码风格统一
#### 代码静态检测
> 选用google官方支持的cpplint作为检测工具，提高代码质量,无基础错误
#### git_commit信息规范检测
> 提交代码必须符合.commitlintrc.js内的规范commit,规范版本库commit message方便CodeView
#### changelog自动生成 
> Commit成功后会通过gitmoji-changelog工具自动更新CL,方便CodeView
