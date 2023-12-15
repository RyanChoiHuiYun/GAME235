class Object(object):
    def __init__(self, pos, v, id, hp):
        self.pos = pos
        self.v = v
        self.id = id
        self.hp = hp
    
    def render(self):
        return
    
    def update(self):
        return

# mob class also has bullets[Bullet]
# TODO: currently bullet rendering logic does not work in mob class
class Mob(Object):
    def __init__(self, pos, v, id, hp):
        super(Mob, self).__init__(pos, v, id, hp)
        self.bullets = []
    
    def bulletDeletion(self):
        for b in self.bullets:
            if b.hp <= 0:
                self.bullets.remove(b)
            if self.isOffScreen(b.pos) is not 0:
                self.bullets.remove(b)
    def isOffScreen(self, pos):
        if pos.x < 0:
            return 1
        elif pos.y > 800:
            return 2
        elif pos.x > 800:
            return 3
        elif pos.y < 0:
            return 4
        return 0
    
    def update(self):
        tempPos = self.pos
        if self.id == 3:
            self.v.x = 2.5
            self.pos.x += self.v.x
            if len(self.bullets) < 1:
                bullet = Bullet(tempPos, PVector(0,0), 1, 1)
                self.bullets.append(bullet)
            self.bulletDeletion()
        
        elif self.id == 4:
            self.v.y = 5
            self.pos.y += self.v.y
    
    def render(self):
        super(Mob, self).render()
        rectMode(CENTER)
        noStroke()
        if self.id == 3:
            fill(255)
            rect(self.pos.x, self.pos.y, 25, 25)

        elif self.id == 4:
            fill(128)
            quad(self.pos.x - 25, self.pos.y - 25, 
                 self.pos.x - 25, self.pos.y + 25,
                 self.pos.x + 25, self.pos.y - 25,
                 self.pos.x + 25, self.pos.y + 25)

class Bullet(Object):
    def __init__(self, pos, v, id, hp):
        super(Bullet, self).__init__(pos, v, id, hp)
    
    def update(self):
        if self.id == 0:
            self.v.y = -20
            self.pos.y += self.v.y
        elif self.id == 1:
            self.v.y = 10
            self.pos.y += self.v.y
    
    def render(self):
        super(Bullet, self).render()
        fill(255, 0, 0)
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
                else:
                    self.v.x = 0
            elif key == "S" or key == "s":
                if self.pos.y < 785:
                    self.v.y = 5
                else:
                    self.v.y = 0
            elif key == "D" or key == "d":
                if self.pos.x < 785:
                    self.v.x = 5
                else:
                    self.v.x = 0
            
            if not (key == "W" or key == "w") and not (key == "S" or key == "s"):
                self.v.y = 0
            if not (key == "A" or key == "a") and not (key == "D" or key == "d"):
                self.v.x = 0
            
            self.pos.x += self.v.x
            self.pos.y += self.v.y
                            
    def render(self):
        super(Player, self).render()
        fill(255, 255, 0)
        triangle(self.pos.x, self.pos.y, self.pos.x + 15, self.pos.y + 15, self.pos.x - 15, self.pos.y + 15)
