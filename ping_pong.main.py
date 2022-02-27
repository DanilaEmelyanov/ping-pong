from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y,wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if key[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
class Player(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    '''def update_r(self):
        keys = key.get_pressed()
        if key[K_UP]:
            self.rect.y += self.speed
        if key[K_DOWN]:
            self.rect.y -= self.speed  '''    
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
racket1 = Player('racket.png', 50, 100, 5)
racket2 = Player('racket.png', 500, 100, 5)
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket1.update_l()
    racket2.reset()
    racket2.update_r()
    display.update()
    clock.tick(FPS)