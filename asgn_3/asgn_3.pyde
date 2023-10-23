# Assignment 3: Fall object game v2
# Ryan Cai

# Constants
GAME_WIDTH = 500
GAME_HEIGHT = 500
ACCEL_RATE = 1.15
MIN_SPEED = 5
MAX_SPEED = 12.5

# score properties
score = 0
highScore = 0
# ball properties
ballPosX = [random(GAME_WIDTH), random(GAME_HEIGHT)]
ballPosY = [0, 0]
ballColor = [color(50, 50, 255), color(50, 250, 255)]
ballRadius = [40, 60]
ballSpeed = [MIN_SPEED, MIN_SPEED]
append = False
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

def draw():
    global ballPosX, ballPosY, paddlePosX, score, highScore, ballSpeed, ballColor
    background(highScore*25)

        
    for i in range(len(ballPosX)):
        ballPosY[i] += ballSpeed[i]
        paddlePosX = mouseX
        if score > highScore:
            highScore = score # updating high score
        
        # failed state: reset score, reset speed
        if ballPosY[i] > height + ballRadius[i]:
            ballPosX[i] = random(0, width)
            ballPosY[i] = -ballRadius[i]
            if (i == 0):
                score = 0
            else:
                score -= 2
            ballSpeed[i] = MIN_SPEED
            
            
        if ballPosX[i] > paddlePosX - paddleWidth/2 and ballPosX[i] < paddlePosX + paddleWidth/2:
            if (paddlePosY - ballPosY[i]) <= 5:
                # success state: score increase, speed increase
                if (i == 0):
                    score += 1
                else:
                    score += 2
                if ballSpeed[i] < MAX_SPEED and i == 0:
                    ballSpeed[i] = ballSpeed[i] * 1.025
                if ballSpeed[i] < MAX_SPEED and i == 1:
                    ballSpeed[i] = ballSpeed[i] * 1.005
                ballPosX[i] = random(0, width)
                ballPosY[i] = -ballRadius[i]
    
            fill(ballColor[i])
        else:
            fill(255, 255, 255)

        fill(ballColor[i])
        circle(ballPosX[i], ballPosY[i], ballRadius[i])
    
    
    
    fill(220, 220, 220)
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)
    
    # some feedbacks to the player
    fill(250, 250, 250)
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
        text("Pog!", GAME_WIDTH / 2, GAME_HEIGHT / 2)
    


    
