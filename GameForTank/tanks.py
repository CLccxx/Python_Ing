# 坦克模块
import pygame

# 我方坦克（是否存活，）
class myTank(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)

        self.player = player
        if self.player == 1:
            self.tanks = ["./images/myTank/tank_T1_0.png", "./images/myTank/tank_T1_1.png", "./images/myTank/tank_T1_2.png"]
        elif self.player == 2:
            self.tanks = ["./images/myTank/tank_T2_0.png", "./images/myTank/tank_T2_1.png", "./images/myTank/tank_T2_2.png"]
        else:
            raise ValueError("myTank class -> player value error")

        # 初始坦克等级
        self.level = 0
        # 载入坦克素材
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()

        # 默认坦克向前方
        self.tank_0 = self.tank.subsurface((0,0),(48,48))
        self.tank_1 = self.tank.subsurface((48,0),(48,48))
        self.rect = self.tank_0.get_rect()

        # 不同玩家的出生位置不同
        if self.player == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        elif self.player == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24

        # 保护罩
        self.protected_mask = pygame.image.load("./images/others/protect.png").convert_alpha()
        self.protected_mask1 = self.protected_mask.subsurface((0,0),(48,48))
        self.protected_mask2 = self.protected_mask.subsurface((48,0),(48,48))

        # 坦克前进方向: 默认朝上
        self.direction_x, self.direction_y = 0, -1

        # 坦克的速度
        self.speed = 1

        # 是否存活
        self.being = True

        # 有几条命
        self.life = 3

        # 是否处于保护状态
        self.protected = False

        # 子弹
        # //////////

    # 等级提升
    def up_level(self):
        if self.level < 3:
            self.level += 1
        try:
            self.tank = pygame.image.load(self.tanks[self.level]).convert.alpha()
        except:
            self.tank = pygame.image.load(self.tanks[-1]).convert.alpha()

    def down_level(self):
        if self.level > 0:
            self.level -= 1
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()

    # 向上移动
    def move_up(self, brickGroup, ironGroup, myHome):
        self.direction_x, self.direction_y = 0, -1
        # 移动
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0,0),(48,48))
        self.tank_1 = self.tank.subsurface((48,0),(48,48))
        is_Move = True

        # 判断是否可以移动
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        # 撞其他坦克
        # ///////TODO: 撞其他坦克

        # 大本营
        if pygame.sprite.collide_rect(self, myHome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        return is_Move

    # 向下移动
    def move_down(self, brickGroup, ironGroup, myHome):
        self.direction_x, self.direction_y = 0, 1
        # 移动
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0,48),(48,48))
        self.tank_1 = self.tank.subsurface((48,48),(48,48))
        is_Move = True

        # 判断是否可以移动
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
            is_Move = False

        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        # 撞其他坦克
        # ///////TODO: 撞其他坦克

        # 大本营
        if pygame.sprite.collide_rect(self, myHome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        return is_Move

    def move_left(self, brickGroup, ironGroup, myHome):
        self.direction_x, self.direction_y = -1, 0
        # 移动
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0,96),(48,48))
        self.tank_1 = self.tank.subsurface((48,96),(48,48))
        is_Move = True

        #判断是否可以移动
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * self.direction_x, self.speed *  self.direction_y)
            is_Move = False

        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        # 撞其他坦克
        # ///////TODO: 撞其他坦克

        # 大本营
        if pygame.sprite.collide_rect(self, myHome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        return is_Move

    def move_right(self, brickGroup, ironGroup, myHome):
        self.direction_x, self.direction_y = 1, 0
        # 移动
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
        is_Move = True

        # 判断是否可以移动
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
            is_Move = False

        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        # 撞其他坦克
        # ///////TODO: 撞其他坦克

        # 大本营
        if pygame.sprite.collide_rect(self, myHome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_Move = False

        return is_Move




# 敌方坦克