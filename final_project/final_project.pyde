from object import *

INTRO = 0
GAME = 1
GAME_OVER = 2
PLAYER_POS = PVector(400, 600)
PLAYER_V = PVector(0, 0)
PLAYER_HP = 10
PLAYER = 0
BULLET = 1
VERTICAL = 3
HORIZONTAL = 4

PLAYER_COLLISION = 0
BULLET_COLLISION = 1

mode = 0
mobs = []
mobsLimit = 10
bulletsLimit = 1
p_bullets = []
p_hp = PLAYER_HP
score = 0
high_score = 0

def setup():
    size(800, 800)
    mode = INTRO
    
def draw():
    # game loop
    if mode == INTRO:
        intro()
    elif mode == GAME:
        main()
    elif mode == GAME_OVER:
        gameOver()
    
# intro scene, button layouts
def intro():
    global mode
    background(0)
    textMode(CENTER)
    textSize(24)
    fill(255)
    text("W - move up", 10, 20)
    text("A - move left", 10, 40)
    text("S - move down", 10, 60)
    text("D - move right", 10, 80)
    text("J - shoot", 10, 100)
    text("Click to START", 325, 750)
    player = Player(PLAYER_POS, PLAYER_V, PLAYER, 100)
    player.render()
    player.update()
    if keyPressed:
        if key == "j" or key == "J":
            if len(p_bullets) < 1:
                tempPos = PVector(player.pos.x, player.pos.y)
                bullet = Bullet(tempPos, PLAYER_V, PLAYER, 1)
                p_bullets.append(bullet)
    for pb in p_bullets:
        pb.render()
        pb.update()
    bulletDeletion()
    if mousePressed:
        mode = GAME
        
# main game action
def main():
    global p_hp, score, high_score, mobsLimit, bulletsLimit, mode
    # check fail condition
    if p_hp <= 0:
        mode = GAME_OVER
    background(0)
    fill(255)
    textSize(14)
    text("HP: " + str(p_hp), 15, 25) # update hp
    text("Score: " + str(score), 700, 25) # update score
    # difficulties scale up when score is higher
    if score >= 25:
        mobsLimit = 25
        bulletsLimit = 3
    if score >= 100:
        mobsLimit = 50
        bulletsLimit = 5
    if score >= 250:
        mobsLimit = 100
    
    # update high score
    if score > high_score:
        high_score = score
    # create player
    player = Player(PLAYER_POS, PLAYER_V, PLAYER, 100)
    player.render()
    player.update()
    # create bullet
    if keyPressed:
        if key == "j" or key == "J":
            if len(p_bullets) < bulletsLimit:
                tempPos = PVector(player.pos.x, player.pos.y)
                bullet = Bullet(tempPos, PLAYER_V, PLAYER, 1)
                p_bullets.append(bullet)
    for pb in p_bullets:
        pb.render()
        pb.update()
    # create mobs (all melee)
    if len(mobs) < mobsLimit:
        tempPos = PVector(random(0, width-20), random(0, 200))
        mob = Mob(tempPos, PLAYER_V, HORIZONTAL, 3)
        mobs.append(mob)
    for m in mobs:
        m.render()
        m.update()
        if collisionDetection(player, m, PLAYER_COLLISION):
            p_hp -= 1
        for pb in p_bullets:
            if collisionDetection(pb, m, BULLET_COLLISION):
                pb.hp -= 1
                m.hp -= 1
                score += 1
    mobDeletion()
    bulletDeletion()

# game over prompt
def gameOver():
    global score, high_score, mode, p_hp
    p_hp = PLAYER_HP
    background(0)
    fill(255)
    textSize(40)
    text("SCORE: " + str(score), 50, 200)
    text("HIGH SCORE: " + str(high_score), 50, 250)
    text("Press to RESTART", 250, 600)
    if mousePressed:
        score = 0
        mode = GAME

# remove mob from mob array
def mobDeletion():
    for m in mobs:
        if m.hp <= 0:
            mobs.remove(m)
        if isOffScreen(m.pos) is not 0:
            mobs.remove(m)

# remove bullet from bullet array
def bulletDeletion():
    for b in p_bullets:
        if b.hp <= 0:
            p_bullets.remove(b)
        if isOffScreen(b.pos) is not 0:
            p_bullets.remove(b)
        
# detect if object is off screen or not
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

# detect collision between two object
def collisionDetection(objA, objB, mode):
    # player-mob collision mode
    if mode == 0:
        if (abs(objA.pos.x - objB.pos.x) <= 15) and (abs(objA.pos.y - objB.pos.y) <= 15):
            return True
        return False
    # bullet-mob collision mode
    if mode == 1:
        if (abs(objA.pos.x - objB.pos.x) <= 25) and (abs(objA.pos.y - objB.pos.y) <= 25):
            return True
        return False
    



    
