import pygame

# 大本营模块

class Home(pygame.sprite.Sprite):
    def __init__(self):
        # 产生关联之后需要初始化一下
        pygame.sprite.Sprite.__init__(self)
        # 列表存储不同状态的大本营素材
        self.homeImgs = ["./images/home/home1.png","./images/home/home2.png","./images/home/home_destroyed.png"]
        # 设置图片
        self.home = pygame.image.load(self.homeImgs[0])

        # 大本营显示的位置及其大小
        self.hrect = self.home.get_rect()
        self.hrect.left,self.hrect.top = (3 + 12 * 24, 3 + 24 * 24)
        # 是否存活
        self.aLive = True

        def set_Dead(self):
            self.home = pygame.image.load(self.homeImgs[-1])
            self.aLive = False
