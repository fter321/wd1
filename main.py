import pygame
import random

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('Угадай число')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

cat = pygame.image.load('Image/cat.png')
cat_rect = cat.get_rect(center=(70,220))

dog = pygame.image.load('Image/dog.png')
dog_rect = dog.get_rect(center=(410,220))

owl = pygame.image.load('Image/room.png')
owl_rect = owl.get_rect(center=(210,120))

bg = pygame.image.load('Image/room.png')
bg_rect = bg.get_rect(topleft=(0,0))

dialog = pygame.image.load('Image/room.png')
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x, dog_rect.w // 2, dog_rect.y - dialog_rect.h)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    screen.blit(bg, bg_rect)
    pygame.display.update()

    screen.blit(bg, gb_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, wol_rect)
    