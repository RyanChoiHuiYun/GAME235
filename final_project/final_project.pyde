from object import *
INTRO = 0
GAME = 1
GAME_OVER = 2
PLAYER_POS = PVector(400, 600)
PLAYER_V = PVector(0, 0)
mode = 1
mobs = []
bullets = []
VERTICAL = 3
HORIZONTAL = 4

def setup():
    size(800, 800)
    mode = INTRO
    
def draw():
    if mode == INTRO:
        intro()
    elif mode == GAME:
        main()
    elif mode == GAME_OVER:
        return 2
    
def intro():
    textMode(CENTER)
    textSize(24)
    text("W - move up", 10, 20)
    text("A - move left", 10, 40)
    text("S - move down", 10, 60)
    text("D - move right", 10, 80)
    
def main():
    background(0)
    if len(mobs) < 5:
        if random(0,2) < 1:
            tempPos = PVector(random(0, width/4), random(0, height/2))
            mob = Mob(tempPos, PLAYER_V, VERTICAL, 1)
        else:
            tempPos = PVector(random(0, width-20), random(0, 200))
            mob = Mob(tempPos, PLAYER_V, HORIZONTAL, 1)
        mobs.append(mob)
    for m in mobs:
        m.render()
        m.update()
    player = Player(PLAYER_POS, PLAYER_V, 0, 3)
    player.render()
    player.update()
    mobDeletion()
    if mousePressed:
        if len(bullets) < 1:
            tempPos = PVector(player.pos.x, player.pos.y)
            bullet = Bullet(tempPos, PLAYER_V, 0, 2)
            bullets.append(bullet)
    for b in bullets:
        b.render()
        b.update()
    bulletDeletion()

def mobDeletion():
    for m in mobs:
        if isOffScreen(m.pos) is not 0:
            mobs.remove(m)

def bulletDeletion():
    for b in bullets:
        if isOffScreen(b.pos) is not 0:
            bullets.remove(b)
        
def isOffScreen(vector):
    if vector.x < 0:
        return 1
    elif vector.y > height:
        return 2
    elif vector.x > width:
        return 3
    elif vector.y < 0:
        return 4
    return 0

def collisionDetection(a, b):
    return
    



    
