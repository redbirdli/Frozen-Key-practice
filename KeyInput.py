import sys,random,math,pygame # 引用了系统、随机数、数学、Python游戏四个类库

words="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"#`-=\[]/;',."  # 这是会从掉落的字符序列

def drawText(screen,text,posx,posy,textHeight=40,fontColor=(0,180,180),backgroudColor=(0,0,0)):
    fontObj = pygame.font.Font("C://Windows//Fonts//simhei.ttf", textHeight)  # 通过字体文件获得字体对象
    temp=""
    if text.upper() in "1qaz0p;/-=\[]".upper():   #不同的字母，对应不同的输入键位
      if text.upper() in "1qaz".upper():temp="左小指  "
      else:temp="右小指  "
      fontColor=(255,255,60)
    elif text.upper() in "2wsx9ol.".upper():
      if text.upper() in "2wsx".upper():temp="左无名指"
      else:temp="右无名指"
      fontColor=(78,189,244)
    elif text.upper() in "3edc8ik,".upper():
      if text.upper() in "3edc".upper():temp="左中指  "
      else:temp="右中指  "
      fontColor=(180,255,180)
    elif text.upper() in "4rfv5tgb".upper():
      temp="左食指  "
      fontColor=(255,153,153)
    elif text.upper() in "6yhn7ujm".upper():
      temp="右食指  "
      fontColor=(248,153,248)
    textSurfaceObj = fontObj.render(text, True,fontColor)  # 配置要显示的文字
    screen.blit(textSurfaceObj, (posx,posy))  
    if level<3 and temp!="" and i>30 and fault>0:  # 在第一关第二关中显示键盘图示
      fontObj = pygame.font.Font("C://Windows//Fonts//simhei.ttf", 20)
      screen.blit(fontObj.render(temp, True,fontColor,backgroudColor) , (948,500)) 

pygame.init()  #游戏初始化
size = width, height =1050, 750   #窗口大小
screen = pygame.display.set_mode(size)
pygame.display.set_caption('空格键唤醒键盘位置图示') # 标题栏提示

snowPos=[]
snowFall=[]
snows=random.randint(20,50) # 随机初始化雪花的数量
for i in range(snows):# 随机给出雪花在窗体上，一次可以显示的个数
  x = random.randint(0,width-5) #参数1为上限，参数2为下限
  y = random.randint(0,100)#random.randint(0,450)
  snowFall.append(random.randint(1,3)) #雪花下落的速度
  snowPos.append([x,y]) # 保存随机获得的位置

# 加载游戏会用到的图片素材
over=pygame.image.load('resource/over.png')  
newSize=over.get_rect()
over=pygame.transform.smoothscale(over,(int(newSize.width*0.3),int(newSize.height*0.3)))

bruni=pygame.image.load('resource/bruni.png') 
newSize=bruni.get_rect()
bruni=pygame.transform.smoothscale(bruni,(int(newSize.width*0.1),int(newSize.height*0.1)))

ball=pygame.image.load('resource/ball.png') 
newSize=ball.get_rect()
ball=pygame.transform.smoothscale(ball,(int(newSize.width*0.1),int(newSize.height*0.1)))

snow1=pygame.image.load('resource/snow.png') 
newSize=snow1.get_rect()
snow1=pygame.transform.smoothscale(snow1,(int(newSize.width*0.1),int(newSize.height*0.1)))
snow2=pygame.image.load('resource/snow1.png') 
newSize=snow2.get_rect()
snow2=pygame.transform.smoothscale(snow2,(int(newSize.width*0.02),int(newSize.height*0.02)))

bg1=pygame.image.load("resource/deer.png")
newSize=bg1.get_rect()
bg1=pygame.transform.smoothscale(bg1,(int(newSize.width*0.71),int(newSize.height*0.71)))

bg2 = pygame.image.load("resource/sis.png")
newSize=bg2.get_rect()
bg2=pygame.transform.smoothscale(bg2,(int(newSize.width*0.82),int(newSize.height*0.82)))

bg0 = pygame.image.load("resource/key.png")#.convert()
screen.blit(bg0,(15,410))
bg0=screen.copy()

carrot=pygame.image.load("resource/Carrot.png")
carrot = pygame.transform.rotate(carrot, 50)
newSize=carrot.get_rect()
carrot=pygame.transform.smoothscale(carrot,(int(newSize.width*0.1),int(newSize.height*0.1)))
olafo=pygame.image.load("resource/5.png")
newSize=olafo.get_rect()
olafo=pygame.transform.smoothscale(olafo,(int(newSize.width*0.3),int(newSize.height*0.3)))
#pygame.display.set_caption('Frozen KeyFall 定制版')
# bg.set_colorkey(bg.get_at((10,10)))

pygame.mixer.music.load("resource/showyourself.mp3") # 载入背景音乐
pygame.mixer.music.set_volume(0.1)# 设置音量为 0.2
pygame.mixer.music.play(100) # 播放背景音乐

levelsound = pygame.mixer.Sound("resource/0.wav") # 关卡升级音效
levelsound.set_volume(0.8)

rightsound = pygame.mixer.Sound("resource/1.wav")  # 输入正确音效
rightsound.set_volume(0.8)

