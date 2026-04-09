import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
dt = 0
running = True
clock = pygame.Clock()

selected_field = ''

class TextField():
    def __init__(self,pos,size,font=pygame.font.SysFont('consolas',12),default_text = ''):
        self.font = font
        self.color = 'black'
        self.bgcolor = 'white'
        self.text = default_text

        self.image = pygame.Surface(size=size)
        self.image.fill(self.bgcolor)
        self.image.blit(self.font.render(self.text,False,self.color),(0,0))
        
        self.rect = pygame.Rect(pos[0],pos[1],size[0],size[1])
    def insert(self,char):
        text = ''
        buffer = []
        for character in self.text:
            buffer.append(character)
        if char == '\x08':
            if len(buffer):
                buffer.pop()
            for character in buffer:
                text += character
            self.text = text
        elif char == '\r':
            pass
        else:
            self.text += char

        self.image.fill(self.bgcolor)
        self.image.blit(self.font.render(self.text,False,self.color),(0,0))
    def backspace(self):
        self.text

    def draw(self):
        global screen
        screen.blit(self.image,self.rect)
text_fields = [
    TextField(
        [30,30],
        [100,20],
        default_text=''
    ),
]


while running:
    mouse = pygame.mouse.get_pos()
    
    screen.fill('black')

    for field in text_fields:
        field.draw()
                


    pygame.display.flip()
    dt = clock.tick(60)/1000