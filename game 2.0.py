import pygame, random, time, math, numpy as np
x = 190
y = 320
pygame.init()
win = pygame.display.set_mode((400, 400))
z = 1
x1 = None
x2 = None
x3 = None
x4 = None
x5 = None
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
c = [1, 2]
random.shuffle(c)
cr = c[0]
# if cr == 2:
x1 = 42
x2 = 124


#    x3 = 160
#    x4 = 240
#    x5 = 320
# else:
#    x1 = 45
#    x2 = 125


#    x3 = 200
#    x4 = 280
#    x5 = 360


class Box():
    def __init__(self):
        self.x = x1
        self.y = 100
        self.w = 40
        self.h = 40

    def draw(self, color):
        pygame.draw.rect(win, (color), (self.x, self.y, self.w, self.h))

class Box2():
    def __init__(self):
        self.x = x2
        self.y = 100
        self.w = 40
        self.h = 40

    def draw(self, color):
        pygame.draw.rect(win, (color), (self.x, self.y, self.w, self.h))


pos = [x1, x2, x3, x4, x5]
pos1 = [x1 + 40, x2 + 40]  # x3 + 40, x4 + 40, x5 + 40]
ys = 100


class TankP():
    def __init__(self):
        self.x = 210
        self.y = 320
        self.x1 = 191
        self.y1 = 360
        self.x2 = 229
        self.y2 = 360
        self.pos = [self.x, self.y]
        self.pos1 = [self.x1, self.y1]
        self.pos2 = [self.x2, self.y2]
        self.q = [self.pos] + [self.pos1] + [self.pos2]
        self.vx = 0
        self.vx1 = 0
        self.vy = 0
        #self.angle = 0
        #self.rotated_point_x = 0
        #self.rotated_point_y = 0

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if self.vy <= 1.5:
                self.vy += 0.01
        elif keys[pygame.K_UP]:
            if self.vy >= -1.5:
                self.vy -= 0.01
        elif keys[pygame.K_LEFT]:
            self.vx = +1
            self.vx1 = -1
            print(1)
        elif self.vy <= 0:
            self.vy += 0.01
        elif self.vy >= 0:
            self.vy -= 0.01



    def draw(self):
        pygame.draw.lines(win, WHITE, True, self.q, 1)
        self.y += self.vy
        self.y1 += self.vy
        self.y2 += self.vy
        self.x += self.vx
        self.x += self.vx1
        self.pos[1] = self.y
        self.pos1[1] = self.y1
        self.pos2[1] = self.y2
        #self.y = self.rotated_point_y
        #self.x = self.rotated_point_x

#class Shell():
#    def __init__(self):
#        self.x = None
#        self.y = None
#        self.w = 15
#        self.h = 30
#
#    def control(self):
#
#
#    def draw(self,color):


class Base():
    def __init__(self, color):
        self.x = 190
        self.y = 360
        self.w = 40
        self.h = 40
        self.id = pygame.draw.rect(win, (color), (self.x, self.y, self.w, self.h))

    def draw(self):
        return self.id


boxes = []
#for i in range(100):
#    b = Box(YELLOW)
#    b.x = i * b.w * 1
#    b.y = i % 2 * b.h * 1
#    boxes.append(b)

t = TankP()
wh  ile z == 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    b = Box()
    b2 = Box2()
    #s = Shell()
    #s.draw(YELLOW)
    # w1 = Wall(RED)
    # w2 = Wall2(RED)
    base = Base(BLUE)
    t.control()
    #t.rotate()
    #for b in boxes:
    b.draw(YELLOW)
    b2.draw(YELLOW)
    t.draw()
    base.draw()
    pygame.display.update()
    time.sleep(0.01)
    win.fill(BLACK)
