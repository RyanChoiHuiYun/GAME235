# Assignment 2: Fall object game v1
# Ryan Cai

# Constants
GAME_WIDTH = 500
GAME_HEIGHT = 500
ACCEL_RATE = 1.15
MIN_SPEED = 5
MAX_SPEED = 20

# score properties
score = 0
highScore = 0
# ball properties
ballPosX = 0
ballPosY = 0
ballRadius = 40
ballSpeed = MIN_SPEED
# paddle board properties
paddlePosX = 0
paddlePosY = GAME_HEIGHT - 20
paddleWidth = 50
paddleHeight = 25

def setup():
    size(GAME_WIDTH, GAME_HEIGHT)
    background(250, 250, 250)
    noStroke()
    textSize(32)
    rectMode(CENTER)
    
    global ballPosX, ballPosY
    ballPosX = width/2
    ballPosY = -ballRadius

def draw():
    global ballPosX, ballPosY, paddlePosX, score, highScore, ballSpeed
    ballPosY += ballSpeed
    paddlePosX = mouseX
    if score > highScore:
        highScore = score # updating high score
    
    # failed state: reset score, reset speed
    if ballPosY > height + ballRadius:
        ballPosX = random(0, width)
        ballPosY = -ballRadius
        score = 0
        ballSpeed = MIN_SPEED
        
        
    if ballPosX > paddlePosX - paddleWidth/2 and ballPosX < paddlePosX + paddleWidth/2:
        if (paddlePosY - ballPosY) <= 5:
            # success state: score increase, speed increase
            score += 1
            if ballSpeed < MAX_SPEED:
                ballSpeed = ballSpeed * 1.05
            ballPosX = random(0, width)
            ballPosY = -ballRadius

        fill(120, 120, 255)
    else:
        fill(255, 255, 255)
    background(255, 120, 255)
    fill(120, 120, 255)
    circle(ballPosX, ballPosY, random(ballRadius-5, ballRadius+5))
    fill(220, 220, 220)
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)
    fill(35, 35, 35)
    
    # some feedbacks to the player
    text("Score: " + str(score), 10, 30)
    if score > 0:
        if score % 10 == 0:
            text(":O", 10, 90)
        else:
            text(":)", 10, 90)
    else:
        text(":(", 10, 90)
    text("High Score: " + str(highScore), 10, 60)
    if score > 0 and score % 10 == 0:
        text("Pog!", random(0, GAME_WIDTH), random(25, GAME_HEIGHT - 250))
    


    
