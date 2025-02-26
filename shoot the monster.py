import pgzrun
import random

WIDTH =500
HEIGHT =500

monster=Actor("cookie")
monster.x=250
monster.y=250
def draw():
    monster.draw()

def on_mouse_down(pos):
    if monster.collidepoint(pos):
        monster.x=random.randint(50,450)
        monster.y=random.randint(50,450)
pgzrun.go()
