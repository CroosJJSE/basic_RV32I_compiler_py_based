# basic_RV32I_compiler_py_based

## what is Translator?
We are using High_level language (python , C++, Java); But machine only understand the bits,
the translator is a complex software which is convert the highlevel language into machine readable.

## two types of translators

### Interpretor 
- An interpreter translates and executes the source code line by line, statement by statement, directly.
- It reads a high-level language program, processes it, and executes it immediately.
- Errors are typically reported as they occur in the code.
- Interpreters are often used in languages like Python, JavaScript, and Ruby.
- They tend to be slower than compilers because they execute code as they go.

### compiler
A compiler is a complex piece of software whose job is to convert source code to machine understandable code (or binary code) in **one go**.

- A compiler translates the entire source code into machine code or an intermediate representation in a single step.
- It generates an executable file or bytecode, which can be run without recompilation.
- Compilation typically takes longer than interpretation but may result in faster execution.
- Compilers are commonly used for languages like C, C++, and Java (in some cases).
- Errors are usually reported after the entire code is analyzed and compiled.

![image](https://github.com/CroosJJSE/basic_RV32I_compiler_py_based/assets/141708783/016b6910-3e47-40a5-8a4c-a33e9ede4397)


So I am making a simple compiler to convert this rv32I base readable instruction to instruction to feed to instruction memory

![image](https://github.com/CroosJJSE/basic_RV32I_compiler_py_based/assets/141708783/78c60c6d-d4e2-4d0b-b2f0-d395da5d6059)

## From this to the below formate
![image](https://github.com/CroosJJSE/basic_RV32I_compiler_py_based/assets/141708783/5181b23c-93c8-41e4-a62b-6f837cd1d35b)


# Steps
## Step 1 python implementation to make a interface to take input and provide output


![image](https://github.com/CroosJJSE/basic_RV32I_compiler_py_based/assets/141708783/1e54064c-8a3a-450b-8d98-e9ad1ff5b6cd)

## step 2 convert it and connect to output


