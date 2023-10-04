# this is a comment. xD
def setup():
    size(400, 400) # size of window: (width,height)
    background(200, 0, 255) # color of background: (r,g,b)
    noStroke()

def draw():
    fill(0, 200, random(200,255))
    circle(mouseX, mouseY, 15) # (x,y,radius)
    fill(random(200,255), 200, 255)
    circle(mouseY, mouseX, 15)
    # line(random(200), random(400), random(200), random(400))
