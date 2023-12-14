class Object(object):
    def __init__(self, pos, v, id, hp):
        self.pos = pos
        self.v = v
        self.id = id
        self.hp = hp
    
    def getPos(self):
        return self.pos
    
    def setPos(self, pos):
        self.pos = pos
    
    def isAlive(self):
        if self.hp <= 0:
            return False
        else:
            return True
    
    def render(self):
        return
    
    def update(self):
        self.selfDeletion()
        return
    
    def selfDeletion(self):
        if self.isAlive is False and self in objects:
            objects.remove(self)

class Mob(Object):
    def __init__(self, pos, v, id, hp):
        super(Mob, self).__init__(pos, v, id, hp)
    
    def update(self):
        if self.id == 3:
            self.v.x = 2.5
            self.pos.x += self.v.x
        elif self.id == 4:
            self.v.y = 2.5
            self.pos.y += self.v.y
    
    def render(self):
        super(Mob, self).render()
        rect(self.pos.x, self.pos.y, 25, 25)

class Bullet(Object):
    def __init__(self, pos, v, id, hp):
        super(Bullet, self).__init__(pos, v, id, hp)
    
    def update(self):
        self.v.y = 5
        self.pos.y += self.v.y
    
    def render(self):
        super(Bullet, self).render()
        circle(self.pos.x, self.pos.y, 10)
    

class Player(Object):
    def __init__(self, pos, v, id, hp):
        super(Player, self).__init__(pos, v, id, hp)
        
    def update(self):
        if keyPressed:
            if key == "W" or key == "w":
                if self.pos.y > 0:
                    self.v.y = -5
                else:
                    self.v.y = 0
            elif key == "A" or key == "a":
                if self.pos.x > 15:
                    self.v.x = -5
            elif key == "S" or key == "s":
                if self.pos.y < 785:
                    self.v.y = 5
            elif key == "D" or key == "d":
                if self.pos.x < 785:
                    self.v.x = 5
            
            if not (key == "W" or key == "w") and not (key == "S" or key == "s"):
                self.v.y = 0
            if not (key == "A" or key == "a") and not (key == "D" or key == "d"):
                self.v.x = 0
            
            self.pos.x += self.v.x
            self.pos.y += self.v.y
                            
    def render(self):
        super(Player, self).render()
        triangle(self.pos.x, self.pos.y, self.pos.x + 15, self.pos.y + 15, self.pos.x - 15, self.pos.y + 15)
        text(self.hp, 25, 25)
