import pygame
import sys
import threading
import random

pygame.init()   # 초기화

#화면 크기
screen_width = 560  # 가로
screen_height = 540 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

tile_size = 20


class GameBoard():   
    def __init__(self, world):
        width = 10  # 너비
        height = 20 # 높이
        self.gameboard = [[0]*width]*height  # 너비*높이 배열 생성
        self.down = False
        self.x_1, self.x_2, self.x_3, self.x_4 = 0, 0, 0, 0
        self.y_1, self.y_2, self.y_3, self.y_4 = 0, 0, 0, 0
        self.Mino = Mino('')
        self.image = pygame.transform.scale(pygame.image.load('img/blank.png'), (width*tile_size, height*tile_size))
        self.r = 0

    def draw(self):
        if self.down == False:
            self.x_1, self.x_2, self.x_3, self.x_4 = int(self.Mino.rect_1.x/tile_size)-4, int(self.Mino.rect_2.x/tile_size)-4, int(self.Mino.rect_3.x/tile_size)-4, int(self.Mino.rect_4.x/tile_size)-4
            self.y_1, self.y_2, self.y_3, self.y_4 = int(self.Mino.rect_1.y/tile_size)-3, int(self.Mino.rect_2.y/tile_size)-3, int(self.Mino.rect_3.y/tile_size)-3, int(self.Mino.rect_4.y/tile_size)-3
            self.stack()
            self.r = random.randint(0, 6)
            if self.r == 0:
                self.Mino = Mino('I')
            elif self.r == 1:
                self.Mino = Mino('O')
            elif self.r == 2:
                self.Mino = Mino('Z')
            elif self.r == 3:
                self.Mino = Mino('S')
            elif self.r == 4:
                self.Mino = Mino('J')
            elif self.r == 5:
                self.Mino = Mino('L')
            elif self.r == 6:
                self.Mino = Mino('T')
            self.down = self.Mino.update()
        else:
            self.down = self.Mino.update()

    def stack(self):
        self.gameboard[self.y_1][self.x_1] = self.r
        self.gameboard[self.y_2][self.x_2] = self.r
        self.gameboard[self.y_3][self.x_3] = self.r
        self.gameboard[self.y_4][self.x_4] = self.r
        
        row_count = 0
        for row in self.gameboard:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.img_rect = self.image.get_rect()
                    self.img_rect.x = col_count * tile_size
                    self.img_rect.y = row_count * tile_size

                if tile == 0 or tile == 2 or tile == 3:
                    self.img_rect = self.image.get_rect()
                    self.img_rect.x = col_count * tile_size
                    self.img_rect.y = row_count * tile_size
                col_count += 1
            row_count += 1

    def show(self):
        # screen.blit(self.image, (80, 60))
        pass
    
    # def stack(self):
    #     rect_1, rect_2, rect_3, rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
    #     rect_1.x, rect_1.y = self.x_1, self.y_1
    #     rect_2.x, rect_2.y = self.x_2, self.y_2
    #     rect_3.x, rect_3.y = self.x_3, self.y_3
    #     rect_4.x, rect_4.y = self.x_4, self.y_4
    #     screen.blit(self.image, rect_1)
    #     screen.blit(self.image, rect_2)
    #     screen.blit(self.image, rect_3)
    #     screen.blit(self.image, rect_4)

        # [y][x]: [3][4] ~ [22][13]

class Mino():
    """Mino Class"""
    def __init__(self, shape):
        if shape == 'I':
            self.img = pygame.image.load('img/I_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 9, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 4
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 5
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 6
        
        if shape == 'O':
            self.img = pygame.image.load('img/O_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 4
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 8, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if shape == 'Z':
            self.img = pygame.image.load('img/Z_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 4
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if shape == 'S':
            self.img = pygame.image.load('img/S_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 4
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if shape == 'J':
            self.img = pygame.image.load('img/J_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 5
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 4
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 5

        if shape == 'L':
            self.img = pygame.image.load('img/L_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 5
            self.rect_3.x, self.rect_3.y = tile_size * 8, tile_size * 4
            self.rect_4.x, self.rect_4.y = tile_size * 8, tile_size * 5

        if shape == 'T':
            self.img = pygame.image.load('img/T_mino.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4
        
        if shape == '':
            self.img = pygame.image.load('img/background.png')
            self.image = pygame.transform.scale(self.img, (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = 0, 0
            self.rect_2.x, self.rect_2.y = 0, 0
            self.rect_3.x, self.rect_3.y = 0, 0
            self.rect_4.x, self.rect_4.y = 0, 0

    def update(self):
        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect_1.x - tile_size != tile_size * 3:    # 왼쪽에 있는 좌표가 [3]이 아니면
                self.rect_1.x = self.rect_1.x - tile_size
                self.rect_2.x = self.rect_2.x - tile_size
                self.rect_3.x = self.rect_3.x - tile_size
                self.rect_4.x = self.rect_4.x - tile_size
                pygame.time.delay(100)

        if key[pygame.K_RIGHT]:
            if self.rect_2.x + tile_size != tile_size * 14:   # 오른쪽에 있는 좌표가 [14]가 아니면
                self.rect_1.x = self.rect_1.x + tile_size
                self.rect_2.x = self.rect_2.x + tile_size
                self.rect_3.x = self.rect_3.x + tile_size
                self.rect_4.x = self.rect_4.x + tile_size
                pygame.time.delay(100)
        
        # draw mino
        screen.blit(self.image, self.rect_1)
        screen.blit(self.image, self.rect_2)
        screen.blit(self.image, self.rect_3)
        screen.blit(self.image, self.rect_4)

        return self.down()

    def down(self):
        # down
        if self.rect_4.y <= tile_size*22:
            self.rect_1.y = self.rect_1.y + 3
            self.rect_2.y = self.rect_2.y + 3
            self.rect_3.y = self.rect_3.y + 3
            self.rect_4.y = self.rect_4.y + 3
            return True
        else:
            return False

##################################################################################################################

class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        background_img = pygame.image.load('img/background.png')
        wall_img = pygame.image.load('img/wall.png')
        blank_img = pygame.image.load('img/blank.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =  (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 0 or tile == 2 or tile == 3:
                    img = pygame.transform.scale(blank_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =  (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 3)       # pygame.draw.rect(Surface, Color, Rect, Width)

# 28x27
world_data = [
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 1
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 2
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 3
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 4
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 5
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 6
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 2, 2, 2, 2, 2, 1, 9, 9, 9],   # 7
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 2, 2, 2, 2, 2, 1, 9, 9, 9],   # 8
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 2, 2, 2, 2, 2, 1, 9, 9, 9],   # 9
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 2, 2, 2, 2, 2, 1, 9, 9, 9],   # 10
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 2, 2, 2, 2, 2, 1, 9, 9, 9],   # 11
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9],   # 12
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 13
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 14
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 15
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 16
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9],   # 17
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 3, 3, 3, 3, 3, 1, 9, 9, 9],   # 18
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9],   # 19
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 20
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 21
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 22
[9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 23
[9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 24
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 25
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],   # 26
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]    # 27
]

world = World(world_data)
GB = GameBoard(world_data)

def start_game():
    # 화면 타이틀
    pygame.display.set_caption("Wouk_TETRIS")

    # fps
    clock = pygame.time.Clock()
    fps = 60

    # 변수
    background_img = pygame.image.load('img/background.png')
    down = True

    # 이벤트 루프
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame 종료
                pygame.quit()
                sys.exit()

        screen.blit(background_img, (0, 0))
        world.draw()
        GB.draw()
        GB.show()
        pygame.display.update()


    


if __name__ == "__main__":
    start_game()