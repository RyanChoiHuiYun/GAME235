# assets: https://www.kenney.nl/assets/map-pack

WINDOW_WIDTH = 680
WINDOW_HEIGHT = 680
GRID_SIZE = 24
CELL_SIZE = WINDOW_WIDTH / GRID_SIZE

assets = ["tile1.png", "tile2.png", "tile3.png", 
          "tile4.png", "tile5.png", "tile6.png"]
currentTile = 0
tilePos = []
tileColor = []


def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    background(255)
    #initGrid(GRID_SIZE, 3)

    
def draw():
    global currentTile, tilePos, tileColor
    background(255)
    
    if keyPressed:
        if keyCode == RIGHT:
            currentTile += 1
        elif keyCode == LEFT:
            currentTile -= 1
        currentTile = currentTile % len(assets)
    
    tile = loadImage(assets[currentTile])
    tint(255, 126)
    image(tile, mouseX, mouseY, CELL_SIZE / 2.5, CELL_SIZE / 2.5)
    
    for i in range(len(tilePos)):
        tile = loadImage(tileColor[i])
        noTint()
        image(tile, tilePos[i][0], tilePos[i][1], CELL_SIZE, CELL_SIZE)
        
    
def mousePressed():
    tempPos = PVector(mouseX - (mouseX % CELL_SIZE), mouseY - (mouseY % CELL_SIZE))
    tilePos.append(tempPos)
    tileColor.append(assets[currentTile])

def initGrid(gridSize, defaultTile):
    for i in range(gridSize):
        for j in range(gridSize):
            tile = loadImage(assets[defaultTile])
            image(tile, i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
