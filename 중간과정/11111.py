import pygame
import sys
import threading

pygame.init()   # 초기화

#화면 크기
screen_width = 560  # 가로
screen_height = 540 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

tile_size = 20


class GameBoard():
    width = 10  # 너비
    height = 20 # 높이
    gameboard = [[0]*width]*height  # 너비*높이 배열 생성
    
    def __init__(self, world):
        self.I_mino = Mino(I_data)
        self.O_mino = Mino(O_data)
        self.Z_mino = Mino(Z_data)
        self.S_mino = Mino(S_data)
        self.J_mino = Mino(J_data)
        self.L_mino = Mino(L_data)
        self.T_mino = Mino(T_data)

        # [y][x]: [3][4] ~ [22][13]

    def draw(self):
        self.I_mino.update()
        self.O_mino.update()

class Mino():
    """Mino Class"""
    def __init__(self, data):
        if data == O_data:
            O_img = pygame.image.load('img/O_mino.png')
            self.image = pygame.transform.scale(O_img, (tile_size*2, tile_size*2))
            self.rect = self.image.get_rect()
            self.rect.x = tile_size * 9
            self.rect.y = tile_size * 3

        if data == I_data:
            I_img = pygame.image.load('img/I_mino.png')
            self.image = pygame.transform.scale(I_img, (tile_size, tile_size*4))    # 가로 20, 세로 80
            self.rect = self.image.get_rect()
            self.rect.x = tile_size * 9
            self.rect.y = tile_size * 3

    def update(self):
        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect.x - tile_size != tile_size * 3:    # 왼쪽에 있는 좌표가 [3]이 아니면
                self.rect.x = self.rect.x - tile_size       # 왼쪽으로 이동
                pygame.time.delay(100)

        if key[pygame.K_RIGHT]:
            if self.rect.x + tile_size != tile_size * 14:   # 오른쪽에 있는 좌표가 [14]가 아니면
                self.rect.x = self.rect.x + tile_size       # 오른쪽으로 이동
                pygame.time.delay(100)
        
        # draw mino
        screen.blit(self.image, self.rect)

    def down(self):
        # down
        if self.rect.y != tile_size*22:
            self.rect.y = self.rect.y + tile_size
            return True
        else:
            return False
        
        # draw mino
        screen.blit(self.image, self.rect)

I_data = [
[1],
[1],
[1],
[1]
]

O_data = [
[1, 1],
[1, 1]
]

Z_data = [
[1, 1, 0],
[0, 1, 1]
]

S_data = [
[0, 1, 1],
[1, 1, 0]
]

J_data = [
[0, 1],
[0, 1],
[1, 1]
]

L_data = [
[1, 0],
[1, 0],
[1, 1]
]

T_data = [
[1, 1, 1],
[0, 1, 0]
]


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

        # if down:
        #     down = Mino.down()
        # else:
        #     # 새 미노 생성, 한 줄이 채워지면 없애고, 점수up
        #     down = True
        
        pygame.display.update()


    


if __name__ == "__main__":
    start_game()