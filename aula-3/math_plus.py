import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()

font = tkfont.Font(family="Consolas",size=16)

frame = [
    tk.Frame(root),
    tk.Frame(root),
    tk.Frame(root)
]
for f in frame:
    f.pack()


X_label = tk.Label(frame[0],text="X:",font=font)
X_field = tk.Entry(frame[0],font=font)
Y_label = tk.Label(frame[0],text="Y:",font=font)
Y_field = tk.Entry(frame[0],font=font)

X_label.grid(row=0,column=0,sticky='w')
X_field.grid(row=0,column=1,sticky='we')
Y_label.grid(row=1,column=0,sticky='w')
Y_field.grid(row=1,column=1,sticky='we')


add_label = tk.Label(frame[1],text="adição:",font=font)
sub_label = tk.Label(frame[1],text="subtração:",font=font)
mul_label = tk.Label(frame[1],text="multiplicação:",font=font)
div_label = tk.Label(frame[1],text="divisão:",font=font)
add_label.grid(row=0,column=0,sticky='w')
sub_label.grid(row=1,column=0,sticky='w')
mul_label.grid(row=2,column=0,sticky='w')
div_label.grid(row=3,column=0,sticky='w')
add_r_label = tk.Label(frame[1],text="X + Y = ?",font=font)
sub_r_label = tk.Label(frame[1],text="X - Y = ?",font=font)
mul_r_label = tk.Label(frame[1],text="X * Y = ?",font=font)
div_r_label = tk.Label(frame[1],text="X / Y = ?",font=font)
add_r_label.grid(row=0,column=1,sticky='w')
sub_r_label.grid(row=1,column=1,sticky='w')
mul_r_label.grid(row=2,column=1,sticky='w')
div_r_label.grid(row=3,column=1,sticky='w')

def run():
    global X_field, Y_label
    global add_r_label, sub_r_label, mul_r_label, div_r_label

    X,Y = float(X_field.get()), float(Y_field.get())

    add_r_label['text'] = f"X + Y = {X+Y}"
    sub_r_label['text'] = f"X - Y = {X-Y}"
    mul_r_label['text'] = f"X * Y = {X*Y}"
    div_r_label['text'] = f"X / Y = {X/Y}"

con_label = tk.Label(frame[2],text='Performar equações:',font=font)
confirm = tk.Button(frame[2],text='OK',command=run,font=font)

con_label.grid(row=0,column=0,sticky='w')
confirm.grid(row=0,column=1,sticky='w')

root.mainloop()