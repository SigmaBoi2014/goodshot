import pgzrun
import random


WIDTH =500
HEIGHT =500

msg="shoot the monster"
result=""
goodshots=0

badshots=0
monster=Actor("the cookie")
monster.x=250
monster.y=250

def draw():
    screen.fill("black")
    monster.draw()
    screen.draw.text(msg,(250,30))
    screen.draw.text(result,(250,50))
    screen.draw.text("goodshots "+str(goodshots),(100,30))
    screen.draw.text("badshots "+str(badshots),(100,50))

    if result=="bad shot":
        screen.fill("red")
        monster.draw()
        screen.draw.text(msg,(250,30))
        screen.draw.text(result,(250,50))
        screen.draw.text("goodshots "+str(goodshots),(100,30))
        screen.draw.text("badshots "+str(badshots),(100,50))
    if result== "good shot":
        screen.fill("green")
        monster.draw()
        screen.draw.text(msg,(250,30))
        screen.draw.text(result,(250,50))
        screen.draw.text("goodshots "+str(goodshots),(100,30))
        screen.draw.text("badshots "+str(badshots),(100,50))
def on_mouse_down(pos):
    global result
    global goodshots
    global badshots
    if monster.collidepoint(pos):
        monster.x=random.randint(50,450)
        monster.y=random.randint(50,450)
        result="good shot"
        goodshots+=1
    else:
        result="bad shot"
        badshots+=1
        
pgzrun.go()