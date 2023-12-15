from object import *
INTRO = 0
GAME = 1
GAME_OVER = 2
PLAYER_POS = PVector(400, 600)
PLAYER_V = PVector(0, 0)
PLAYER_HP = 100
PLAYER = 0
BULLET = 1
VERTICAL = 3
HORIZONTAL = 4

PLAYER_COLLISION = 0
BULLET_COLLISION = 1

mode = 1
mobs = []
mobsLimit = 5
p_bullets = []
score = 0
high_score = 0
p_hp = PLAYER_HP


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
    global p_hp, score, high_score, mobsLimit
    background(0)
    text("HP: " + str(p_hp), 15, 25)
    text("Score: " + str(score), 750, 25)
    if score >= 25:
        mobsLimit = 25
    # create player
    player = Player(PLAYER_POS, PLAYER_V, PLAYER, 100)
    player.render()
    player.update()
    # create bullet
    if keyPressed:
        if key == "j" or key == "J":
            if len(p_bullets) < 1:
                tempPos = PVector(player.pos.x, player.pos.y)
                bullet = Bullet(tempPos, PLAYER_V, PLAYER, 1)
                p_bullets.append(bullet)
    for pb in p_bullets:
        pb.render()
        pb.update()
    # create mobs
    if len(mobs) < 100:
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
        if collisionDetection(player, m, PLAYER_COLLISION):
            p_hp -= 1
            m.hp -= 1
        for pb in p_bullets:
            if collisionDetection(pb, m, BULLET_COLLISION):
                pb.hp -= 1
                m.hp -= 1
                score += 1
    
    mobDeletion()
    bulletDeletion()

def mobDeletion():
    for m in mobs:
        if m.hp <= 0:
            mobs.remove(m)
        if isOffScreen(m.pos) is not 0:
            mobs.remove(m)

def bulletDeletion():
    for b in p_bullets:
        if b.hp <= 0:
            p_bullets.remove(b)
        if isOffScreen(b.pos) is not 0:
            p_bullets.remove(b)
        
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

def collisionDetection(objA, objB, mode):
    if mode == 0:
        if (abs(objA.pos.x - objB.pos.x) <= 15) and (abs(objA.pos.y - objB.pos.y) <= 15):
            return True
        return False
    if mode == 1:
        if (abs(objA.pos.x - objB.pos.x) <= 25) and (abs(objA.pos.y - objB.pos.y) <= 25):
            return True
        return False
    



    
