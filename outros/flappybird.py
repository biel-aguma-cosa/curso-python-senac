import math
import random
import time
import tkinter as tk
import threading

root = tk.Tk()
root.title("pasrinho voa voa")
root.resizable(False,False)

running = False
t0 = time.time()

screen = [600,400] # dimensões da tela
fps = 1/60
gap = 120 # espaço (vertical) entre os canos
canvas = tk.Canvas(root,width=600,height=400,background='black')
canvas.pack()

class rect():
    def __init__(self,x,y,w,h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self.image = None
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        if type(value) in [int,float]:
            self._x = float(value)
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        if type(value) in [int,float]:
            self._y = float(value)
    
    @property
    def position(self):
        return [self._x,self._y]
    @position.setter
    def position(self,value):
        if type(value) in [tuple,list] and len(value) >= 2:
            self._x, self._y = value[0], value[1]
        elif type(value) in [int,float]:
            self._x, self._y = float(value), float(value)
    @position.getter
    def position(self):
        return [self.x,self.y]
    
    @property
    def w(self):
        return self._w
    @w.setter
    def w(self,value):
        if type(value) in [int,float]:
            self._w = float(value)
            return self._w
    @property
    def h(self):
        return self._h
    @h.setter
    def h(self,value):
        if type(value) in [int,float]:
            self._h = float(value)
            return self._h
    
    @property
    def scale(self):
        return [self._w,self._h]
    @scale.setter
    def scale(self,value):
        if type(value) in [tuple,list] and len(value) >= 2:
            self._w, self._h = value[0], value[1]
        elif type(value) in [int,float]:
            self._w, self._h = float(value), float(value)
    @scale.getter
    def scale(self):
        return [self._w,self._h]

    def draw(self,color,surface):
        boop = self.image # variavel temporária que segura a imagen antiga
        self.image = surface.create_rectangle(
            int(self.x),
            int(self.y),
            int(self.x)+self.w,
            int(self.y)+self.h,
            fill = color
            )
        if boop != None:
            surface.delete(boop)
    def collidewith(self,other):
        if (self.x + self.w >= other.x  and  # r1 right edge past r2 left
            self.x <= other.x + other.w and  # r1 left edge past r2 right
            self.y + self.h >= other.y  and  # r1 top edge past r2 bottom
            self.y <= other.y + other.h):    # r1 bottom edge past r2 top
            return True
        else:
            return False

player = {
    'rect' : rect(60,20,40,40),
    'speed' : [0.0,0.0]
}
pipes = {
    'rect' : [
        [rect(0,0,50,400),rect(0,0,50,400)],
        [rect(0,0,50,400),rect(0,0,50,400)]
        ],
    'pos' : [
        [0,0],
        [0,0]
    ],
    'x0' : [
        600,900
    ]
    }

def input_manager(event):
    global player
    global fps
    if event.keycode == 32:
        player['speed'][1] = -5
root.bind('<Key>',input_manager)


def pipe_setup(index):
    global pipes, gap
    pipes['pos'][index][1] = random.randint(0,400-gap)
    pipes['pos'][index][0] = 600
    pipes['rect'][index][0].x = pipes['pos'][index][0]
    pipes['rect'][index][1].x = pipes['pos'][index][0]
    pipes['rect'][index][0].y = pipes['pos'][index][1] - pipes['rect'][index][0].h
    pipes['rect'][index][1].y = pipes['pos'][index][1] + gap

def game_loop():
    global root, canvas, t0, running, player, screen, pipes
    t0 = time.time()
    while (time.time() - t0) < 1:
        pass
    else:
        pipe_setup(0)
        pipe_setup(1)
        pipes['pos'][1][0] = 900
        pipes['rect'][1][0].x = pipes['pos'][1][0]
        pipes['rect'][1][1].x = pipes['pos'][1][0]
        running = True

    while running:
        if time.time() - t0 >= fps:

            player['speed'][0] = 0*fps      
            player['speed'][1] += 12*fps

            player['rect'].x += player['speed'][0]
            player['rect'].y += player['speed'][1]

            player['rect'].draw('red',canvas)

            for pipe in pipes['rect']:
                pipe[0].x -= 60*fps
                pipe[1].x -= 60*fps
                pipe[0].draw('green',canvas)
                pipe[1].draw('green',canvas)
                if pipe[0].x+pipe[0].w < 0:
                    pipe_setup(0)
                if pipe[1].x+pipe[1].w < 0:
                    pipe_setup(1)

            t0 = time.time()

loop = threading.Thread(target=game_loop)
loop.start()

root.mainloop()