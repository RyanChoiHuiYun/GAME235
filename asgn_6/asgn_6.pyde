# Ryan Cai
# Modified from Day 12 Demo - OOP Part 2

shapeList = []
SHAPE_SIZE_DECAY = -0.25
GRAVITY_VALUE = 1

def setup():
    size(800, 800)
    background(0)
    textSize(24)
    rectMode(CENTER)
    
def draw():
    background(0)
    if mousePressed:
        tempPos = PVector(mouseX, mouseY)
        tempVel = PVector(random(2.0) - 1, random(2.0) - 1)
        tempSize = 50
        tempColor = randomColor(120)
        chance = int(random(0, 2))
        if chance == 1:
            newShape = Triangle(tempPos, tempVel, tempSize, tempColor)
        else:
            newShape = Rectangle(tempPos, tempVel, tempSize, tempColor)
        shapeList.append(newShape)
        
        
    for shape in shapeList:
        shape.update()
        shape.render()
        
    fill(255)
    textAlign(LEFT)
    text("Shapes: " + str(len(shapeList)), 8, 25)



def randomColor(floorValue = 0, ceilingValue = 255):
    return color(random(floorValue, ceilingValue), random(floorValue, ceilingValue), random(floorValue, ceilingValue), )

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

class Shape(object):
    def __init__(self, tempPos, tempVel, tempSize, tempColor):
        self.pos = tempPos
        self.vel = tempVel
        self.siz = tempSize
        self.col = tempColor
        self.startingSize = tempSize
        self.rotation = 0
        
    def update(self):
        self.vel += PVector(0, GRAVITY_VALUE)
        self.pos += self.vel
        self.siz += SHAPE_SIZE_DECAY
        self.rotation += self.vel.x / 10.0
        self.wallReflection()
        self.selfDeletion()
        
    def render(self):
        textAlign(CENTER)
        fill(self.col, 255 * self.siz/float(self.startingSize))
        #text("Shape", self.pos.x, self.pos.y)
        
    def wallReflection(self):
        whichWall = isOffScreen(self.pos)
        if whichWall > 0:
            if whichWall % 2 == 1:
                self.vel.rotate(PI - 2*self.vel.heading())
            else:
                self.vel.rotate(-2*self.vel.heading())
    
    def selfDeletion(self):
        if self.siz < 0 and self in shapeList:
            shapeList.remove(self)

class Rectangle(Shape):
    def render(self):
        super(Rectangle, self).render()
        rect(self.pos.x, self.pos.y, random(15, 50), random(15, 50))
            
class Triangle(Shape):
    def render(self):
        super(Triangle, self).render()
        triangle(self.pos.x, self.pos.y, self.pos.x + 15, self.pos.y + 15, self.pos.x - 15, self.pos.y + 15)
