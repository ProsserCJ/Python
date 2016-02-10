from tkinter import *
from functools import partial
from math import *

bHeight = 0
bWidth = 5
padx = 2
pady = 2

class Calculator(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.initComponents()
        self.pack()

    def initComponents(self):
        self.text = StringVar(self)
        self.textBox = Entry(self, textvariable=self.text,
                             state=DISABLED,
                             disabledbackground='white',
                             disabledforeground = 'black',
                             justify=RIGHT,
                             width=33)
        self.textBox.grid(row=0, column=0, columnspan=5, padx = 4)

        self.buttons = dict()
        col,row = 2,3
        
        #Add numeric buttons 1-9
        for i in range(1,10):
            self.buttons[str(i)] = Button(self, text=str(i), command = partial(self.push, i), height=bHeight, width=bWidth)
            self.buttons[str(i)].grid(row=row, column=col, padx=padx, pady=pady)
            col += 1
            if (col > 4):
                col = 2
                row -= 1

        #Add bottom row (0, ., -)
        col = 2
        for s in ['0', '.', '-']:
            self.buttons[s] = Button(self, text=s, command = partial(self.push, s), height=bHeight, width=bWidth)
            self.buttons[s].grid(row=4, column=col, padx=padx, pady=pady)
            col += 1

        #Add arithmetic operations
        row = 1
        for s in [' / ',' * ',' - ',' + ']:
            self.buttons[s] = Button(self, text=s, command = partial(self.push, s), height=bHeight, width=bWidth)
            self.buttons[s].grid(row=row, column=5, padx=padx, pady=pady)
            row += 1

        #Add enter, erase, and clear
        self.buttons['enter'] = Button(self, text='enter', command = self.calculate, height=bHeight, width=2*bWidth)
        self.buttons['enter'].grid(row=4, column=6, columnspan=2, padx=padx, pady=pady)
        self.buttons['<-'] = Button(self, text='<-', command = self.erase, height=bHeight, width=bWidth)
        self.buttons['<-'].grid(row=0, column=5, padx=padx, pady=pady)
        self.buttons['clear'] = Button(self, text='clear', command = self.clear, height=bHeight, width=bWidth)
        self.buttons['clear'].grid(row=0, column=6, padx=padx, pady=pady)

        #Add ln, log, 1/x, x^y
        self.buttons['ln'] = Button(self, text='ln', command = partial(self.calculate, f=log), height=bHeight, width=bWidth)
        self.buttons['ln'].grid(row=3, column=0, padx=padx, pady=pady)
        self.buttons['log'] = Button(self, text='log', command = partial(self.calculate, f=log10), height=bHeight, width=bWidth)
        self.buttons['log'].grid(row=4, column=0, padx=padx, pady=pady)
        self.buttons['1/x'] = Button(self, text='1/x', command = partial(self.calculate, f=self.reciprocal), height=bHeight, width=bWidth)
        self.buttons['1/x'].grid(row=3, column=1, padx=padx, pady=pady)
        self.buttons['x^y'] = Button(self, text='x^y', command = partial(self.push, '**'), height=bHeight, width=bWidth)
        self.buttons['x^y'].grid(row=4, column=1, padx=padx, pady=pady)

        #Add parens
        self.buttons['('] = Button(self, text='(', command = partial(self.push, '('), height=bHeight, width=bWidth)
        self.buttons['('].grid(row=1, column=0, padx=padx, pady=pady)
        self.buttons[')'] = Button(self, text=')', command = partial(self.push, ')'), height=bHeight, width=bWidth)
        self.buttons[')'].grid(row=1, column=1, padx=padx, pady=pady)
        
        #Add pi and e
        self.buttons['pi'] = Button(self, text='pi', command = partial(self.push, str(pi)), height=bHeight, width=bWidth)
        self.buttons['pi'].grid(row=2, column=0, padx=padx, pady=pady)
        self.buttons['e'] = Button(self, text='e', command = partial(self.push, str(e)), height=bHeight, width=bWidth)
        self.buttons['e'].grid(row=2, column=1, padx=padx, pady=pady)

        #Add trig functions
        self.buttons['sin'] = Button(self, text='sin', command = partial(self.calculate, f=sin), height=bHeight, width=bWidth)
        self.buttons['sin'].grid(row=1, column=6, padx=padx, pady=pady)
        self.buttons['cos'] = Button(self, text='cos', command = partial(self.calculate, f=cos), height=bHeight, width=bWidth)
        self.buttons['cos'].grid(row=2, column=6, padx=padx, pady=pady)
        self.buttons['tan'] = Button(self, text='tan', command = partial(self.calculate, f=tan), height=bHeight, width=bWidth)
        self.buttons['tan'].grid(row=3, column=6, padx=padx, pady=pady)

        self.buttons['sinh'] = Button(self, text='sinh', command = partial(self.calculate, f=sinh), height=bHeight, width=bWidth)
        self.buttons['sinh'].grid(row=1, column=7, padx=padx, pady=pady)
        self.buttons['cosh'] = Button(self, text='cosh', command = partial(self.calculate, f=cosh), height=bHeight, width=bWidth)
        self.buttons['cosh'].grid(row=2, column=7, padx=padx, pady=pady)
        self.buttons['tanh'] = Button(self, text='tanh', command = partial(self.calculate, f=tanh), height=bHeight, width=bWidth)
        self.buttons['tanh'].grid(row=3, column=7, padx=padx, pady=pady)

    def push(self, s):
        current = self.text.get()
        if current == "ERR": current = ''
        self.text.set(current+str(s))
        self.textBox.xview(len(self.text.get())-1)

    def calculate(self, f=None):
        try:
            val = eval(self.text.get())
            try: val=f(val)
            except: pass
            if abs(val) < pow(10,-15): val = 0.0
            self.text.set(str(val))
        except:
            self.text.set("ERR")

    def reciprocal(self, x): return 1/x
    def clear(self): self.text.set('')
    def erase(self): self.text.set(self.text.get()[:-1])
        
if __name__ == "__main__":
    top = Tk()
    calc = Calculator(top)
    top.mainloop()
