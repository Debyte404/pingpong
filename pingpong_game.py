from numpy import dot
from ursina import *
import random

#pingpong

app = Ursina()

camera.orthographic = True
window.title = "ping pong"
Text.default_resolution = 1080 * Text.size

bat_distance = 20
vertical_padding = 15
speed = 5

started = False

test = Text(text="SPACEBAR TO PLAY", size = 8,position = (-0.85,0.45,0) , color = color.black)

Ball = Entity(model="sphere",scale=1,collider = "sphere")

Bat_left = Entity(model="cube", scale = (0.5,4,1), position = (-bat_distance,0,0), collider = "box")
Bat_right = Entity(model="cube", scale = (0.5,4,1), position = (bat_distance,0,0), collider = "box")

def input(key):
    global started
    if key == 'space':
        started = True;
        # print("starteded")

def Start():
    global speed
    speed = 5
    init_direction = Vec3(random.choice([-2,2]),random.choice([-1,1]),0)
    return init_direction

direction = Start()

def update():
    global direction
    global started
    global speed

    if started:
        speed += 0.04*time.dt
    # print(speed)
    # if not started:
        
        
        # test.align = 'center'

    if abs(Bat_right.y) > vertical_padding:
        Bat_right.y = vertical_padding * Bat_right.y / abs(Bat_right.y)

    if held_keys[Keys.up_arrow] and started:
        Bat_right.y += 10 * time.dt

    if held_keys[Keys.down_arrow] and started:
        Bat_right.y -= 10 * time.dt

    if abs(Ball.position.x) > bat_distance+5:
        Ball.position = (0,0,0)
        started = False
        Bat_right.y = 0
        direction = Start()

    hitInfo = Ball.intersects()
    
    if abs(Ball.y)> vertical_padding:
        normal = Vec3(0,-1,0) if Ball.y/abs(Ball.y) > 0 else Vec3(0,1,0)
        
        direction = direction - 2*(dot(list(direction),normal)) * normal

    # if 

    if hitInfo.hit:
        # direction = - direction
        # print(direction)
        # print(-hitInfo.normal)
        # direction = direction - 2*(dot(list(direction),hitInfo.normal)) * hitInfo.normal
        normal = Vec3(-1,0,0) if Ball.x/abs(Ball.x) > 0 else Vec3(1,0,0)
        # print(normal)
        # print(hitInfo.normal)  
        # print(type(hitInfo.normal))
        # direction = direction - 2*(dot(list(direction),tuple(normal))) * tuple(normal)
        direction = direction - 2*(dot(list(direction),normal)) * normal
        # pass
        # return

    Bat_left.y = Ball.y;

    if started:
        # print(direction)
        Ball.position += speed * direction * time.dt
        # print("bitch")
        # print("hmm")
    # Ball.x += 100 * time.dt
app.run()