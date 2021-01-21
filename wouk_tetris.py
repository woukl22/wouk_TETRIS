import pygame
import sys
import threading
import random

pygame.init()   # 초기화

#화면 크기

screen_width = 560  # 가로
screen_height = 540 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont('배달의민족 주아', 25)
tile_size = 20

class GameBoard():
    def __init__(self, world):
        width = 18  # 너비 4 + 10 + 4
        height = 24 # 높이 3 + 20 + 1
        self.gameboard = [[0 for _ in range(width)] for _ in range(height)]
        self.down = False
        self.x_1, self.x_2, self.x_3, self.x_4 = 0, 0, 0, 0
        self.y_1, self.y_2, self.y_3, self.y_4 = 0, 0, 0, 0
        self.r = 0
        self.Mino = Mino('')
        self.rect = self.Mino.image.get_rect()
        self.full = False
        self.count = 0
        self.rd = random.randint(1, 7)
        self.score = 0
        
        self.I_img = pygame.transform.scale(pygame.image.load('img/I_mino.png'), (tile_size, tile_size))
        self.O_img = pygame.transform.scale(pygame.image.load('img/O_mino.png'), (tile_size, tile_size))
        self.Z_img = pygame.transform.scale(pygame.image.load('img/Z_mino.png'), (tile_size, tile_size))
        self.S_img = pygame.transform.scale(pygame.image.load('img/S_mino.png'), (tile_size, tile_size))
        self.J_img = pygame.transform.scale(pygame.image.load('img/J_mino.png'), (tile_size, tile_size))
        self.L_img = pygame.transform.scale(pygame.image.load('img/L_mino.png'), (tile_size, tile_size))
        self.T_img = pygame.transform.scale(pygame.image.load('img/T_mino.png'), (tile_size, tile_size))
        
        
    def draw(self):
        if self.check_gameover() == False:
            return False
        else:
            if self.down == False:
                self.x_1, self.x_2, self.x_3, self.x_4 = int(self.Mino.rect_1.x/tile_size), int(self.Mino.rect_2.x/tile_size), int(self.Mino.rect_3.x/tile_size), int(self.Mino.rect_4.x/tile_size)
                self.y_1, self.y_2, self.y_3, self.y_4 = int(self.Mino.rect_1.y/tile_size), int(self.Mino.rect_2.y/tile_size), int(self.Mino.rect_3.y/tile_size), int(self.Mino.rect_4.y/tile_size)
                self.stack()
                self.r = self.rd
                self.rd = random.randint(1, 7)
                if self.r == 1:
                    self.Mino = Mino('I')
                elif self.r == 2:
                    self.Mino = Mino('O')
                elif self.r == 3:
                    self.Mino = Mino('Z')
                elif self.r == 4:
                    self.Mino = Mino('S')
                elif self.r == 5:
                    self.Mino = Mino('J')
                elif self.r == 6:
                    self.Mino = Mino('L')
                elif self.r == 7:
                    self.Mino = Mino('T')
                self.down = self.Mino.update(self.gameboard)
            else:
                self.down = self.Mino.update(self.gameboard)
            self.show_next()
            self.show_score()

    def stack(self):
        '''바닥에 닿으면 위치 표시'''
        self.gameboard[self.y_1][self.x_1] = self.r
        self.gameboard[self.y_2][self.x_2] = self.r
        self.gameboard[self.y_3][self.x_3] = self.r
        self.gameboard[self.y_4][self.x_4] = self.r

        self.board_list = []
        # for i in self.gameboard:
        #     print(i)
        # print('')

        self.erase_line()

        '''바닥에 닿으면 색칠'''
        row_count = 0
        for row in self.gameboard:
            col_count = 0
            for col in row:
                if col == 1:
                    rect = self.I_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.I_img, rect))
                elif col == 2:
                    rect = self.O_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.O_img, rect))
                elif col == 3:
                    rect = self.Z_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.Z_img, rect))
                elif col == 4:
                    rect = self.S_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.S_img, rect))
                elif col == 5:
                    rect = self.J_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.J_img, rect))
                elif col == 6:
                    rect = self.L_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.L_img, rect))
                elif col == 7:
                    rect = self.T_img.get_rect()
                    rect.x, rect.y = col_count*tile_size, row_count*tile_size
                    self.board_list.append((self.T_img, rect))
                col_count += 1
            row_count += 1
        

    def erase_line(self):
        '''한 줄 채워지면 지우기'''
        line = 0
        zerolist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for board in self.gameboard:
            for count in board:
                if count != 0:
                    self.count += 1
                    if self.count == 10:
                        self.score += 100
                        for i in range(line, 0, -1):
                            self.gameboard[i] = self.gameboard[i-1]
                        self.gameboard[0] = zerolist
            self.count = 0
            line += 1

    def show_next(self):
        if self.rd == 1:
            image = self.I_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 21, tile_size * 6
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 7
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 8
            rect_4.x, rect_4.y = tile_size * 21, tile_size * 9
        
        elif self.rd == 2:
            image = self.O_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 21, tile_size * 7
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 8
            rect_3.x, rect_3.y = tile_size * 20, tile_size * 7
            rect_4.x, rect_4.y = tile_size * 20, tile_size * 8

        elif self.rd == 3:
            image = self.Z_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 20, tile_size * 7
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 7
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 8
            rect_4.x, rect_4.y = tile_size * 22, tile_size * 8

        elif self.rd == 4:
            image = self.S_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 20, tile_size * 8
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 8
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 7
            rect_4.x, rect_4.y = tile_size * 22, tile_size * 7
            
        elif self.rd == 5:
            image = self.J_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 20, tile_size * 9
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 7
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 8
            rect_4.x, rect_4.y = tile_size * 21, tile_size * 9

        elif self.rd == 6:
            image = self.L_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 21, tile_size * 9
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 7
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 8
            rect_4.x, rect_4.y = tile_size * 22, tile_size * 9

        elif self.rd == 7:
            image = self.T_img
            rect_1, rect_2, rect_3, rect_4 = image.get_rect(), image.get_rect(), image.get_rect(), image.get_rect()
            rect_1.x, rect_1.y = tile_size * 20, tile_size * 8
            rect_2.x, rect_2.y = tile_size * 21, tile_size * 8
            rect_3.x, rect_3.y = tile_size * 21, tile_size * 9
            rect_4.x, rect_4.y = tile_size * 22, tile_size * 8

        screen.blit(image, rect_1)
        screen.blit(image, rect_2)
        screen.blit(image, rect_3)
        screen.blit(image, rect_4)
        pygame.draw.rect(screen, (255, 255, 255), rect_1, 3)
        pygame.draw.rect(screen, (255, 255, 255), rect_2, 3)
        pygame.draw.rect(screen, (255, 255, 255), rect_3, 3)
        pygame.draw.rect(screen, (255, 255, 255), rect_4, 3)

    def check_gameover(self):
        for i in self.gameboard[3]:
            if i != 0:
                return False
        return True
    
    def show_score(self):
        score = font.render(str(self.score), True, (0, 0, 0))
        screen.blit(score, (19*tile_size, 17*tile_size))

    def show(self):
        for i in self.board_list:
            screen.blit(i[0], i[1])
            pygame.draw.rect(screen, (255, 255, 255), i[1], 3)



