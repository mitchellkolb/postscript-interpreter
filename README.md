
<h1 align="center">Postscript Interpreter in Python</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/mitchellkolb/postscript-interpreter?color=DA1F26">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/mitchellkolb/postscript-interpreter?color=DA1F26">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mitchellkolb/postscript-interpreter?color=DA1F26">

  <img alt="Github stars" src="https://img.shields.io/github/stars/mitchellkolb/postscript-interpreter?color=DA1F26" />
</p>

<p align="center">
<img
    src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/Postscript-DA1F26?style=for-the-badge&logo=adobe&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"
    alt="Website Badge" />
</p>

An interpreter for the PostScript language in Python. PostScript is a stack-based, interpreted language developed by Adobe Systems long ago for producing vector graphics in the printing industry. My interpreter includes the operators: add, sub, mul, div, mod, eq, lt, gt, length, get, getinterval, put, if, ifelse, for, dup, copy, clear, exch, roll, and dict.

![project image](resources/image1.png)

<details>
<summary style="color:#5087dd">Watch the Full Video Demo Here</summary>

[![Full Video Demo Here](https://img.youtube.com/vi/VidKEY/0.jpg)](https://www.youtube.com/watch?v=VidKEY)

</details>

---


# Table of Contents
- [What I Learned](#what-i-learned-in-this-project)
- [Tools Used / Development Environment](#tools-used--development-environment)
- [Team / Contributors / Teachers](#team--contributors--teachers)
- [How to Set Up](#how-to-set-up)
- [Project Overview](#project-overview)
  - [Project Details](#project-details)
  - [Technical Plan](#technical-plan)
  - [Implementation Details](#implementation-details)
  - [Files and Structure](#files-and-structure)
  - [Implementation](#implementation)
  - [Example Usage](#example-usage)
  - [Results and Future Goals](#results-and-future-goals)
- [Acknowledgments](#acknowledgments)

---

# What I Learned in this Project
- How to code in python with emphasis using: 
    - Static Scoping and Dynamic Scoping
    - Pythons strong dyanmic typing
    - Data types / systems like iterators, iterables, streams, classes, closures, and objects
- Understanding how Pythons handles its Scope, Referencing Environment, and Activation Record when dealing with programs and data.
- Compile-time (static) type checking versus Run-time (dynamic) type checking
- Storage Management
  - Static area
  - Stack
  - Heap


# Tools Used / Development Environment
- Python
- Postscript
- VS Code
- Terminal
- Ubuntu





# Team / Contributors / Teachers
- [Mitchell Kolb](https://github.com/mitchellkolb)
- Associate Professor. Jeremy E. Thompson






# How to Set Up
This project was implemented on my local machine inside of a virtual machine using vscode:
- [Ubuntu Download](https://ubuntu.com/download/desktop)
- Install [Python](https://www.python.org/downloads/)
- Clone this repository 
- Open terminal at the codebase `~.../postscript-interpreter/sps-part-1/` or `~.../postscript-interpreter/sps-part-2/`
- Run the python file with some arugments in the main function or try out the tests file to see example input/output.



# Project Overview
I used Python to create an interpreter for the PostScript language. PostScript, developed by Adobe Systems, is a stack-based language used primarily for vector graphics in the printing industry. The interpreter supports a range of operators including arithmetic, comparison, string manipulation, and stack operations.


## Project Details
PostScript is a programming language primarily used in the printing industry to describe the appearance of text, graphics, and images on printed pages. Developed by Adobe Systems, PostScript is a stack-based, interpreted language, meaning it uses a stack data structure to hold operands and execute operations. In a stack-based language like PostScript, operators pop their operands from the stack and push their results back onto the stack.

For example, to add two numbers in PostScript, you would push the numbers onto the stack and then use the `add` operator, like so:
```
3 4 add
```
This sequence pushes `3` and `4` onto the stack, and then `add` pops these two values, adds them, and pushes the result (`7`) back onto the stack. 

The interpreter includes support for the following PostScript operators:
- Arithmetic: `add`, `sub`, `mul`, `div`, `mod`
- Comparison: `eq`, `lt`, `gt`
- String: `length`, `get`, `getinterval`, `put`
- Conditional: `if`, `ifelse`
- Loop: `for`
- Stack: `dup`, `copy`, `clear`, `exch`, `roll`
- Dictionary: `dict`, `begin`, `end`, `def`

## Technical Plan
The project employs Python to build the essential components of the interpreter:
- Operand Stack: Implemented as a Python list to store integers, strings, and code arrays.
- Dictionary Stack: Implemented as a Python list to store dictionaries, which are used to map PostScript variable names to their values.
- Operators: Implemented as Python functions that manipulate the operand and dictionary stacks.

## Implementation Details
The implementation is divided into two main parts:
1. Part 1 (HW4) focuses on building the operand stack, dictionary stack, variable definition, and operators that do not involve code arrays.
2. Part 2 (HW5) adds support for conditional operators, loop operators, and function calls.

## Files and Structure
- `HW4.py`: Contains the SPS Interpreter codebase for Part 1.
- `HW4test.py`: Contains the Unit Tests for the interpreter.
- `HW5.py`: Contains the SPS Interpreter codebase for Part 2.
- `HW5test.py`: Contains the Unit Tests for Part 2 of the interpreter.

## Implementation
In this project, the interpreter processes PostScript code by pushing and popping values on stacks and applying operators to these values. The operand stack is used to store data values and the dictionary stack to store mappings of variable names to their values. Operators are implemented to manipulate these stacks according to the semantics of the PostScript language.

## Example Usage
Here is a simple example demonstrating the usage of the interpreter:
```python
opPush(10)
opPush(20)
add()
print(opPop())  # Output: 30
```

## Results and Future Goals

During development, I learned how to implement key programming concepts in Python, including:

- Static and dynamic scoping
- Python's strong dynamic typing
- Data types and systems such as iterators, iterables, streams, classes, closures, and objects
- Understanding Python's handling of scope, referencing environment, and activation record
- Compile-time vs. run-time type checking
- Storage management: static area, stack, and heap

Future goals for this project include optimizing the interpreter's performance and extending it to support additional PostScript features and operators.




--- 
# Acknowledgments
This codebase and all supporting materials was made as apart of a course for my undergrad at WSU for CPTS 355 - Programming Language Design in the Summer of 2023. 

