from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=400, height=400)
drawpad.pack()

ground = drawpad.create_rectangle(0, 380, 410, 410)
obstical = drawpad.create_rectangle(200, 340, 250, 380)
obstical2 = drawpad.create_rectangle(120, 300, 180, 310)
objects = [obstical2, ground, obstical]

player = drawpad.create_rectangle(120, 360, 130, 380)
ground = False
jumped = False
jump = False
airTime = 0
xDir = 0
derection = 0
key = None

def KeyStorage (c):
    global key
    key = c.char

def hop(space):
    global ground
    global airTime
    global jumped
    global jump
    if ground == True:
        airTime = -20
        drawpad.move(player, 0, -1)
        ground = False
        
root.bind("<Key>", KeyStorage)
root.bind("<space>", hop)

def KeyInput(Key):
    global key
    global xDir
    derection = 0
    if (key != None):
        if (key == 'a'):
            derection = -1
            xDir = -1
        elif (key == 'd'):
            derection = 1
            xDir = 1
        key = None
    return derection

def gravity():
    global jumped
    global airTime
    global ground
    if ground != True:
        airTime = airTime + 1
        yVelosity = (airTime**3) / 400
        drawpad.move(player, xDir, 0)
    else:
        yVelosity = 0
        
    if yVelosity >= 10:
        airTime = 15
    drawpad.move(player, 0, yVelosity)
    
def collisionDetect (i):
    global player
    global ground
    global airTime
    global xDir
    #for i in (objects): #Shuld this be for i in range (objects): ?
    px1, py1, px2, py2 = drawpad.coords(player)
    ox1, oy1, ox2, oy2 = drawpad.coords(i)
    if (py1 > oy1 and py1 < oy2) or (py2 > oy1 and py2 < oy2):
        if px1 <= ox2 and px2 >= ox2:
            drawpad.move(player, (ox2 - px1) + 1, 0)

        if px2 >= ox1 and px1 <= ox1:
            drawpad.move(player, (ox1 - px2) - 1, 0)

    if ((px1 > ox1 and px1 < ox2) or (px2 > ox1 and px2 < ox2)):
        if py1 < oy2 and py2 > oy2:
            drawpad.move(player, 0, oy2 - py1)
            airTime = 0

        if (py2 >= oy1) and (py2 <= oy2):
            drawpad.move(player, 0, oy1 - py2)
            airTime = 0
            #xDir = 0
            ground = True
        else:
            ground = False
        print ground

def animate():
    gravity()
    derection = KeyInput(key)
    drawpad.move(player,derection,0)
    for i in (objects):
        collisionDetect(i)   
    drawpad.after(1, animate)

animate()
mainloop()