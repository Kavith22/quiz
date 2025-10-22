import pgzrun
HEIGHT=500
WIDTH=500
questionrectangle=Rect(0,60,400,60)
answerrectangle1=Rect(30,160,150,80)
answerrectangle2=Rect(190,160,150,80)
answerrectangle3=Rect(30,250,150,80)
answerrectangle4=Rect(190,250,150,80)
timerrectangle=Rect(400,60,100,60)
skiprectangle=Rect(350,160,140,170)
boxes=[answerrectangle1,answerrectangle2,answerrectangle3,answerrectangle4]

questions=[]
def read_ans():
    global questions
    text = open('Quiz\Text.txt')
    questions=(text.readlines())

def nextqu():
    global questions
    firstquestion=questions.pop(0)
    fq=(firstquestion.split('|'))
    return fq

def correct():
    global nextq
    nextq=nextqu()

def on_mouse_down(pos):
    boxnum=1
    for box in boxes:
        if box.collidepoint(pos):
            if boxnum == int(nextq[5]):      
                print('yes')
                correct()
            else:
                print('wrong')
        boxnum=boxnum+1

def draw():
    screen.draw.filled_rect(questionrectangle,(0,0,190))
    screen.draw.filled_rect(timerrectangle,(0,190,0))
    screen.draw.filled_rect(skiprectangle,(0,120,160))
    for i in range(4):
        screen.draw.filled_rect(boxes[i],(0,90,90))
    screen.draw.textbox(nextq[0], questionrectangle)
    screen.draw.textbox(nextq[1], answerrectangle1)
    screen.draw.textbox(nextq[2], answerrectangle2)
    screen.draw.textbox(nextq[3], answerrectangle3)
    screen.draw.textbox(nextq[4], answerrectangle4)
read_ans()
nextq=nextqu()
pgzrun.go()