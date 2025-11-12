import pgzrun
import time

HEIGHT = 500
WIDTH = 500

questionrectangle = Rect(0, 60, 400, 60)
answerrectangle1 = Rect(30, 160, 150, 80)
answerrectangle2 = Rect(190, 160, 150, 80)
answerrectangle3 = Rect(30, 250, 150, 80)
answerrectangle4 = Rect(190, 250, 150, 80)
timerrectangle = Rect(400, 60, 100, 60)
skiprectangle = Rect(350, 160, 140, 170)

score = 0
timer = 20

def timedown():
    global timer
    if timer > 0:
        timer -= 1

Wrongy = False
boxes = [answerrectangle1, answerrectangle2, answerrectangle3, answerrectangle4]
questions = []

banner_text = "Welcome to the Kavith Quiz Master Game!"
banner_x = WIDTH 
banner_speed = 2  
banner_y = 20     


def read_ans():
    global questions
    text = open('Quiz\\Text.txt')
    questions = text.readlines()

def nextqu():
    global questions
    firstquestion = questions.pop(0)
    fq = firstquestion.split('|')
    return fq

def correct():
    global Wrongy, timer, nextq, score
    score += 1
    if questions:
        nextq = nextqu()
    else:
        nextq = ['Congrats you got: ' + str(score) + '/5', '-', '-', '-', '-', 0]
        timer = 0
    Wrongy = False

def wrong():
    global Wrongy, timer, nextq
    Wrongy = True
    nextq = ['Game Over you got: ' + str(score) + '/5', '-', '-', '-', '-', 0]
    timer = 0
    print(nextq)

def on_mouse_down(pos):
    global nextq, timer
    boxnum = 1
    for box in boxes:
        if box.collidepoint(pos):
            if boxnum == int(nextq[5]):
                print('yes')
                correct()
            else:
                print('wrong')
                wrong()
        boxnum += 1
    if questions:
        if skiprectangle.collidepoint(pos):
            nextq = nextqu()
    else:
        nextq = ['Game Over you got: ' + str(score) + '/5', '-', '-', '-', '-', 0]
        timer = 0

def draw():
    screen.clear()
    

    screen.draw.text(banner_text, (banner_x, banner_y), color="yellow", fontsize=40)

    screen.draw.filled_rect(questionrectangle, (0, 0, 190))
    screen.draw.filled_rect(timerrectangle, (0, 190, 0))
    screen.draw.filled_rect(skiprectangle, (0, 120, 160))
    for i in range(4):
        screen.draw.filled_rect(boxes[i], (0, 90, 90))
    screen.draw.textbox(nextq[0], questionrectangle)
    screen.draw.textbox(nextq[1], answerrectangle1)
    screen.draw.textbox(nextq[2], answerrectangle2)
    screen.draw.textbox(nextq[3], answerrectangle3)
    screen.draw.textbox(nextq[4], answerrectangle4)
    screen.draw.textbox(str(timer), timerrectangle)
    screen.draw.textbox('skip', skiprectangle, angle=0)

def update():
    global banner_x
    banner_x -= banner_speed
    text_width = screen.surface.get_width() + len(banner_text) 
    if banner_x < -text_width:
        banner_x = WIDTH


read_ans()
nextq = nextqu()
clock.schedule_interval(timedown, 1)
pgzrun.go()
