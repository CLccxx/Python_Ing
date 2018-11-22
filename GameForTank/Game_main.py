import pygame
import sys
# 导入自定义模块
import home
import scene
import tanks

from pygame.locals import *

# 每一关结束之后显示的界面
def show_change_stage(screen, scrWidth, scrHeight, stage):
    # 设置背景图片
    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img ,(0, 0))

    # 设置文字
    tfont = pygame.font.Font("./font/simkai.ttf", scrWidth // 20)
    title = tfont.render(u"第%d关" % stage ,True, (0, 255, 0))
    trect = title.get_rect()
    trect.midtop = (scrWidth / 2, scrHeight / 2.5)

    screen.blit(title, trect)
    pygame.display.update()

    # 自定义事件
    dele_event = pygame.constants.USEREVENT
    # 将事件添加到事件队列里面，执行他（1000计量单位为毫秒）
    pygame.time.set_timer(dele_event, 1000)

    # 监听用户事件，关闭 或 时间到了自动结束当前界面
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == dele_event:
                return

# 游戏开始界面
def show_interface_start(screen, scrWidth, scrHeight):

    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img, (0, 0))

    tfont = pygame.font.Font("./font/simkai.ttf", scrWidth // 4)
    cfont = pygame.font.Font("./font/simkai.ttf", scrWidth // 20)
    title = tfont.render(u"坦克大战",True,(255,0,0))
    content1 = cfont.render(u"按1进入单人游戏",True,(0,255,255))
    content2 = cfont.render(u"按2进入双人游戏",True,(0,255,255))
    trect = title.get_rect()
    crect = content1.get_rect()
    crect2 = content2.get_rect()

    # mid 中间点，top 距上间距
    trect.midtop = (scrWidth / 2 , scrHeight / 4)
    crect.midtop = (scrWidth / 2 , scrHeight / 1.8)
    crect2.midtop = (scrWidth / 2, scrHeight / 1.6)

    # 将文字显示到屏幕上（渲染屏幕）
    # 第一个参数为显示的文字，第二个参数是显示的大小及其位置
    screen.blit(title, trect)
    screen.blit(content1, crect)
    screen.blit(content2, crect2)

    # 刷新一下
    pygame.display.update()

    # 监听用户事件
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2

# 游戏结束界面
def show_interface_end(screen, scrWidth, scrHeight, is_Win):
    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img,(0, 0))
    if is_Win:
        tfont = pygame.font.Font("./font/simkai.ttf", scrWidth // 20)
        title = tfont.render(u"恭喜通关", True, (255, 0, 0))
        trect = title.get_rect()
        trect.midtop = (scrWidth / 2, scrHeight / 2.5)
        screen.blit(title, trect)
    else:
        fail_img = pygame.image.load("./images/others/gameover.png")
        fail_ima_rect = fail_img.get_rect()
        fail_ima_rect.midtop = (scrWidth / 2, scrWidth / 2)
        screen.blit(fail_img, fail_ima_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


# 加载音乐
def add_load_Music():
    pass

# 绘制地图
def drawMap(screen):
    pass


def main():
    pygame.init()
    # 构造屏幕宽高为 630 * 630
    screen = pygame.display.set_mode([630 , 630])
    # 设置窗口上方显示的文字
    pygame.display.set_caption("坦克大战-xx_cc")
    # 刷新一下
    # pygame.display.update()

    # 默认关数
    stage = 0
    # 总关数
    stage_Num = 2
    # 游戏是否结束
    is_GameOver = False
    # 时钟
    clock = pygame.time.Clock()

    # 显示主页面
    player = show_interface_start(screen, 630, 630)

    # 加载音频
    sound_volume = 1
    add_sound = pygame.mixer.Sound("./audios/add.wav")
    bang_sound = pygame.mixer.Sound("./audios/bang.wav")
    blast_sound = pygame.mixer.Sound("./audios/blast.wav")
    fire_sound = pygame.mixer.Sound("./audios/fire.wav")
    gunfire_sound = pygame.mixer.Sound("./audios/Gunfire.wav")
    hit_sound = pygame.mixer.Sound("./audios/hit.wav")
    start_sound = pygame.mixer.Sound("./audios/start.wav")

    # 设置音量
    add_sound.set_volume(sound_volume)
    bang_sound.set_volume(sound_volume)
    blast_sound.set_volume(sound_volume)
    fire_sound.set_volume(sound_volume)
    gunfire_sound.set_volume(sound_volume)
    hit_sound.set_volume(sound_volume)
    start_sound.set_volume(sound_volume)

    # 游戏主循环
    while not is_GameOver:
        stage += 1
        if stage > stage_Num:
            break

        # 游戏开始音效
        start_sound.play()

        # 显示当前关数界面 1s时间
        show_change_stage(screen, 630, 630, stage)

        # 该关卡坦克总数量
        enemytanks_total = min(stage * 18 ,80)
        # 场上存在的地方坦克总数量
        enemytanks_now = 0
        # 场上可以存在的地方坦克总数量
        enemytanks_now_max = min((max(stage * 2, 4), 8))

        # 精灵组
        tanksGroup = pygame.sprite.Group()
        myTanksGroup = pygame.sprite.Group()
        enemyTanksGroup = pygame.sprite.Group()
        bulletsGroup = pygame.sprite.Group()
        mybulletsGroup = pygame.sprite.Group()
        enemybulletsGroup = pygame.sprite.Group()
        myfoodsGroup = pygame.sprite.Group()

        # 自定义事件
        # 生成地方坦克事件
        genEnemyEvent = pygame.constants.USEREVENT
        pygame.time.set_timer(genEnemyEvent, 100)

        # 敌方坦克静止恢复事件
        recoverEnemyEvent = pygame.constants.USEREVENT
        pygame.time.set_timer(recoverEnemyEvent, 8000)

        # 我方坦克无敌恢复事件
        noprotextMyTankEvent = pygame.constants.USEREVENT
        pygame.time.set_timer(noprotextMyTankEvent, 8000)

        # 显示背景
        bg_img = pygame.image.load("./images/others/background.png")
        screen.blit(bg_img, (0, 0))

        # 显示大本营
        # 在外部模块使用其他模块的类创建对象时，需要：模块名字+类名创建
        myHome = home.Home()

        # 绘制地图
        map_stage = scene.Map(stage)

        # 添加我方坦克
        tank_player1 = tanks.myTank(1)
        tanksGroup.add(tank_player1)
        myTanksGroup.add(tank_player1)
        if player > 1:
            tank_player2 = tanks.myTank(2)
            tanksGroup.add(tank_player2)
            myTanksGroup.add(tank_player2)

        is_switch_tank = True
        player1_moving = False
        player2_moving = False

        # 为了轮胎的动画效果
        time = 0
        # 敌方坦克




        # 实时监听用户操作事件 1. 用户点击事件 2. 用户点击键盘
        while True:

            # 遍历所有事件
            for event in pygame.event.get():
                # 如果点击了关闭
                if event.type == QUIT:
                    # 关闭屏幕
                    sys.exit()

            # 刷新背景
            screen.blit(bg_img,(0,0))

            # 监听用户按键事件
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w]:
                tank_player1.move_up(map_stage.brickGroup, map_stage.ironGroup, myHome)
            if key_pressed[pygame.K_s]:
                tank_player1.move_down(map_stage.brickGroup, map_stage.ironGroup, myHome)
            if key_pressed[pygame.K_a]:
                tank_player1.move_left(map_stage.brickGroup, map_stage.ironGroup, myHome)
            if key_pressed[pygame.K_d]:
                tank_player1.move_right(map_stage.brickGroup, map_stage.ironGroup, myHome)

            # 绘制大本营
            screen.blit(myHome.home, myHome.rect)

            # 绘制本方坦克
            screen.blit(tank_player1.tank_0, tank_player1.rect)

            # 绘制地图元素（砖块等）
            for eachBrick in map_stage.brickGroup:
                screen.blit(eachBrick.brick, eachBrick.rect)

            for eachIron in map_stage.ironGroup:
                screen.blit(eachIron.iron, eachIron.rect)

            for eachIce in map_stage.iceGroup:
                screen.blit(eachIce.ice, eachIce.rect)

            for eachRiver in map_stage.riverGroup:
                screen.blit(eachRiver.river, eachRiver.rect)

            for eachTree in map_stage.treeGroup:
                screen.blit(eachTree.tree, eachTree.rect)

            pygame.display.flip()


main()