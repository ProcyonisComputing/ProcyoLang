![ProcyoLang Logo](https://raw.githubusercontent.com/ProcyonisSoftware/ProcyonComponentsLogos/06fa759e799c31f77d4e35e31bd7c8dbe6b5c5bd/ProcyoLang.png)

ProcyoLang Interpreted Programming Language developed by [Gautham Nair](https://github.com/gauthamnair2005)

Latest : `ProcyoLang 1.0.1 Alpha 10`

Tools Included:
* ProcyoLang Interactive Shell (procyolang.py) (Will be removed from Beta releases (after Alpha 10))
* ProcyoLang Script Interpreter (pl.py)
* Sample ProcyoLang Source Code (prog.pcl)

## ProcyoLang Interactive Shell vs ProcyoLang Script Interpreter:
### ProcyoLang Interactive Shell
The ProcyoLang Interactive Shell is a command-line interface that allows users to interact with ProcyoLang, however, it lacks few features/commands present in ProcyoLang Script Interpreter, like actual `for` loop, `if-else` statements, etc.
### ProcyoLang Script Interpreter
The ProcyoLang Script Interpreter is a command-line tool that runs ProcyoLang Source Files (.pcl), which is supplied to it as argument.

#### Usage:
`python pl.py prog.pcl`

## What's new in Alpha 10?
* Improved array declaration.
* Experimental support for arrays in for loop.
* Fixed known bugs.

## What was new in Alpha 9?
* For loop code refactor.
* Added support for more operations in for loop.
* Improved error handling in ProcyoLang Script Interpreter.
* Interactive mode will be removed from Beta releases, which will arrive after Alpha 10.

## What was new in Alpha 8?
* Added support for simple `if-else`.
* We stopped updating the Interactive Shell with newer commands and script-specific features like loops, conditional statements, etc, as we promote and recommend the Script Interpreter. However, we will still provide the Interactive Shell in downloads and repository and not delete it.
* We stopped binary releases of pre-release versions of ProcyoLang, we will restart the binary executable release while this project reaches stability and enters stable or release-preview state.

## What was new in Alpha 7?
* Added support for `till` and `noDuckTill` member operators in `for` loop.
* Updated `input` to actually take input and store it in the specified variable.
* Added new string space escape sequence `|s|` in `for` loop and `input` routines.
* Fixed known bugs.

## What was new in Alpha 6?
* Added support for "real `for` loop", with print integer, string or iterating variable value support.
* Fixed few bugs.
* Removed old, fake `for` and `xfor` commands.
* Started maintaining proper `README.md`.
