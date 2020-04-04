import pygame
import sys

BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (200, 200, 200)
pygame.init()
pygame.display.set_caption("生命游戏，按空格演化")
screen = pygame.display.set_mode((500, 500))
icon = pygame.image.load("1234.png")
pygame.display.set_icon(icon)


def init_screen():
    screen.fill(WHITE)
    for i in range(50):
        pygame.draw.line(screen, GRAY, (i*10, 0), (i*10, 500))
        pygame.draw.line(screen, GRAY, (0, i*10), (500, i*10))
    pygame.display.update()
def kin_count(x,y):
    count=0
    kins=[(x-10,y-10),(x-10,y),(x-10,y+10),(x,y-10),(x,y+10),(x+10,y-10),(x+10,y),(x+10,y+10)]
    kins=[(x,y) for x,y in kins if 0<x<500 and 0<y<500]
    for kin in kins:
        if screen.get_at(kin)==BLACK:
            count=count+1
    return count



init_screen()
cells =[]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            if screen.get_at(event.pos)==WHITE:
                x,y=event.pos
                cellx,celly=x-x%10,y-y%10
                cell=pygame.Rect(cellx,celly,10,10)
                pygame.draw.rect(screen,BLACK,cell)
                cells.append((cellx,celly))
                pygame.display.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                clock=pygame.time.Clock()
                clock.tick(10)
                turn=0
                while len(cells)>0:
                    turn=turn+1
                    pygame.display.set_caption("生命游戏第%s轮" % turn)
                    for x in range(5,500,10):
                        for y in range(5,500,10):
                            if screen.get_at((x,y))==BLACK:
                              if kin_count(x,y) not in [2,3]:
                                  cells.remove((x-5,y-5))
                            else:
                              if kin_count(x,y)==3:
                                  cells.append((x-5,y-5))
                    init_screen()
                    for cellx,celly in cells:
                        cell=pygame.Rect(cellx,celly,10,10)
                        pygame.draw.rect(screen, BLACK, cell)
                    pygame.display.update()
                    break




