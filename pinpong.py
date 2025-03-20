import random
import pygame
import time

updateUrl=""
Render3d=False
LevelEdit=True
Boxes=[]

pygame.init()
screenW=1920/2
screenH=1080/2
screen = pygame.display.set_mode((screenW, screenH))
x=screenW/2
y=screenH/2
pygame.display.set_caption('pinpong')
angle=45
angx=0
wallColor = (254,254,254)
maxTrail=100
pointsDot=[]
timeInBossFight=0
wallsX=[150,screenW-170]
wallsY=[0,0]
anglel = 180
colBall=[(255, 125, 10),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255,255,255)]
selcol=0
boompos = (x,y)
boomsize=0
    #BossImage=pygame.image.load("image.png")
moveY2=0
moveY=0
    # imag=pygame.image.load('image.png')
    # for yh in range(imag.get_height()-1):
    #     mas=[]
    #     for xw in range(imag.get_width()-1):
    #         try:
    #             mas.append(imag.get_at((xw,yh)))
    #         except:
    #             mas.append((0,0,0,0))
    #     BossImage.append(mas)
    # open("foo.txt", "a").write(str(BossImage))

gameTextY=-200

score = [0,0]

angy=0
oldPos=[]
colorCir = (255, 125, 10)
radiusCir=10
boss=False
for fone in range(255):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screenW, screenH), 0)
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(f'PinAndPong'), True, (fone, fone, fone))
    screen.blit(text, (screenW / 2 - 400 // 2 + 5, 0 + 220))
    pygame.display.flip()
    time.sleep(0.001)
time.sleep(1)
for fone in range(255):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screenW, screenH), 0)
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(f'PinAndPong'), True, (255-fone, 255-fone, 255-fone))
    screen.blit(text, (screenW / 2 - 400 // 2 + 5, 0 + 220))
    pygame.display.flip()
    time.sleep(0.001)
while True:
    backGroundY=0
    screenW = 1920 / 2
    screenH = 1080 / 2
    screen = pygame.display.set_mode((screenW, screenH))
    x = screenW / 2
    y = screenH / 2
    angle = 45
    angx = 0

    maxTrail = 100
    pointsDot = []
    wallsX = [150, screenW - 170]
    wallsY = [0, 0]
    anglel = 180

    selcol = 0
    boompos = (x, y)
    boomsize = 0
    # BossImage=pygame.image.load("image.png")
    moveY2 = 0
    moveY = 0
    score = [0, 0]
    # imag=pygame.image.load('image.png')
    # for yh in range(imag.get_height()-1):
    #     mas=[]
    #     for xw in range(imag.get_width()-1):
    #         try:
    #             mas.append(imag.get_at((xw,yh)))
    #         except:
    #             mas.append((0,0,0,0))
    #     BossImage.append(mas)
    # open("foo.txt", "a").write(str(BossImage))

    gameTextY = -200



    angy = 0
    oldPos = []

    radiusCir = 10
    boss = False
    for dots in range(10):
        pointsDot.append([random.randint(0,int(screenW)),random.randint(0,int(screenH))])
    def PlaySound(file):
        try:
            pygame.mixer.Sound(file).play()
        except:
            print("Fail play sound")
    def BackGround():
        if wallColor==(254,254,254):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screenW, screenH), 0)
            for i in range(200):
                R=70
                G=37
                B=125
                R -= i
                G -= i
                B -= i
                if R < 0: R = 0
                if G < 0: G = 0
                if B < 0: B = 0
                pygame.draw.rect(screen, (R, G, B,i), pygame.Rect(0, screenH-i*3, screenW, 3), 0)
            for dots in pointsDot:
                dots[1] -= 1
                if dots[1] <= -10:
                    dots[1] = int(screenH) + 10
                    dots[0]=random.randint(0,int(screenW))
                pygame.draw.circle(surface=screen, color=(255, 255, 255), center=(dots[0], dots[1]), radius=3, width=0)
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, screenW, screenH), 0)
    def AngleMove(x,y,speed,angle):
        moveVector = pygame.math.Vector2()
        moveVector.from_polar((speed,angle))
        return (x,y) + moveVector
    def SetAngle(_angle):
        global boss
        global angle
        global angx,angy
        angle = _angle
        if boss==True:
            angx = AngleMove(0,0,5,angle)[0]
            angy = AngleMove(0,0,5,angle)[1]
        if boss==False:
            angx = AngleMove(0,0,2,angle)[0]
            angy = AngleMove(0,0,2,angle)[1]
    SetAngle(random.randint(0,360))
    def DistGet(xy,xy2):
        distX = xy[0] - xy2[0]
        # if distX<0:distX=-distX
        distY = xy[1] - xy2[1]
        # if distY < 0: distY = -distY
        return (distX,distY)

    def CircleMove():
        global x
        global y
        global gameTextY
        global angx
        global angy
        global anglel
        global angle
        global mah
        global boomsize
        global boompos
        if screen.get_at((int(x+angx), int(y))) == wallColor:
            angx = -angx
            anglel = 180

            mah = False


        elif screen.get_at((int(x), int(y+angy))) == wallColor:
            angy = -angy
            anglel = 180
            mah=False


        if setting==False:
            if x <= 10:
                boomsize = 0
                boompos = (x, y)
                score[1]+=1
                gameTextY=-200
                x = screenW / 2
                y = screenH / 2
                SetAngle(random.randint(45,60))

            if x>=screenW-10:
                boomsize = 0
                boompos = (x, y)
                gameTextY = -200
                x = screenW / 2
                y = screenH / 2
                SetAngle(random.randint(45,60))

                score[0]+=1
        if x<=10 or x>=screenW-10:
            angx = -angx
        if y<=10 or y>=screenH-10:
            angy = -angy
            #angle=angle-180;
        (x,y) = (angx+x,angy+y) #AngleMove(x,y,1, angle)
    def AiMove(char):
        global x
        global y
        global gameTextY
        global angx
        global angy
        global angle
        pogreh=15
        global boomsize
        global boss
        global boompos
        tmpx=x
        tmpy=y
        tmpangx=angx
        tmpangy = angy
        for stepToAi in range(350):

            try:
                if screen.get_at((int(tmpx + tmpangx), int(tmpy))) == wallColor and tmpx < wallsX[char]-10:
                    tmpangx = -tmpangx


                elif screen.get_at((int(tmpx), int(tmpy + tmpangy))) == wallColor and tmpx < wallsX[char]-10:
                    tmpangy = -tmpangy
            except:
                print("",end="")

            if tmpx <= 10 or tmpx >= screenW - 10:
                tmpangx = -tmpangx
            if tmpy <= 10 or tmpy >= screenH - 10:
                tmpangy = -tmpangy
                # angle=angle-180;

            #pygame.draw.circle(surface=screen, color=(255, 0, 255), center=(tmpx, tmpy), radius=1, width=0)

            (tmpx, tmpy) = (tmpangx+random.randint(-pogreh,pogreh) + tmpx, tmpangy+random.randint(-pogreh,pogreh) + tmpy)
            if tmpx >= wallsX[char] and char==1:
                #print(stepToAi)
                break
            if tmpx <= wallsX[char] and char==0:
                #print(stepToAi)
                break
        # tmpx = x
        # tmpy = y
        # tmpangx = angx
        # tmpangy = angy
        if boss==False:
            if tmpangy+tmpy<wallsY[char]+50:
                wallsY[char]+=(-1/1.2)
            else:
                wallsY[char] += (1 / 1.2)
        else:
            if tmpangy+tmpy<wallsY[char]+50:
                wallsY[char]+=(-1*3)
            else:
                wallsY[char] += (1 * 3)
    pygame.mouse.set_visible(False)
    setting=False
    play=False
    bot=False
    selectButt = False
    backGroundY=0
    LevelEdit = False
    while True:
        time.sleep(0.005)
        BackGround()
        sizeS=7
        size=5

        if setting==True:
            wallsY[0] = y-50
            wallsY[1] = y - 50
            for wallIn in range(len(wallsX)):
                pygame.draw.rect(screen, wallColor, pygame.Rect(wallsX[wallIn], wallsY[wallIn], 20, 100), 0)
            CircleMove()
            for xy in range(1, len(oldPos)):
                pygame.draw.circle(surface=screen, color=(colorCir[0], colorCir[1], colorCir[2]), center=oldPos[xy],
                                   radius=radiusCir - xy / 10, width=0)
            pygame.draw.circle(surface=screen, color=colorCir, center=(x, y), radius=radiusCir, width=0)
            oldPos.insert(0, (x, y))
            if len(oldPos) > maxTrail:
                oldPos.pop()
            font = pygame.font.SysFont(None, 120)
            text = font.render(str(f'Settings'), True, wallColor)
            screen.blit(text, (screenW / 2 - 170, 50))
            buttW = 150
            buttY = 200
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0,
                             border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Ball color'), True, (255, 255, 255))

            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
            buttW = 150
            buttY = 320
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0,
                             border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Theme'), True, (255, 255, 255))
            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
            buttW = 150
            buttY = 440
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0,
                             border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Exit'), True, (255, 255, 255))
            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
            # buttW = 150
            # buttY = 0
            # pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(0, buttY, buttW, 100), 0,
            #                  border_radius=30)
            # font = pygame.font.SysFont(None, 50)
            # text = font.render(str(f'3D'), True, (255, 255, 255))
            # screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
        if setting==False and play==False:
            font = pygame.font.SysFont(None, 120)
            text = font.render(str(f'PinPong'), True, wallColor)
            screen.blit(text, (screenW / 2 - 170, 50))
            buttW=150
            buttY=200
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW/2-buttW//2, buttY, buttW, 100), 0,border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Play'), True, (255, 255, 255))
            screen.blit(text, (screenW/2-buttW//2+5, buttY+30))
            buttW = 150
            buttY = 320
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0, border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Settings'), True, (255, 255, 255))
            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
        if play==True:
            font = pygame.font.SysFont(None, 120)
            text = font.render(str(f'How play?'), True, wallColor)
            screen.blit(text, (screenW / 2 - 170, 50))
            buttW=150
            buttY=200
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW/2-buttW//2, buttY, buttW, 100), 0,border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Player'), True, (255, 255, 255))
            screen.blit(text, (screenW/2-buttW//2+5, buttY+30))
            buttW = 150
            buttY = 320
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0, border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Bot'), True, (255, 255, 255))
            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
            buttW = 150
            buttY = 440
            pygame.draw.rect(screen, (37, 31, 71), pygame.Rect(screenW / 2 - buttW // 2, buttY, buttW, 100), 0,
                             border_radius=30)
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(f'Map Editor'), True, (255, 255, 255))
            screen.blit(text, (screenW / 2 - buttW // 2 + 5, buttY + 30))
        for mouseSize in range(10):
            pygame.draw.circle(surface=screen, color=colorCir, center=(
            pygame.mouse.get_pos()[0] + mouseSize * 2, pygame.mouse.get_pos()[1] + mouseSize * 2), radius=mouseSize + 3,
                               width=0)
        for mouseSize in range(10):
            pygame.draw.circle(surface=screen, color=(0 + mouseSize * 4, 0 + mouseSize * 4, 0 + mouseSize * 4), center=(
            pygame.mouse.get_pos()[0] + mouseSize * 2, pygame.mouse.get_pos()[1] + mouseSize * 2), radius=mouseSize,
                               width=0)
        exitMenu = False

        if backGroundY != screenH - 10: backGroundY += 10
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, backGroundY, screenW, screenH), 0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pygame.mouse.get_pos()[0] >= screenW / 2 - 150 // 2 and pygame.mouse.get_pos()[
                0] <= screenW / 2 - 150 // 2 + 150 and pygame.mouse.get_pos()[1] >= 320 and pygame.mouse.get_pos()[
                1] <= 420:
                if selectButt==False:
                    PlaySound("sel.mp3")
                    selectButt = True
            elif pygame.mouse.get_pos()[0] >= screenW / 2 - 150 // 2 and pygame.mouse.get_pos()[
                0] <= screenW / 2 - 150 // 2 + 150 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[
                1] <= 300:
                if selectButt==False:
                    PlaySound("sel.mp3")
                    selectButt = True
            elif pygame.mouse.get_pos()[0] >= screenW / 2 - 150 // 2 and pygame.mouse.get_pos()[
                0] <= screenW / 2 - 150 // 2 + 150 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[
                1] <= 540:
                if selectButt==False:
                    PlaySound("sel.mp3")
                    selectButt = True
            else:
                selectButt=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if setting ==False and play==False:
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 200 and pygame.mouse.get_pos()[1] <= 300:
                        play=True
                        PlaySound("blip1.mp3")
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 320 and pygame.mouse.get_pos()[1] <= 420:
                        setting=True
                        PlaySound("blip1.mp3")
                elif play==True:
                    if pygame.mouse.get_pos()[0] >= screenW / 2 - 150 // 2 and pygame.mouse.get_pos()[
                        0] <= screenW / 2 - 150 // 2 + 150 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[
                        1] <= 540:
                        LevelEdit=True
                        exitMenu=True
                        PlaySound("blip1.mp3")
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 200 and pygame.mouse.get_pos()[1] <= 300:
                        bot=False
                        exitMenu = True
                        PlaySound("blip1.mp3")
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 320 and pygame.mouse.get_pos()[1] <= 420:
                        bot=True
                        exitMenu=True
                        PlaySound("blip1.mp3")
                elif setting==True:
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 200 and pygame.mouse.get_pos()[1] <= 300:
                        selcol+=1
                        if selcol==len(colBall):
                            selcol=0
                        colorCir=colBall[selcol]
                        PlaySound("blip1.mp3")
                    if pygame.mouse.get_pos()[0]>= screenW/2-150//2 and pygame.mouse.get_pos()[0] <= screenW/2-150//2+150 and pygame.mouse.get_pos()[1]>= 320 and pygame.mouse.get_pos()[1] <= 420:
                        if wallColor==(254,254,254):
                            wallColor=(0,0,0)
                        else:
                            wallColor = (254,254,254)
                        PlaySound("blip1.mp3")
                    if pygame.mouse.get_pos()[0] >= screenW / 2 - 150 // 2 and pygame.mouse.get_pos()[
                        0] <= screenW / 2 - 150 // 2 + 150 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[
                        1] <= 540:
                        setting=False
                        PlaySound("blip1.mp3")
        if exitMenu==True:
            break
    SetAngle(random.randint(45, 60))
    setting=False
    x=screenW/2
    y=screenH/2
    mah=False
    backGroundY=0
    exitMenu=False
    #BossImage=pygame.transform.scale(BossImage, (BossImage.get_width() - 100, BossImage.get_height() - 100))
    if boss ==True:
        PlaySound("mus.mp3")
    draw=False
    setc=50
    if LevelEdit==True:
        while True:
            time.sleep(0.005)
            BackGround()
            posSeeBox=[(pygame.mouse.get_pos()[0] - 5)//setc*setc, (pygame.mouse.get_pos()[1] - 5)//setc*setc, setc, setc]
            pygame.draw.rect(screen, (135,135,135), pygame.Rect(posSeeBox[0], posSeeBox[1], posSeeBox[2], posSeeBox[3]), 0)
            for Box in Boxes:
                if Render3d == True:
                    demul3d = 30
                    pygame.draw.rect(screen, (135, 135, 135), pygame.Rect(
                        Box[0] + -DistGet((Box[0], Box[1] + 50), (screenW / 2, screenH / 2))[
                            0] / demul3d,
                        Box[1] + -DistGet((Box[0], Box[1] + 50), (screenW / 2, screenH / 2))[
                            1] / demul3d, Box[2], Box[3]), 0)
            for Box in Boxes:

                pygame.draw.rect(screen, wallColor, pygame.Rect(Box[0],Box[1], Box[2], Box[3]), 0)
            for mouseSize in range(10):
                pygame.draw.circle(surface=screen, color=colorCir, center=(
                    pygame.mouse.get_pos()[0] + mouseSize * 2, pygame.mouse.get_pos()[1] + mouseSize * 2),
                                   radius=mouseSize + 3,
                                   width=0)
            for mouseSize in range(10):
                pygame.draw.circle(surface=screen, color=(0 + mouseSize * 4, 0 + mouseSize * 4, 0 + mouseSize * 4),
                                   center=(
                                       pygame.mouse.get_pos()[0] + mouseSize * 2,
                                       pygame.mouse.get_pos()[1] + mouseSize * 2), radius=mouseSize,
                                   width=0)
            exitMenu = False
            pygame.display.flip()
            if draw==True:

                Boxes.append(
                    [(pygame.mouse.get_pos()[0] - 5) // setc * setc, (pygame.mouse.get_pos()[1] - 5) // setc * setc,
                     setc, setc])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()



                if event.type == pygame.MOUSEBUTTONDOWN:
                   draw=True
                if event.type == pygame.MOUSEBUTTONUP:
                    draw = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        mah = True

                    if event.key == pygame.K_UP:
                        setc += 4
                    if event.key == pygame.K_DOWN:
                        setc -= 4
                    if event.key == pygame.K_w:
                        moveY = -1
                    if event.key == pygame.K_s:
                        moveY = 1
                    if event.key == pygame.K_q:
                        exitMenu = True
                    if event.key == pygame.K_r:
                        Boxes=[]
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        moveY2 = 0
                    if event.key == pygame.K_DOWN:
                        moveY2 = 0
                    if event.key == pygame.K_w:
                        moveY = 0



            if exitMenu == True:
                break
    while True:
        time.sleep(0.005)
        boomsize+=1
        if boomsize>= 255:
            boomsize=255



        BackGround()

        for Box in Boxes:
            if Render3d == True:
                demul3d = 30
                pygame.draw.rect(screen, (135, 135, 135), pygame.Rect(
                    Box[0] + -DistGet((Box[0], Box[1] + 50), (screenW / 2, screenH / 2))[
                        0] / demul3d,
                    Box[1] + -DistGet((Box[0], Box[1] + 50), (screenW / 2, screenH / 2))[
                        1] / demul3d, Box[2], Box[3]), 0)
        for Box in Boxes:

            pygame.draw.rect(screen, wallColor, pygame.Rect(Box[0], Box[1], Box[2], Box[3]), 0)
        for wallIn in range(len(wallsX)):
            if Render3d==True:

                demul3d=30
                pygame.draw.rect(screen, (135,135,135), pygame.Rect(wallsX[wallIn]+-DistGet((wallsX[wallIn], wallsY[wallIn]+50),(screenW/2,screenH/2))[0]/demul3d, wallsY[wallIn]+-DistGet((wallsX[wallIn], wallsY[wallIn]+50),(screenW/2,screenH/2))[1]/demul3d, 20, 100), 0)
            pygame.draw.rect(screen, wallColor, pygame.Rect(wallsX[wallIn], wallsY[wallIn], 20, 100), 0)
        if boss==True:

            for laz in range(1):
                xl = wallsX[0]+50
                yl = wallsY[0]+100

                if mah==True:anglel+=4
                if anglel==360+180:
                    mah=False
                    anglel=180
                pygame.draw.circle(surface=screen, color=wallColor, center=(xl, yl), radius=12, width=0)
                for ranL in range(2):(xl, yl) = AngleMove(xl, yl, 10, anglel)
                for lazer in range(5):
                    (xl, yl) = AngleMove(xl, yl, 10, anglel)
                    pygame.draw.circle(surface=screen, color=wallColor, center=(xl, yl), radius=12, width=0)
        #pygame.draw.rect(screen, wallColor, pygame.Rect(500, 100, 100, 500), 0)

        if gameTextY >= screenH: CircleMove()
        if boss == False:
            wallsY[0] += moveY / 1.2
        else:
            wallsY[0] += moveY * 3

        if bot == False and boss == False:
            wallsY[1] += moveY2 / 1.2
        else:
            AiMove(1)
            #screen.blit(BossImage, (screenW - BossImage.get_width(), screenH - BossImage.get_height()))

        if boomsize<255: pygame.draw.circle(surface=screen, color=(255, 0 + boomsize, 0 + boomsize), center=boompos, radius=boomsize//2, width=0)
        for xy in range(1,len(oldPos)):
            pygame.draw.circle(surface=screen, color=(colorCir[0],colorCir[1],colorCir[2]), center=oldPos[xy], radius=radiusCir - xy/10, width=0)
        pygame.draw.circle(surface=screen, color=colorCir, center=(x,y), radius=radiusCir, width=0)
        if gameTextY < screenH:
            pygame.draw.circle(surface=screen, color=(0,0,150), center=((angx*5 + x), (angy*5 + y)), radius=radiusCir, width=0)
        oldPos.insert(0, (x,y))
        if len(oldPos) > maxTrail:
            oldPos.pop()
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(f'{score[0]} / {score[1]}'), True, (255,0,0))
        screen.blit(text, (screenW/2-60, 50))
        font = pygame.font.SysFont(None, 100)
        text = font.render(str(f'Round!'), True, wallColor)
        screen.blit(text, (screenW / 2 - 140, gameTextY))
        gameTextY+=3
        exitMenu=False

        if backGroundY!=screenH+10:backGroundY+=10
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, backGroundY, screenW, screenH), 0)

        if boss==True:
            timeInBossFight+=1
            timeonbit=30
            if timeInBossFight % timeonbit >= 0 and timeInBossFight % timeonbit <= 20 :

                s = pygame.Surface((screenW, screenH))  # the size of your rect
                s.set_alpha(255 - timeInBossFight % timeonbit*12)  # alpha level
                s.fill((255, 255, 255))  # this fills the entire surface
                screen.blit(s, (0,0))
                if timeInBossFight >= 1010 and timeInBossFight <= 2500:
                    # x-=0.01
                    if random.randint(0,30) == 15:
                        angx = -angx


                # for pixC in range(100):
                #     pos=(random.randint(0,round(screenW)-10),random.randint(0,round(screenH)-10))
                #     colPix = screen.get_at(pos)
                #
                #     else:
                #
                #         pygame.draw.rect(screen, colPix, pygame.Rect(pos[0]-10, pos[1]-10, (20-timeInBossFight % timeonbit)*2 , (20-timeInBossFight % timeonbit)* 2), 0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    mah=True

                if event.key == pygame.K_UP:
                    moveY2 = -1
                if event.key == pygame.K_DOWN:
                    moveY2 = 1
                if event.key == pygame.K_w:
                    moveY = -1
                if event.key == pygame.K_s:
                    moveY = 1
                if event.key == pygame.K_q:
                    exitMenu=True
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    moveY2 = 0
                if event.key == pygame.K_DOWN:
                    moveY2 = 0
                if event.key == pygame.K_w:
                    moveY = 0
                if event.key == pygame.K_s:
                    moveY = 0
        if exitMenu==True or LevelEdit==True:
            break
        #if boss==True and score[1] >0:
        #    break



        

