[中文](./README.zh-CN.md) / [English](./README.md)

# common-tool

[![符合标准的阅读手册](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

PC端C++开发软件基建、质量工程工具

## 目录

- [common-tool](#common-tool)
  - [目录](#目录)
  - [背景](#背景)
  - [用法](#用法)
    - [依赖](#依赖)
        - [Python 依赖](#python-依赖)
        - [Npm 依赖](#npm-依赖)
    - [支持平台](#支持平台)
    - [支持功能](#支持功能)
      - [文件自动转码](#文件自动转码)
      - [代码格式化](#代码格式化)
      - [代码静态检测](#代码静态检测)
      - [Git\_commit信息规范检测](#git_commit信息规范检测)
      - [Changelog自动生成](#changelog自动生成)
  - [维护者](#维护者)
  - [许可](#许可)

## 背景
规范纳入版本控制代码，提高软件质量，在添加一些任务在githook中。

## 用法
- Mac:
  **在工作空间根目录**
  `sudo ./init.sh`
- Win:
  **在git bash的cmd终端**
  `./init.sh`
  
`quanlity-components/config.py 配置功能`
`!!!初始成功,相关依赖安装成功后,注意重启Git Gui/Git Cmd 重载环境变量`

### 依赖
- Python `>=3.7`
- Npm `>=8.5.5`

##### Python 依赖

- chardet
- [cpplint](https://github.com/cpplint/cpplint)
  
##### Npm 依赖

- [husky](https://github.com/typicode/husky)
- [commitlint](https://github.com/conventional-changelog/commitlint)
- [clang-format](https://clang.llvm.org/docs/ClangFormat.html)
- [gitmoji-changelog](https://github.com/frinyvonnick/gitmoji-changelog)

### 支持平台

- ✅  `MAC` 
- ✅  `windows` 

### 支持功能

- [x] [文件自动转码](#文件自动转码)
- [x] [代码格式化](#代码格式化)
- [x] [代码静态检测](#代码静态检测)
- [x] [Git_commit信息规范检测](#git_commit信息规范检测)
- [x] [Changelog自动生成](#changelog自动生成)
- [ ] [基于AST代码检测](#基于AST代码检测)
- [ ] [TDD工具](#TDD工具)

---

#### 文件自动转码
> 处理windows gbk 与 unix utf-8编码问题。确保纳入版本控制文件为utf-8标准编码。
#### 代码格式化
> 选用clang-format工具,在pre-commit hook中自动增量格式化.cpp .h文件为[google style](https://google.github.io/styleguide/cppguide.html)，确保版本库内代码风格统一，支持git diff增量、文件增量。
#### 代码静态检测
> 选用google官方支持的cpplint作为检测工具，提高代码质量,无基础错误
#### Git_commit信息规范检测
> 提交代码必须符合.commitlintrc.js内的规范commit,规范版本库commit message方便CodeView
#### Changelog自动生成 
> Commit成功后会通过gitmoji-changelog工具自动更新CL,方便CodeView
> 
## 维护者

[@calvinhxx](https://github.com/calvinhxx)

## 许可

MIT © 2023 calvinhxx