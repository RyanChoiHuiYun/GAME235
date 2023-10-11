# Fall object game v1
# Ryan Cai
GAME_WIDTH = 500
GAME_HEIGHT = 500
ballPosX = 0
ballPosY = 0
ballRadius = [30, 50, 70]
ballSpeed = 5

paddlePosX = 0
paddlePosY = GAME_HEIGHT - 20
paddleWidth = 50
paddleHeight = 25

def setup():
    size(GAME_WIEDTH, GAME_HEIGHT)
    background(250, 250, 250)
    noStroke()
    textSize(32)
    rectMode(CENTER)
    
    global ballPosX, ballPosY
    ballPosX = width/2
    ballPosY = -ballRadius[0]

def draw():
    global ballPosX, ballPosY, paddlePosX
    ballPosY += ballSpeed
    paddlePosX = mouseX
    
    if ballPosY > height + ballRadius[0]:
        ballPosX = random(0, width)
        ballPosY = -ballRadius[0]
        
    if ballPosX > paddlePosX - paddleWidth/2 and ballPosX < paddlePosX + paddleWidth/2:
        if (paddlePosY - ballPosY) <= 5:
            ballPosX = random(0, width)
            ballPosY = -ballRadius[0]
        fill(120, 120, 255)
    else:
        fill(255, 255, 255)
    background(255, 120, 255)
    fill(120, 120, 255)
    circle(ballPosX, ballPosY, ballRadius[0])
    fill(220, 220, 220)
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)
    


    
