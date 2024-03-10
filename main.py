from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')

background = transform.scale(
    image.load('background.png'), (700, 500)
)

sprite1 = transform.scale (image.load('sprite1.png'), (100,100))
x1, y1 = 0, 0
# 1 - создание   (sprite2.png и другие координаты)
sprite2 = transform.scale (image.load('sprite2.png'), (100,100))
x2, y2 = 0, 0

# 3 - сделать управление с помощью wasd K_s,K_w,K_a, K_d

game = True
clock = time.Clock()

while game:
    clock.tick(60)
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))# 2 - отобразить
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    dict_keys = key.get_pressed()
    if dict_keys[K_DOWN] and y1 < 400:
        y1 += 5
    if dict_keys[K_UP] and y1 > 0:
        y1 -= 5
    if dict_keys[K_RIGHT] and x1 < 600:
        x1 += 5
    if dict_keys[K_LEFT] and x1 > 0:
        x1 -= 5
    
    if dict_keys[K_s] and y2 < 400:
        y2 += 5
    if dict_keys[K_w] and y2 > 0:
        y2 -= 5
    if dict_keys[K_d] and x2 < 600:
        x2 += 5
    if dict_keys[K_a] and x2 > 0:
        x2 -= 5
    display.update()