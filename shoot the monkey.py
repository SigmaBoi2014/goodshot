import pgzrun
import random

WIDTH =500
HEIGHT =500
msg="shoot the monkey"
result=""
goodshots=0
badshots=0
monkey=Actor("smiley monkey (3)")
monkey.x=250
monkey.y=250
def draw():
    screen.fill("black")
    monkey.draw()
    screen.draw.text(msg,(250,30))
    screen.draw.text(result,(250,50))
    screen.draw.text("goodshots "+str(goodshots),(100,30))
    screen.draw.text("badshots "+str(badshots),(100,50))

def on_mouse_down(pos):
    global result
    global goodshots
    global badshots
    if monkey.collidepoint(pos):
        monkey.x=random.randint(50,450)
        monkey.y=random.randint(50,450)
        result="good shot"
        goodshots+=1
    else:
        result="bad shot"
        badshots+=1
pgzrun.go()