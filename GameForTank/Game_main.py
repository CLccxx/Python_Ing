import pygame
import sys
# 导入自定义模块
import home
import scene
import tanks
import food

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
            if event.type == pygame.KEYDOWN:
                main()


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
        # 生成敌方坦克事件
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
        for i in range(0,3):
            if enemytanks_total > 0:
                enemytank = tanks.enemyTank(i)
                tanksGroup.add(enemytank)
                enemyTanksGroup.add(enemytank)
                enemytanks_now += 1
                enemytanks_total -= 1

        appearance_img = pygame.image.load("./images/others/appear.png").convert_alpha()
        appearance = []
        appearance.append(appearance_img.subsurface((0,0),(48,48)))
        appearance.append(appearance_img.subsurface((48,0),(48,48)))
        appearance.append(appearance_img.subsurface((96,0),(48,48)))


        # 实时监听用户操作事件 1. 用户点击事件 2. 用户点击键盘
        while True:
            if is_GameOver is True:
                break
            if enemytanks_total < 1 and enemytanks_now < 1:
                is_GameOver = False
                break

            # 遍历所有事件
            for event in pygame.event.get():
                # 如果点击了关闭
                if event.type == QUIT:
                    # 关闭屏幕
                    sys.exit()
                if event.type == genEnemyEvent:
                    if enemytanks_total > 0:
                        if enemytanks_now < enemytanks_now_max:
                            enemytank = tanks.enemyTank()
                            if not pygame.sprite.spritecollide(enemytank, tanksGroup, False, None):
                                tanksGroup.add(enemytank)
                                enemyTanksGroup.add(enemytank)
                                enemytanks_now += 1
                                enemytanks_total -= 1

                if event.type == recoverEnemyEvent:
                    for each in enemyTanksGroup:
                        each.can_move = True

                if event.type == noprotextMyTankEvent:
                    for each in myTanksGroup:
                        each.protected = False

            # 刷新背景
            screen.blit(bg_img,(0,0))

            # 监听用户按键事件
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            if key_pressed[pygame.K_s]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            if key_pressed[pygame.K_a]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            if key_pressed[pygame.K_d]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            if key_pressed[pygame.K_SPACE]:
                if not tank_player1.bullet.being:
                    fire_sound.play()
                    tank_player1.shoot()

            # 玩家二
            if player > 1:
                if key_pressed[pygame.K_UP]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_DOWN]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_LEFT]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_RIGHT]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_0]:
                    if not  tank_player2.bullet.being:
                        fire_sound.play()
                        tank_player2.shoot()

            # 绘制大本营
            screen.blit(myHome.home, myHome.rect)

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

            time += 1
            if time == 5:
                time = 0
                is_switch_tank = not is_switch_tank

            # 绘制本方坦克
            if tank_player1 in myTanksGroup:
                if is_switch_tank and player1_moving:
                    screen.blit(tank_player1.tank_0, tank_player1.rect)
                    player1_moving = False
                else:
                    screen.blit(tank_player1.tank_1, tank_player1.rect)
                # 如果有保护罩
                if tank_player1.protected:
                    screen.blit(tank_player1.protected_mask1, tank_player1.rect)
            if player > 1:
                if tank_player2 in myTanksGroup:
                    if is_switch_tank and player2_moving:
                        screen.blit(tank_player2.tank_0, tank_player2.rect)
                        player1_moving = False
                    else:
                        screen.blit(tank_player2.tank_1, tank_player2.rect)

                    if tank_player2.protected:
                        screen.blit(tank_player2.protected_mask1, tank_player2.rect)

            # 绘制敌方坦克
            for each in enemyTanksGroup:
                # 出生特效
                if each.born:
                    if each.times > 0:
                        each.times -= 1
                        if each.times <= 10:
                            screen.blit(appearance[2],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 20:
                            screen.blit(appearance[1],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 30:
                            screen.blit(appearance[0],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 40:
                            screen.blit(appearance[2],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 50:
                            screen.blit(appearance[1],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 60:
                            screen.blit(appearance[0],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 70:
                            screen.blit(appearance[2],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 80:
                            screen.blit(appearance[1],(3 + each.x * 12 * 24, 3))
                        elif each.times <= 90:
                            screen.blit(appearance[0],(3 + each.x * 12 * 24, 3))
                    else:
                        each.born = False
                else:
                    if is_switch_tank:
                        screen.blit(each.tank_0, each.rect)
                    else:
                        screen.blit(each.tank_1, each.rect)

                    if each.can_move:
                        tanksGroup.remove(each)
                        each.move(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myHome)
                        tanksGroup.add(each)

            # 我方子弹
            for tank_player in myTanksGroup:
                if tank_player.bullet.being:
                    tank_player.bullet.move()
                    screen.blit(tank_player.bullet.bullet, tank_player.bullet.rect)

                    # 子弹碰撞敌方子弹
                    for each in enemybulletsGroup:
                        if each.being:
                            if pygame.sprite.collide_rect(tank_player.bullet, each):
                                tank_player.bullet.being = False
                                each.bing = False
                                enemybulletsGroup.remove(each)
                                break
                        else:
                            enemybulletsGroup.remove(each)

                    # 子弹碰撞敌方坦克
                    for each in enemyTanksGroup:
                        if each.being:
                            if pygame.sprite.collide_rect(tank_player.bullet, each):
                                if each.is_Red == True:
                                    myfood = food.Food()
                                    myfood.generate()
                                    myfoodsGroup.add(myfood)
                                    each.is_Red = False
                                each.blood -= 1
                                each.color -= 1
                                if each.blood < 0:
                                    bang_sound.play()
                                    each.being = False
                                    enemyTanksGroup.remove(each)
                                    enemytanks_now -= 1
                                    tanksGroup.remove(each)
                                else:
                                    each.reload()
                                tank_player.bullet.being = False
                                break
                        else:
                            enemyTanksGroup.remove(each)
                            tanksGroup.remove(each)

                    # 子弹碰撞石头墙
                    for each in map_stage.brickGroup:
                        if pygame.sprite.collide_rect(tank_player.bullet, each):
                            tank_player.bullet.being = False
                            each.being = False
                            map_stage.brickGroup.remove(each)
                            break

                    # 子弹碰撞钢墙
                    for each in map_stage.ironGroup:
                        if pygame.sprite.collide_rect(tank_player.bullet, each):
                            tank_player.bullet.being = False
                            if tank_player.bullet.stronger:
                                each.being = False
                                map_stage.ironGroup.remove(each)
                            break

                    # 子弹碰撞大本营
                    if pygame.sprite.collide_rect(tank_player.bullet, myHome):
                        tank_player.bullet.being = False
                        myHome.set_Dead()
                        is_GameOver = True
                        break
            # 敌方子弹
            for each in enemyTanksGroup:
                if each.being:
                    if each.can_move and not each.bullet.being:
                        enemyTanksGroup.remove(each.bullet)
                        each.shoot()
                        enemybulletsGroup.add(each.bullet)
                    if not each.born:
                        if each.bullet.being:
                            each.bullet.move()
                            screen.blit(each.bullet.bullet, each.bullet.rect)
                            # 子弹碰撞我方坦克
                            for tank_player in myTanksGroup:
                                if pygame.sprite.collide_rect(each.bullet, tank_player):

                                    if tank_player.protected:
                                        tank_player.protected = False
                                    else:
                                        tank_player.life -= 1
                                    if tank_player.life < 0:
                                        myTanksGroup.remove(tank_player)
                                        tanksGroup.remove(tank_player)
                                        if len(myTanksGroup) < 1:
                                            is_GameOver = True
                                    else:
                                        tank_player.reset()

                                    each.bullet.being = False
                                    enemybulletsGroup.remove(each.bullet)
                                    brick

                            # 子弹碰撞石头墙
                            for brick in map_stage.brickGroup:
                                if pygame.sprite.collide_rect(each.bullet, brick):
                                    each.bullet.being = False
                                    enemybulletsGroup.remove(each.bullet)
                                    brick.being = False
                                    map_stage.brickGroup.remove(brick)
                                    break

                            # 子弹碰撞钢墙
                            for iron in map_stage.ironGroup:
                                if pygame.sprite.collide_rect(each.bullet, iron):
                                    each.bullet.being = False
                                    if each.bullet.stronger:
                                        iron.being = False
                                        map_stage.ironGroup.remove(iron)
                                    break

                            # 子弹碰撞大本营
                            if pygame.sprite.collide_rect(each.bullet, myHome):
                                each.bullet.being = False
                                myHome.set_Dead()
                                is_GameOver = True
                                break
                else:
                    enemyTanksGroup.remove(each)
                    tanksGroup.remove(each)


            # 食物
            for myfood in myfoodsGroup:
                if myfood.being and myfood.time > 0:
                    screen.blit(myfood.food, myfood.rect)
                    myfood.time -= 1
                    for tanke_player in myTanksGroup:
                        if pygame.sprite.collide_rect(tank_player, myfood):
                            # 消灭当前所有敌人
                            if myfood.kind == 0:
                                for _ in enemyTanksGroup:
                                    bang_sound.play()
                                enemyTanksGroup = pygame.sprite.Group()
                                enemytanks_total -= enemytanks_now
                                enemytanks_now = 0

                            # 敌人静止
                            if myfood.kind == 1:
                                for each in enemyTanksGroup:
                                    each.can_move = False

                            # 子弹增强
                            if myfood.kind == 2:
                                add_sound.play()
                                tank_player.bullet.stronger = True

                            # 是大本营的墙变为刚板
                            if myfood.kind == 3:
                                map_stage.protect_home()

                            # 坦克获得一段时间的保护罩
                            if myfood.kind == 4:
                                add_sound.play()
                                for tank_player in myfoodsGroup:
                                    tank_player.protected = True

                            # 坦克升级
                            if myfood.kind == 5:
                                add_sound.play()
                                tank_player.up_level()

                            # 坦克生命 + 1
                            if myfood.kind == 6:
                                add_sound.play()
                                tank_player.lefe += 1

                            myfood.being = False
                            myfoodsGroup.remove(myfood)
                            break
                else:
                    myfood.being = False
                    myfoodsGroup.remove(myfood)

            pygame.display.flip()
            clock.tick(60)

        if not is_GameOver:
            show_interface_end(screen, 630,630, True)
        else:
            show_interface_end(screen,630,630, False)


main()