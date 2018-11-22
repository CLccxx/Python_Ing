# 坦克模块
import pygame
import random
from bullet import Bullet

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
        self.bullet = Bullet()

    # 射击
    def shoot(self):
        self.bullet.being = True
        self.bullet.turn(self.direction_x,self.direction_y)
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top - 1
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet.rect.left = self.rect.right - 1
            self.bullet.rect.top = self.rect.top + 20
        else:
            raise ValueError("myTank bullet class -> direction value error")

        if self.level == 0:
            self.bullet.speed = 8
            self.bullet.stronger = False
        elif self.level ==1:
            self.bullet.speed = 12
            self.bullet.stronger = False
        elif self.level == 2:
            self.bullet.speed = 12
            self.bullet.stronger = True
        elif self.level == 3:
            self.bullet.speed = 16
            self.bullet.stronger = True
        else:
            raise  ValueError("myTank level class -> level value error")

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

    # 死后重置
    def reset(self):
        self.level = 0
        self.protected = False
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0,0),(48,48))
        self.tank_1 = self.tank.subsurface((48,0),(48,48))
        self.rect = self.tank_0.get_rect()
        self.direction_x, self.direction_y = 0, -1
        self.speed = 3
        if self.player == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        elif self.player == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
        else:
            raise ValueError("my Tank class -> player value error")


# 敌方坦克类
class enemyTank(pygame.sprite.Sprite):
    def __init__(self, x = None, kind = None, is_red = False):
        # 用于给刚出生的坦克播放出生特效
        self.born = True
        # python 时间单位毫秒
        self.times = 90
        # 坦克的种类编号
        if kind == None or kind > 3:
            self.kind = random.randint(0,3)
        else:
            self.kind = kind
        # 所有坦克素材
        self.tanks1 = ['./images/enemyTank/enemy_1_0.png', './images/enemyTank/enemy_1_1.png',
                       './images/enemyTank/enemy_1_2.png', './images/enemyTank/enemy_1_3.png']
        self.tanks2 = ['./images/enemyTank/enemy_2_0.png', './images/enemyTank/enemy_2_1.png',
                       './images/enemyTank/enemy_2_2.png', './images/enemyTank/enemy_2_3.png']
        self.tanks3 = ['./images/enemyTank/enemy_3_0.png', './images/enemyTank/enemy_3_1.png',
                       './images/enemyTank/enemy_3_2.png', './images/enemyTank/enemy_3_3.png']
        self.tanks4 = ['./images/enemyTank/enemy_4_0.png', './images/enemyTank/enemy_4_1.png',
                       './images/enemyTank/enemy_4_2.png', './images/enemyTank/enemy_4_3.png']
        self.tanks = [self.tanks1, self.tanks2, self.tanks3, self.tanks4]
        # 是否携带事物（红色的坦克携带食物）
        if is_red is None:
            # 5分之1的概率为红色
            self.is_Red = random.choice((True, False, False, False, False))
        else:
            self.is_Red = is_red

        # 同一种类的坦克具有不同的颜色，红色的坦克比同类坦克多一点血量
        if self.is_Red:
            self.color = 3
        else:
            self.color = random.randint(0,2)
        # 血量
        self.blood = self.color

        # 载入素材
        self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0,48),(48,48))
        self.tank_1 = self.tank.subsurface((48,48),(48,48))
        self.rect = self.tank_0.get_rect()

        # 坦克位置
        if x is None or x > 2:
            self.x = random.randint(0,2)
        else:
            self.x = x
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3

        # 坦克是否可以移动
        self.can_move = True

        # 坦克速度
        self.speed = max(3 - self.kind, 1)

        # 方向 (默认朝下)
        self.direction_x, self.direction_y = 0, 1

        # 是否存活
        self.being = True

        # 子弹
        self.bullet = Bullet()

    # 射击
    def shoot(self):
        self.bullet.being = True
        self.bullet.turn(self.direction_x, self.direction_y)
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top - 1
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet.rect.left = self.rect.right - 1
            self.bullet.rect.top = self.rect.top + 20
        else:
            raise ValueError("myTank bullet class -> direction value error")


    def move(self, tankGroup, brickGroup, ironGroup, myHome):
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        is_Move = True
        if self.direction_x == 0 and self.direction_y == -1:
            self.tank_0 = self.tank.subsurface((0,0),(48,48))
            self.tank_1 = self.tank.subsurface((48, 0),(48,48))
            if self.rect.top < 3:
                self.reset_Location()
                # 给个随机方向
                self.reset_Direction()
                is_Move = False
        elif self.direction_x == 0 and self.direction_y == 1:
            self.tank_0 = self.tank.subsurface((0,48),(48,48))
            self.tank_1 = self.tank.subsurface((48,48),(48,48))
            if self.rect.bottom > 630 - 3:
                self.reset_Location()
                self.reset_Direction()
                is_Move = False
        elif self.direction_x == 1 and self.direction_y == 0:
            self.tank_0 = self.tank.subsurface((0,96),(48,48))
            self.tank_1 = self.tank.subsurface((48,96),(48,48))
            if self.rect.right > 630 - 3:
                self.reset_Location()
                self.reset_Direction()
                is_Move = False
        elif self.direction_x == -1 and self.direction_y == 1:
            self.tank_0 = self.tank.subsurface((0,144),(48,48))
            self.tank_1 = self.tank.subsurface((48,144),(48,48))
            if self.rect.left < 3:
                self.reset_Location()
                self.reset_Direction()
                is_Move = False
        else:
            raise  ValueError("enemyTank class -> direction value error")

        if pygame.sprite.spritecollide(self, brickGroup, False ,None) \
            or pygame.sprite.spritecollide(self, ironGroup, False ,None) \
            or pygame.sprite.spritecollide(self,tankGroup, False, None):
            self.reset_Location()
            self.reset_Direction()
            is_Move = False

        if pygame.sprite.collide_rect(self, myHome):
            self.reset_Location()
            self.reset_Direction()
            is_Move = False

        return is_Move

    # 如果移动越界则返回移动前的位置
    def reset_Location(self):
        self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)

    # 设置随机方向
    def reset_Direction(self):
        self.direction_x, self.direction_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))

    # 重新载入坦克
    def reload(self):
        self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0,0),(48,48))
        self.tank_1 = self.tank.subsurface((48,48),(48,48))