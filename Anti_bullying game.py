import pygame
FPS = 60
HEIGHT = 600
WIDTH = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#遊戲視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("反霸凌遊戲")


#霸凌者
Player_width = 50
Player_height = 50
Player_color = (176, 224, 230)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Player_width, Player_height))
        self.image.fill(Player_color)
        self.rect = self.image.get_rect()
        self.rect.center = (Player_width, HEIGHT / 2)
        self.speedx = 5
        self.speedy = 5
        
    def update(self):
        #人物移動
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speedx

        if key[pygame.K_d]:
            self.rect.x += self.speedx

        if key[pygame.K_w]:
            self.rect.y -= self.speedy

        if key[pygame.K_s]:
            self.rect.y += self.speedy

        #判定人物是否超出視窗邊界
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#遊戲執行迴圈
clock = pygame.time.Clock()
playgame = True
while playgame:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playgame = False

    #更新遊戲
    all_sprites.update()

    #畫面顯示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()
print("hello world")