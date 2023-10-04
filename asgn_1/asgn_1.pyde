# this is a comment. xD
def setup():
    size(400, 400) # size of window: (width,height)
    background(200, 0, 255) # color of background: (r,g,b)
    noStroke()

def draw():
    fill(0, 200, random(200,255))
    ellipse(mouseX, mouseY, 15, 30)
    fill(random(200,255), 200, 255)
    ellipse(mouseY, mouseX, 30, 15) # symmetric/mirror