class Mino():
    """Mino Class"""
    def __init__(self, shape):
        self.shape = shape
        self.I_rotate = 0
        self.Z_rotate = 0
        self.S_rotate = 0
        self.J_rotate = 0
        self.L_rotate = 0
        self.T_rotate = 0

        if self.shape == 'I':
            self.image = pygame.transform.scale(pygame.image.load('img/I_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 9, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 4
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 5
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 6
        
        if self.shape == 'O':
            self.image = pygame.transform.scale(pygame.image.load('img/O_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 4
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 8, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if self.shape == 'Z':
            self.image = pygame.transform.scale(pygame.image.load('img/Z_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 4
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if self.shape == 'S':
            self.image = pygame.transform.scale(pygame.image.load('img/S_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 4
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4

        if self.shape == 'J':
            self.image = pygame.transform.scale(pygame.image.load('img/J_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 5
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 4
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 5

        if self.shape == 'L':
            self.image = pygame.transform.scale(pygame.image.load('img/L_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 9, tile_size * 5
            self.rect_3.x, self.rect_3.y = tile_size * 8, tile_size * 4
            self.rect_4.x, self.rect_4.y = tile_size * 8, tile_size * 5

        if self.shape == 'T':
            self.image = pygame.transform.scale(pygame.image.load('img/T_mino.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = tile_size * 8, tile_size * 3
            self.rect_2.x, self.rect_2.y = tile_size * 10, tile_size * 3
            self.rect_3.x, self.rect_3.y = tile_size * 9, tile_size * 3
            self.rect_4.x, self.rect_4.y = tile_size * 9, tile_size * 4
        
        if self.shape == '':
            self.image = pygame.transform.scale(pygame.image.load('img/background.png'), (tile_size, tile_size))
            self.rect_1, self.rect_2, self.rect_3, self.rect_4 = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
            self.rect_1.x, self.rect_1.y = 0, 0
            self.rect_2.x, self.rect_2.y = 0, 0
            self.rect_3.x, self.rect_3.y = 0, 0
            self.rect_4.x, self.rect_4.y = 0, 0

    def update(self, board):
        # get keypresses
        key = pygame.key.get_pressed()

        # 좌우 이동
        if key[pygame.K_LEFT]:
            if self.rect_1.x - tile_size != tile_size * 3:    # 왼쪽에 있는 좌표가 [3]이 아니면
                if board[int(self.rect_1.y/tile_size)][int((self.rect_1.x - tile_size)/tile_size)] < 1 and board[int(self.rect_2.y/tile_size)][int((self.rect_2.x - tile_size)/tile_size)] < 1 and board[int(self.rect_3.y/tile_size)][int((self.rect_3.x - tile_size)/tile_size)] < 1 and board[int(self.rect_4.y/tile_size)][int((self.rect_4.x - tile_size)/tile_size)] < 1:
                    self.rect_1.x = self.rect_1.x - tile_size
                    self.rect_2.x = self.rect_2.x - tile_size
                    self.rect_3.x = self.rect_3.x - tile_size
                    self.rect_4.x = self.rect_4.x - tile_size
                    pygame.time.delay(100)

        if key[pygame.K_RIGHT]:
            if self.rect_2.x + tile_size != tile_size * 14:   # 오른쪽에 있는 좌표가 [14]가 아니면
                if board[int(self.rect_1.y/tile_size)][int((self.rect_1.x + tile_size)/tile_size)] < 1 and board[int(self.rect_2.y/tile_size)][int((self.rect_2.x + tile_size)/tile_size)] < 1 and board[int(self.rect_3.y/tile_size)][int((self.rect_3.x + tile_size)/tile_size)] < 1 and board[int(self.rect_4.y/tile_size)][int((self.rect_4.x + tile_size)/tile_size)] < 1:
                    self.rect_1.x = self.rect_1.x + tile_size
                    self.rect_2.x = self.rect_2.x + tile_size
                    self.rect_3.x = self.rect_3.x + tile_size
                    self.rect_4.x = self.rect_4.x + tile_size
                    pygame.time.delay(100)
        
        # 회전
        if key[pygame.K_UP]:
            self.rotate()

        # 드롭
        if key[pygame.K_DOWN]:
            self.down(board)

        # 이탈 확인
        if self.rect_1.x <= tile_size * 3 or self.rect_2.x <= tile_size * 3 or self.rect_3.x <= tile_size * 3 or self.rect_4.x <= tile_size * 3:    # 왼쪽
            self.rect_1.x = self.rect_1.x + tile_size
            self.rect_2.x = self.rect_2.x + tile_size
            self.rect_3.x = self.rect_3.x + tile_size
            self.rect_4.x = self.rect_4.x + tile_size
        
        if self.rect_1.x >= tile_size * 14 or self.rect_2.x >= tile_size * 14 or self.rect_3.x >= tile_size * 14 or self.rect_4.x >= tile_size * 14:    # 오른쪽
            self.rect_1.x = self.rect_1.x - tile_size
            self.rect_2.x = self.rect_2.x - tile_size
            self.rect_3.x = self.rect_3.x - tile_size
            self.rect_4.x = self.rect_4.x - tile_size

        # draw mino
        screen.blit(self.image, self.rect_1)
        screen.blit(self.image, self.rect_2)
        screen.blit(self.image, self.rect_3)
        screen.blit(self.image, self.rect_4)
        pygame.draw.rect(screen, (255, 255, 255), self.rect_1, 3)
        pygame.draw.rect(screen, (255, 255, 255), self.rect_2, 3)
        pygame.draw.rect(screen, (255, 255, 255), self.rect_3, 3)
        pygame.draw.rect(screen, (255, 255, 255), self.rect_4, 3)

        return self.down(board)

    # 회전
    def rotate(self):
        if self.shape == 'I':
            pygame.time.delay(100)
            if self.I_rotate == 0:
                self.rect_1.x, self.rect_1.y = self.rect_1.x - 2*tile_size, self.rect_1.y + 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y + tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y - tile_size
                self.I_rotate = 1
            elif self.I_rotate == 1:
                self.rect_1.x, self.rect_1.y = self.rect_1.x + 2*tile_size, self.rect_1.y - 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y - tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y + tile_size
                self.I_rotate = 0
            
        if self.shape == 'Z':
            pygame.time.delay(100)
            if self.Z_rotate == 0:
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y - 2*tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x - tile_size, self.rect_4.y
                self.Z_rotate = 1

            elif self.Z_rotate == 1:
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y + 2*tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x + tile_size, self.rect_4.y
                self.Z_rotate = 0
            
        if self.shape == 'S':
            pygame.time.delay(100)
            if self.S_rotate == 0:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y - tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y + tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y + tile_size
                self.S_rotate = 1
            
            elif self.S_rotate == 1:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y + tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y - tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y - tile_size
                self.S_rotate = 0

        if self.shape == 'J':
            pygame.time.delay(100)
            if self.J_rotate == 0:
                self.rect_1.x, self.rect_1.y = self.rect_1.x - tile_size, self.rect_1.y - tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y + 2*tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x - 2*tile_size, self.rect_4.y
                self.J_rotate = 1
            
            elif self.J_rotate == 1:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y - tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y - 2*tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y
                self.J_rotate = 2
            
            elif self.J_rotate == 2:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x + 2*tile_size, self.rect_4.y - tile_size
                self.J_rotate = 3
            
            elif self.J_rotate == 3:
                self.rect_1.x, self.rect_1.y = self.rect_1.x + tile_size, self.rect_1.y + 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y + tile_size
                self.J_rotate = 0
                

        if self.shape == 'L':
            pygame.time.delay(100)
            if self.L_rotate == 0:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y - 2*tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y - tile_size
                self.L_rotate = 1
            
            elif self.L_rotate == 1:
                self.rect_1.x, self.rect_1.y = self.rect_1.x + tile_size, self.rect_1.y
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x + 2*tile_size, self.rect_4.y + tile_size
                self.L_rotate = 2

            elif self.L_rotate == 2:
                self.rect_1.x, self.rect_1.y = self.rect_1.x - tile_size, self.rect_1.y + 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y + tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x, self.rect_4.y
                self.L_rotate = 3
            
            elif self.L_rotate == 3:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y - 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y + tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x - 2*tile_size, self.rect_4.y
                self.L_rotate = 0

        if self.shape == 'T':
            pygame.time.delay(100)
            if self.T_rotate == 0:
                self.rect_1.x, self.rect_1.y = self.rect_1.x + tile_size, self.rect_1.y + tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y + tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x + tile_size, self.rect_4.y + tile_size
                self.T_rotate = 1
            
            elif self.T_rotate == 1:
                self.rect_1.x, self.rect_1.y = self.rect_1.x - tile_size, self.rect_1.y + tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x, self.rect_2.y + 2*tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y
                self.rect_4.x, self.rect_4.y = self.rect_4.x - tile_size, self.rect_4.y
                self.T_rotate = 2
            
            elif self.T_rotate == 2:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y - 2*tile_size
                self.rect_2.x, self.rect_2.y = self.rect_2.x - tile_size, self.rect_2.y - tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x - tile_size, self.rect_3.y
                self.rect_4.x, self.rect_4.y = self.rect_4.x - tile_size, self.rect_4.y
                self.T_rotate = 3
            
            elif self.T_rotate == 3:
                self.rect_1.x, self.rect_1.y = self.rect_1.x, self.rect_1.y
                self.rect_2.x, self.rect_2.y = self.rect_2.x + tile_size, self.rect_2.y - tile_size
                self.rect_3.x, self.rect_3.y = self.rect_3.x + tile_size, self.rect_3.y - tile_size
                self.rect_4.x, self.rect_4.y = self.rect_4.x + tile_size, self.rect_4.y - tile_size
                self.T_rotate = 0
            

    def down(self, board):
        # down
        if self.rect_4.y <= tile_size*22:
            if board[int((self.rect_1.y+tile_size)/tile_size)][int(self.rect_1.x/tile_size)] >= 1 or board[int((self.rect_2.y+tile_size)/tile_size)][int(self.rect_2.x/tile_size)] >= 1 or board[int((self.rect_3.y+tile_size)/tile_size)][int(self.rect_3.x/tile_size)] >= 1 or board[int((self.rect_4.y+tile_size)/tile_size)][int(self.rect_4.x/tile_size)] >= 1:
                return False
            else:
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

        # 배경 색칠
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
#0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
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
    gameover_img = pygame.image.load('img/gameover.png')
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
        if GB.draw() == False:
            screen.blit(gameover_img, (1, 1))
            score = font.render("Score: " + str(GB.score), True, (255, 255, 255))
            screen.blit(score, (18*tile_size, 17*tile_size))
        GB.show()
        pygame.display.update()

if __name__ == "__main__":
    start_game()