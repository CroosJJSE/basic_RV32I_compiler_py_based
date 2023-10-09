from tkinter import *
compiler = Tk()
compiler.title('RV32I Compiler')
def run():
    code = editor.get("1.0", END)
    print(code)
    output = 'we received the code'
    code_output.insert("1.0", output)
    
    
    
menu_bar = Menu(compiler)   

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()
compiler.mainloop
