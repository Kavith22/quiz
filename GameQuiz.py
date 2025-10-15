import pgzrun
HEIGHT=500
WIDTH=500
questionrectangle=Rect(0,60,500,60)
answerrectangle1=Rect(30,160,150,80)
answerrectangle2=Rect(190,160,150,80)
answerrectangle3=Rect(30,250,150,80)
answerrectangle4=Rect(190,250,150,80)
timerrectangle=Rect(400,60,100,60)
skiprectangle=Rect(350,160,140,170)
boxes=[answerrectangle1,answerrectangle2,answerrectangle3,answerrectangle4]

def draw():
    screen.draw.filled_rect(questionrectangle,(0,0,190))
    screen.draw.filled_rect(timerrectangle,(0,190,0))
    screen.draw.filled_rect(skiprectangle,(0,120,160))
    for i in range(4):
        screen.draw.filled_rect(boxes[i],(0,90,90))
    screen.draw.textbox("heady", answerrectangle1)
pgzrun.go()
