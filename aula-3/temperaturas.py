import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

root = tk.Tk()
font = tkfont.Font(family="Consolas",size=16)

K, F, C = 0, 0, 0

C_label = tk.Label(root,text="0 °C",font=font)
K_label = tk.Label(root,text="0  K",font=font)
F_label = tk.Label(root,text="0 °F",font=font)
C_label.grid(row=0,column=0)
K_label.grid(row=1,column=0)
F_label.grid(row=2,column=0)

def update(i):
    global C_slider, K_slider, F_slider, K, F, C
    match i:
        case 0:
            C = C_slider.get()
            K = C + 273,15
            F = C * 9/5 + 32
        case 1:
            K = K_slider.get()
            C = K - 273,15
            F = (C * 1.8) + 32
        case 2:
            F = F_slider.get()
            C = (F - 32)*5/9
            K = C + 273,15
    C_label['text'] = f"{str(C)[:5]} °C"
    K_label['text'] = f"{str(K)[:5]}  K"
    F_label['text'] = f"{str(F)[:5]} °F"


C_slider = ttk.Scale(root,from_=-100,to=100,command=lambda x=0:update(0))
K_slider = ttk.Scale(root,from_=-100,to=100,command=lambda x=1:update(1))
F_slider = ttk.Scale(root,from_=-100,to=100,command=lambda x=2:update(2))
C_slider.grid(row=0,column=1)
K_slider.grid(row=1,column=1)
F_slider.grid(row=2,column=1)

root.mainloop()