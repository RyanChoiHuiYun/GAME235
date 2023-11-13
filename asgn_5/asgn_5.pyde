# Ryan Cai
# 11/13/2023
# https://www.kenney.nl/assets/map-pack

WINDOW_WIDTH = 680
WINDOW_HEIGHT = 680
GRID_SIZE = 24
CELL_SIZE = WINDOW_WIDTH / GRID_SIZE
SAVE_FILE = "tempsave.txt"

assets = ["character.png", "tile1.png", "tile2.png", 
          "tile3.png", "tile4.png", "tile5.png"]
currentTile = 0
tilePos = []
tileColor = []
saveState = False

def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    background(255)
    
def draw():
    global currentTile, tilePos, tileColor, saveState
    background(255)
    textSize(15)
    fill(0)
    text("Press R to reset", 0, 15)
    text("Press F to save a screenshot", 0, 30)
    text("Press S to save tile map", 0, 45)
    text("Press L to load tile map", 0, 60)
    text("Click to place tiles", WINDOW_WIDTH - 200, 15)
    text("Use <- or -> to change textures", WINDOW_WIDTH - 200, 30)
    if keyPressed:
        if keyCode == RIGHT:
            currentTile += 1
        elif keyCode == LEFT:
            currentTile -= 1
        elif key == "R" or key == "r":
            tilePos = []
            tileColor = []
        elif key == "S" or key == "s":
            saveState = True
            if saveState == True:
                saveTile()
        elif key == "L" or key == "l":
            tilePos = []
            tileColor = []
            loadTile(loadStrings(SAVE_FILE))
        elif key == "F" or key == "f":
            save("screenshot.png")
            
    currentTile = currentTile % len(assets)
    
    tile = loadImage(assets[currentTile])
    tint(255, 126)
    imageMode(CENTER)
    image(tile, mouseX, mouseY, CELL_SIZE, CELL_SIZE)
    for i in range(len(tilePos)):
        tile = loadImage(tileColor[i])
        noTint()
        imageMode(CORNER)
        image(tile, tilePos[i][0], tilePos[i][1], CELL_SIZE, CELL_SIZE)
        
    
def mousePressed():
    tempPos = PVector(mouseX - (mouseX % CELL_SIZE), mouseY - (mouseY % CELL_SIZE))
    tilePos.append(tempPos)
    tileColor.append(assets[currentTile])
    
def saveTile():
    saveData = []
    for i in range(len(tilePos)):
        row = str(tilePos[i][0]) + "," + str(tilePos[i][1]) + "," + str(tileColor[i])
        saveData.append(row)
    saveStrings("data/" + SAVE_FILE, saveData)
    saveState = False
    
def loadTile(data):
    for row in data:
        rowList = row.split(",")
        tilePos.append(PVector(float(rowList[0]), float(rowList[1])))
        tileColor.append(rowList[2])