faultsound = pygame.mixer.Sound("resource/fault.wav")  # 输入错误音效
faultsound.set_volume(0.8)
i=256
oldi=0
pygame.key.set_repeat(200)
while True:   # 游戏主循环
  screen.fill((0,0,0))  # 屏幕刷成黑色
  if i==256:#初始化
    oldi=0
    alphai=20
    olaf=pygame.transform.flip(olafo,90,0)
    wordY=30
    score=0
    level=1
    fault=9
    olafX=500
    dx=1
    bgz=screen.copy()
    bgn=bg0.copy()
    bg=bgn
    i=255
    right=1
    wrong=0
  #pygame.display.set_caption(str(pygame.mouse.get_pos()))
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()  # 接收到退出事件就退出整个游戏
    elif event.type==pygame.KEYDOWN:  # 如果是按键事件，就继续判断按的到底什么键
      if chr(event.key).upper()==key.upper(): # 如果事件触发的按键值 与 画面显示的键 一致，说明按键正确
        rightsound.play()  # 播放按键正确的声音
        wordY=30           # 赋值成30 会触发重新生成一个 新的随机字符
        score+=5
        right+=1
        i-=alphai          # 键盘的透明度越来越隐
        if score >= level*100 >0:   # 如果得分 超过 100，关卡还在 1关，就会触发 关卡升级 ，以此类推
          level+=1    
          levelsound.play()   # 播放升级的声音
          if level>2 and level<8:  # 第三关以后，开始有冰雪奇缘的人物彩蛋画面陆续出现
            if level==3:alphai=-alphai
            screen.fill((0,0,0))
            screen.blit(bgz,(0,0))
            if level==3 or level>4:
              screen.blit(bg1,(25,350))
            if level>=4:
              screen.blit(bg2,(560,350))
            if level>5:      
              screen.blit(bruni,(20,692))
            if level>6:    
              screen.blit(ball,(915,650))
            if  i!=0:i=0
            bgn=screen.copy()
            bg=bgn
          else:i=255
          if dx>0:dx=level
          else:dx=-level
     
      elif  event.key==pygame.K_SPACE :  # 如果按的是空格
        if fault==0:i=256    # 如果游戏生命结束就重新开始游戏，否则就是呼叫唤醒键盘位置图示
        else: bg=bgn=bg0
      elif fault>0:  # 如果按键错误
          score-=5
          faultsound.play()
          i+=alphai*2
          words+=key #把当前没按对的字母再追加到字串里，强化错误键的复习
          wordY+=150
          wrong+=1

  if wordY==30:   # 和上方代码呼应，生成新的随机字符，供掉落使用
    key=random.choice(words)
    x=olafX

  if fault>0:   # 生命数还有，减命
    if wordY>=height:
      score-=10
      faultsound.play()
      i+=alphai*2
      words+=key
      fault-=1
      wordY=30
      wrong+=1
      key=random.choice(words)
  
  if fault==0:   # 生命数没了，游戏结束
    screen.blit(bg,(0,0))
    if i!=oldi: 
      bg=screen.copy()
      bg.blit(over,(380,120))
      drawText(bg,"游  戏  结  束             空 格 键 重 新 开 始",70,280,40)
  else:    # 如果什么也没按，字母会按照关卡的速度跌落
    wordY+=level
    if i!=oldi and level>1:
      if i>0:
        bg=bgn
        bg.set_alpha(i)
      else:bg=bgz

  oldi=i
  screen.blit(bg,(0,0))


  screen.blit(carrot,(970,8))    # 画胡萝卜生命数
  drawText(screen,"x"+str(fault),1020,20,18)  
  screen.blit(olaf,(olafX,0))   # 动态位置画雪宝
  drawText(screen,"得分："+str(score),0,0,18)   # 计算得分
  drawText(screen,"正确率:"+str(right*100//(right+wrong))+"%",0,20,18)  # 计算正确率
  drawText(screen,"关卡："+str(level),970,0,18)  # 显示关卡

  if olafX>=width-20 or olafX<10:   # 负责雪宝在屏幕两端间来回溜达
    dx=-dx
    olaf=pygame.transform.flip(olaf,90,0)
  olafX+=dx

  num=0
  for snowone in snowPos: # 雪花列表循环，从snowone轴的上限往下限方向飘落
    snowone[1]=snowone[1]+snowFall[num] #改变snowone轴坐标，移动雪花位置

    if snowPos.index(snowone) % 2==0: snowStart=snow1    # 雪花的左右摇摆飘落规则
    else:snowStart=snow2   
    if snowone[1] % 4 <2:screen.blit(snowStart,(snowone[0]+snowone[1] % 2,snowone[1]))
    else:screen.blit(snowStart,(snowone[0],snowone[1])) 
    tempX=snowone[0]+5
    if tempX>=width:
      tempX=width-1
    tempY=snowone[1]+3

    if  bg.get_at((tempX,tempY)) != (0,0,0) or snowone[1]>=height-7: #判断当前雪花下方的图像是否黑色，如果非黑色，就停在那里，形成堆叠效果
      if tempY>85:bg.blit(snowStart,(snowone[0],snowone[1])) 
      snowone[1]=random.randint(0,50) #重设snowone轴的坐标到0以上，从而使得雪花下一次循环有效
      if snowone[1]<25:snowone[0]=random.randint(0,width-10)
      else:snowone[0]=random.randint(olafX-5,olafX+5)   #random.randint(0,width-5)
    num+=1
  drawText(screen,key,x,wordY)   # 显示掉落的字母
  pygame.display.flip()  #更新整个待显示的Surface 对象到屏幕上
  pygame.time.delay(50//level)    # 屏幕延迟
