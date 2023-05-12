import pygame
def kresli():
    screen.fill((0, 0, 0))
    for i in range(len(labyrint)):
        for j in range(len(labyrint[i])):
            if labyrint[i][j] == "#":
                pygame.draw.rect(screen,(255, 255, 50), pygame.Rect(j * 20,i * 20,20,20))
    pygame.draw.circle(screen, (0,0,255), (panak[0]*20+10,panak[1]*20+10), 10)
    pygame.display.flip()
panak = [1,1]
pygame.init()
screen = pygame.display.set_mode((700, 220))
f = open("labyrint.txt", "r")
labyrint = f.read().split("\n")
koniec = False
cas = pygame.time.Clock()
while not koniec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: koniec = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if labyrint[panak[1]][panak[0]+1]=="#":print("au")
            else: panak[0] += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if labyrint[panak[1]][panak[0] - 1] == "#":
                print("au")
            else:
                panak[0] -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if labyrint[panak[1]-1][panak[0]] == "#":
                print("au")
            else:
                panak[1] -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if labyrint[panak[1]+1][panak[0]] == "#":
                print("au")
            else:
                panak[1] += 1
    kresli()