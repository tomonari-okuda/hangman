import sys
import random
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        pointlist = []
        for _ in range(5):
            xpos = random.randint(0, 300)
            ypos = random.randint(0, 300)
            pointlist.append((xpos, ypos))

        pygame.draw.lines(SURFACE, (255, 0, 0), True, pointlist, 10)

        pointlist2 = []
        for _ in range(6):
            xpos2 = random.randint(301, 600)
            ypos2 = random.randint(0, 300)
            pointlist2.append((xpos2, ypos2))
        pygame.draw.lines(SURFACE, (0, 255, 0), True, pointlist2, 10)

        pointlist3 = []
        for _ in range(4):
            xpos3 = random.randint(301, 600)
            ypos3 = random.randint(301, 600)
            pointlist3.append((xpos3, ypos3))
        pygame.draw.lines(SURFACE, (0, 0, 255), True, pointlist3, 5)

        pointlist4 = []
        for _ in range(8):
            xpos4 = random.randint(0,300)
            ypos4 = random.randint(301, 600)
            pointlist4.append((xpos4, ypos4))
        pygame.draw.lines(SURFACE, (200, 200, 0), True, pointlist4, 20)
        
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
