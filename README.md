[中文](./README.zh-CN.md) / [English](./README.md)

# common-tool

[![standards-compliant readme](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

PC-based C++ development software infrastructure, quality engineering tools

## Contents

- [common-tool](#common-tool)
  - [Contents](#contents)
  - [Background](#background)
  - [Usage](#usage)
    - [Dependencies](#dependencies)
        - [Python dependencies](#python-dependencies)
        - [Npm dependencies](#npm-dependencies)
    - [Supported platforms](#supported-platforms)
    - [Supported features](#supported-features)
      - [Automatic File Transcoding](#automatic-file-transcoding)
      - [Code Formatting](#code-formatting)
      - [Code Static Detection](#code-static-detection)
      - [Git\_commit Information Specification Detection](#git_commit-information-specification-detection)
      - [Changelog Automatically Generated](#changelog-automatically-generated)
  - [Maintainer](#maintainer)
  - [License](#license)

## Background
Specification incorporates version control code to improve software quality, after adding some tasks in git hook.

## Usage
- Mac:
  **in the workspace root directory**
  `sudo . /init.sh`
- Win:
  **in git bash's cmd terminal**
  `. /init.sh`
  
`quanlity-components/config.py configuration function`
`!!! After the initial success and the installation of the dependencies, take care to restart Git Gui/Git Cmd and reload the environment variables`

### Dependencies
- Python `>=3.7`
- Npm `>=8.5.5`

##### Python dependencies

- chardet
- [cpplint](https://github.com/cpplint/cpplint)
  
##### Npm dependencies

- [husky](https://github.com/typicode/husky)
- [commitlint](https://github.com/conventional-changelog/commitlint)
- [clang-format](https://clang.llvm.org/docs/ClangFormat.html)
- [gitmoji-changelog](https://github.com/frinyvonnick/gitmoji-changelog)

### Supported platforms

- ✅ `MAC` 
- ✅ `windows` 

### Supported features

- [x] [File-auto-transcoding](#automatic-file-transcoding)
- [x] [Code formatting](#code-formatting)
- [x] [Code static detection](#code-static-detection)
- [x] [Git_commit Information Specification Detection](#git_commit-information-specification-detection)
- [x] [Changelog Automatically Generated](#changelog-automatically-generated)
- [ ] [AST Code Based Detection](#ast-code-based-detection)
- [ ] [TDD Tool](#tdd-tool)

---

#### Automatic File Transcoding
> Handle windows gbk and unix utf-8 encoding issues. Ensure that version control files are included in utf-8 standard encoding.
#### Code Formatting
> Use clang-format tool to incrementally format .cpp .h files to [google style](https://google.github.io/styleguide/cppguide.html) in the pre-commit hook to ensure uniform code style in the repository, support git diff incremental, file incremental.
#### Code Static Detection
> choose google official support cpplint as a detection tool to improve code quality, no basic errors
#### Git_commit Information Specification Detection
> commit code must comply with the specification commit within .commitlintrc.js, specification repository commit message to facilitate CodeView
#### Changelog Automatically Generated 
> After a successful commit, the CL is automatically updated via the gitmoji-changelog tool for CodeView


## Maintainer

[@calvinhxx](https://github.com/calvinhxx)

## License

MIT © 2023 calvinhxx