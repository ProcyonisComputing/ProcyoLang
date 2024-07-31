# ProcyoLang
ProcyoLang Interactive Interpreted Programming Language developed by [Gautham Nair](https://github.com/gauthamnair2005)

Latest : `ProcyoLang 0.64.0 Alpha 7`

Tools Included:
* ProcyoLang Interactive Shell (procyolang.py)
* ProcyoLang Script Interpreter (pl.py)
* Sample ProcyoLang Source Code (prog.pcl)

## ProcyoLang Interactive Shell vs ProcyoLang Script Interpreter:
### ProcyoLang Interactive Shell
The ProcyoLang Interactive Shell is a command-line interface that allows users to interact with ProcyoLang, however, it lacks few features/commands present in ProcyoLang Script Interpreter, like actual `for` loop.
### ProcyoLang Script Interpreter
The ProcyoLang Script Interpreter is a command-line tool that runs ProcyoLang Source Files (.pcl), which is supplied to it as argument.

#### Usage:
`pl prog.pcl`

## What's new in Alpha 7?
* Added support for `till` and `noDuckTill` member operators in `for` loop.
* Updated `input` to actually take input and store it in the specified variable.
* Added new string space escape sequence `|s|` in `for` loop and `input` routines.
* Fixed known bugs.

## What was new in Alpha 6?
* Added support for "real `for` loop", with print integer, string or iterating variable value support.
* Fixed few bugs.
* Removed old, fake `for` and `xfor` commands.
* Started maintaining proper `README.md`.
