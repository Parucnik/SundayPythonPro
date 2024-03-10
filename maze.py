from pygame import *

SCREEN_SIZE = (700, 500)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y  < SCREEN_SIZE[1]-self.rect.height: # 500-65
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed  
        if key_pressed[K_d] and self.rect.x < SCREEN_SIZE[0]-self.rect.width: # 700-65
            self.rect.x += self.speed   

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, end_x):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.end_x = end_x
        self.start_x = player_x
        self.direction = 'left' if end_x < player_x else 'right'
    
    def make_step(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x <= self.end_x:
                self.direction = 'right'
                self.start_x, self.end_x = self.end_x, self.start_x
        else:
            self.rect.x += self.speed
            if self.rect.x >= self.end_x:
                self.direction = 'left'
                self.start_x, self.end_x = self.end_x, self.start_x
            
class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color):           
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
walls = []

walls.append(Wall(150, 50, 400, 5, (17, 255, 0)))
walls.append(Wall(200, 50, 5, 350, (17, 255, 0)))
walls.append(Wall(280, 440, 300, 5, (17, 255, 0)))  
walls.append(Wall(350, 200, 5, 240, (17, 255, 0)))
walls.append(Wall(550, 50, 5, 200, (17, 255, 0)))
       
player = Player('hero.png', 20,20, 3)
cyborg = Enemy('cyborg.png', 600, 300, 3, 400)
gold = GameSprite('treasure.png', 600, 400, 3)
window = display.set_mode(SCREEN_SIZE)
display.set_caption('Лабиринт')

background = transform.scale(
    image.load('background.jpg'), SCREEN_SIZE
)

# ФОНОВАЯ МУЗЫКА
mixer.init()
mixer.music.load('lesnik.mp3')
mixer.music.set_volume(.03)
mixer.music.play()
finish = False
game = True
clock = time.Clock()

def show_text(text):
    font.init()
    font1 = font.SysFont('Arial', 40)
    text = font1.render(text, True, (255, 255, 255))
    window.blit(text, (250, 200))
    return True

while game:
    if finish == False:
        clock.tick(60)
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        cyborg.make_step()
        cyborg.reset()
        gold.reset()
        for w in walls:
            w.draw_wall()
            if sprite.collide_rect(player, w):
                finish = show_text('Вы проиграли')
                mixer.music.stop()
                kick = mixer.Sound('kick.ogg')
                kick.play()
        if sprite.collide_rect(player, gold):
            finish = show_text('Вы победили!!!')
        if sprite.collide_rect(player, cyborg):
            finish = show_text('Вы проиграли')              
            mixer.music.stop()
            kick = mixer.Sound('kick.ogg')
            kick.play()
        
        
        display.update()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        
    