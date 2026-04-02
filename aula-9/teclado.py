import tkinter, tkinter.font, tkinter.colorchooser

tkinter.colorchooser.askcolor()

root = tkinter.Tk()
font=tkinter.font.nametofont('system')
font.config(size=12)

screen = tkinter.Label(root,text='',background='white',width=15,height=2,font=font)

def Button(text):
    global screen
    self = tkinter.Button(
        root,text=text,
        width=10,height=10,
        font=font
    )
    if text == 'X':
        self['command'] = lambda: screen.config(text = '')
        self.config(background='red')
    else:
        self['command'] = lambda: screen.config(text = screen['text'] + text) if len(screen['text']) < 4 else print(end='')
    return self

buttons = [
    [Button('1'),Button('2'),Button('3')],
    [Button('4'),Button('5'),Button('6')],
    [Button('7'),Button('8'),Button('9')],
    [Button('*'),Button('0'),Button('#')],
]
X = Button('X')

screen.grid(row=0,column=0,columnspan=3)

for name in tkinter.font.names():
    print(name)

for x,_list in enumerate(buttons):
    for y, button in enumerate(_list):
        button.grid(column=y,row=x+1)
        button.config(width=4,height=2)
X.grid(columnspan=4,row=6)
X.config(width=13,height=1)


root.mainloop()