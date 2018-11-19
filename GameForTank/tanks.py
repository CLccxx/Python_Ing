# 坦克模块
import pygame

# 我方坦克（是否存活，）
class myTank(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)

        if player == 1:
            self.tank = ["./images/myTank/tank_T1_0.png", "./images/myTank/tank_T1_1.png", "./images/myTank/tank_T1_2.png"]
        elif player == 2:
            self.tank = []

        self.level = 0
        self.tank = pygame.image.load()

# 敌方坦克