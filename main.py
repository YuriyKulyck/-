import pygame

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

layout = pygame.image.load("background.png")
layout = pygame.transform.scale(layout, (800, 500))

topic1 = pygame.image.load("sprite1.png")
topic1 = pygame.transform.scale(topic1, (75, 70))

topic2 = pygame.image.load("sprite2.png")
topic2 = pygame.transform.scale(topic2, (75, 70))

x1, y1 = 50, 50
x2, y2 = 650, 350
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x1 += 3
    if keys[pygame.K_a]:
        x1 -= 3
    if keys[pygame.K_w]:
        y1 -= 4
    if keys[pygame.K_s]:
        y1 += 4
    if keys[pygame.K_LEFT]:
        x2 -= 5
    if keys[pygame.K_RIGHT]:
        x2 += 5
    if keys[pygame.K_UP]:
        y2 -= 6
    if keys[pygame.K_DOWN]:
        y2 += 6
    window.blit(layout, [0, 0])
    window.blit(topic1, [x1, y1])
    window.blit(topic2, [x2, y2])
    pygame.display.flip()
    fps.tick(90)