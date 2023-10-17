from tkinter import *

compiler = Tk()
compiler.title('RV32I Compiler')

def convert(input_str):
    # Split the string into a list of words by spaces
    words = input_str.split()
    return words

def get_register_number(register_name):
    if register_name.startswith('x'):
        return int(register_name[1:])  # Extract the number part after 'x'
    else:
        raise ValueError('Invalid register name')

def build_r_type(opcode, rd, rs1, rs2, funct3, funct7):
    instruction = f'{funct7:07b}{rs2:05b}{rs1:05b}{funct3:03b}{rd:05b}{opcode:07b}'
    return instruction

def build_i_type(opcode, rd, rs1, imm, funct3):
    instruction = f'{imm:012b}{rs1:05b}{funct3:03b}{rd:05b}{opcode:07b}'
    return instruction

def build(instruction):
    opcode = {
        'add': 51, 'sub': 51, 'sll': 51, 'slt': 51, 'sltu': 51,
        'xor': 51, 'srl': 51, 'sra': 51, 'or': 51, 'and': 51,
        'addi': 19
    }.get(instruction[0], -1)

    if opcode == -1:
        return 'Invalid instruction'

    if opcode == 51:
        rd = get_register_number(instruction[1])
        rs1 = get_register_number(instruction[2])
        rs2 = get_register_number(instruction[3])
        funct3 = {
            'add': 0, 'sub': 0, 'sll': 1, 'slt': 2, 'sltu': 3,
            'xor': 4, 'srl': 5, 'sra': 5, 'or': 6, 'and': 7
        }.get(instruction[0])

        funct7 = 0
        if instruction[0] == 'sub':
            funct7 = 32
        elif instruction[0] in ('srl', 'sra'):
            funct7 = 32 if instruction[0] == 'sra' else 0

        return build_r_type(opcode, rd, rs1, rs2, funct3, funct7)
    elif opcode == 19:
        rd = get_register_number(instruction[1])
        rs1 = get_register_number(instruction[2])
        imm = int(instruction[3])
        funct3 = {
            'addi': 0
        }.get(instruction[0])
        return build_i_type(opcode, rd, rs1, imm, funct3)

def run():
    code = editor.get("1.0", END)
    code_lines = code.splitlines()

    output = []
    memory_index = 0  # Initialize the memory index
    for line in code_lines:
        words = convert(line)
        instruction = build(words)
        if instruction != 'Invalid instruction':
            comment = ' // ' + ' '.join(words)  # Create a comment with the original instruction
            formatted_instruction = f"memory[{memory_index}] = 32'b{instruction[:7]}_{instruction[7:12]}_{instruction[12:17]}_{instruction[17:20]}_{instruction[20:25]}_{instruction[25:]};{comment}\n"
            output.append(formatted_instruction)
            memory_index += 1  # Increment the memory index

    code_output.delete("1.0", END)
    code_output.insert(END, ''.join(output))


menu_bar = Menu(compiler)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
