import tkinter as tk
import logic
from exceptions import *
# from tkinter import messagebox


class CustomWidget(tk.Frame):
    def __init__(self, parent, label, default=""):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text=label, anchor="w")
        self.entry = tk.Entry(self)
        self.entry.insert(0, default)

        self.label.pack(side="left", fill="x")
        self.entry.pack(side="right", fill="x", padx=10)
        
# borderwidth=1, relief="solid"
    def get(self):
        return self.entry.get()


class ErrorMsg(tk.Frame):
    def __init__(self, parent, label):
        super().__init__(self, parent)
        
        label = tk.Label(self, text=label, anchor='center')
        
        
class GoButton(tk.Frame):
    def __init__(self, parent, text, command):
        tk.Frame.__init__(self, parent)
        
        self.button = tk.Button(self, text=text, command=command)
        

class CodeInput(tk.Frame):
    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent)
        
        pass


class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.difficult = 4
        self.label = tk.Label(self)
        self.e1 = CustomWidget(self, "First Name:", "Noname")
        self.e2 = CustomWidget(self, "Difficult:", self.difficult)
        self.e3 = CustomWidget(self, "Code:")
        # self.text1 = tk.Text(self)
        self.go_button = tk.Button(self, text="Go!", command=self.go)
        
        # self.go_button = GoButton(parent, label="Go!", command=self.go)
        self.inp_button = tk.Button(self, text='input', command=self.press_input)
        # self.grid = tk.Canvas(self)
        self.input_error = tk.Label(self)
        self.code_error = tk.Label(self)
        self.codes = tk.Label(self)
        self.bulls = tk.Label(self)
        self.cows = tk.Label(self)
        self.secret_code = []
        self.last_row = 9

        self.e1.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.e2.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.input_error.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.go_button.grid(row=3, column=0, columnspan=2)
        self.label.grid(row=4, column=0, sticky="ew", columnspan=2)
        
        # self.e3.grid_remove()
        self.code_error.grid(row=7, column=0, sticky="ew", columnspan=2)
        self.codes.grid(row=8, column=0, sticky="ew", columnspan=1)
        self.bulls.grid(row=8, column=1, sticky="ew")
        self.cows.grid(row=8, column=2, sticky="ew")

        # for c in range(4):
        #     self.grid_columnconfigure(c, weight=1)
        # for r in range(16):
        #     self.grid_rowconfigure(r, weight=1)
        self.fg_color = self.inp_button.cget('foreground')


    def go(self):
        symbols = [i for i in range(10)]
        name = self.e1.get()[0:16]
        self.difficult = self.e2.get()
        try:
            if int(self.difficult) < 3 or int(self.difficult) > 6:
                # messagebox.showerror("error", "try again")
                self.input_error.configure(text='Pls, choose between 3 and 6', fg='red')
                return
        except ValueError as e:
            self.input_error.configure(text='Difficult should be a num', fg='red')
            return
        else:
            self.input_error.configure(text='')
            
        self.secret_code = logic.make_code(symbols, int(self.difficult))

        self.label.configure(text="Game for %s. Try to find %s numbers" % (name, self.difficult))
        self.e3.grid(row=5, column=0, sticky='ew', columnspan=2)
        self.inp_button.grid(row=5, column=2, padx=0)
        self.codes.configure(text='codes')
        self.bulls.configure(text='bulls')
        self.cows.configure(text='cows')
        # self.text1.grid(row=5, column=0, columnspan=2, sticky='ew')
        # self.grid.grid(row=5, column=0)
        # self.grid.create_line((0,100,0,100))
        
    
    def press_input(self):
        try_code = self.e3.entry.get()
        try:
            logic.check_rules(try_code, int(self.difficult))
        except logic.UniqueError as e:            
            self.code_error.configure(text=f'numbers should be unique', fg='red')
            return
        except logic.LengthError as e:
            self.code_error.configure(text=f'The code length should be {self.difficult}', fg='red')
            return
        else:
            self.code_error.configure(text='')
        bulls, cows = logic.check(self.secret_code, try_code)
        c = tk.Label(self)
        c.grid(row=self.last_row+1, column=0, sticky='ew')
        c.configure(text=try_code)
        b = tk.Label(self)
        b.grid(row=self.last_row+1, column=1, sticky='ew')
        b.configure(text=bulls)
        co = tk.Label(self)
        co.grid(row=self.last_row+1, column=2, sticky='ew')
        co.configure(text=cows)
        self.e3.entry.delete(0, 'end')
        
        self.last_row += 1
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('350x400+400+400')
    App(root).place(x=0, y=0, relwidth=1, relheight=1)
    
    root.mainloop()
