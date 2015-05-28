from Tkinter import *

root = Tk()
drawpad = Canvas(root, width=400, height=400)
drawpad.pack()

ground = drawpad.create_rectangle(0, 380, 410, 410, fill = 'green')
obstical1 = drawpad.create_rectangle(200, 320, 250, 330)
obstical2 = drawpad.create_rectangle(120, 300, 180, 310)
obstical3 = drawpad.create_rectangle(80, 250, 100, 260)
obstical4 = drawpad.create_rectangle(130, 230, 160, 250)
objects = [ground, obstical1, obstical2, obstical3, obstical4]

player = drawpad.create_rectangle(120, 360, 130, 380, fill = 'red')

ground = False
airTime = 0
xDir = 0
derection = 0
key = None

print 'you are the red rectangle'
print 'hold A or D to move leaft or right'
print 'use "space" to jump'



def hop(space):
    global ground
    global airTime
    if ground == True:
        airTime = -17
        drawpad.move(player, 0, -1)
        ground = False

def KeyStorage (c):
    global key
    key = c.char

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
    global airTime
    global ground
    if ground != True:
        airTime = airTime + 1
        yVelosity = (airTime**3) / 350
        drawpad.move(player, xDir, 0)
    else:
        yVelosity = 0
        
    if yVelosity >= 8:
        airTime = 14
    drawpad.move(player, 0, yVelosity)
    
def collisionDetect ():
    global player
    global ground
    global airTime
    global xDir
    temp = False
    for i in (objects):
        px1, py1, px2, py2 = drawpad.coords(player)
        ox1, oy1, ox2, oy2 = drawpad.coords(i)
        if ((px1 > ox1 and px1 < ox2) or (px2 > ox1 and px2 < ox2)):
            if (py1 < oy2) and (py2 > oy2):
                drawpad.move(player, 0, oy2 - py1)
                airTime = 0

            if (py2 >= oy1) and (py2 < oy2):
                drawpad.move(player, 0, oy1 - py2)
                airTime = 0
                #xDir = 0
                temp = True
            else:
                ground = False

        if (py1 > oy1 and py1 < oy2) or (py2 > oy1 and py2 < oy2):
            if px1 <= ox2 and px2 >= ox2:
                drawpad.move(player, (ox2 - px1) + 1, 0)

            if px2 >= ox1 and px1 <= ox1:
                drawpad.move(player, (ox1 - px2) - 1, 0)

        if (temp == True):
            ground = True

def animate():
    gravity()
    derection = KeyInput(key)
    drawpad.move(player,derection,0)
    collisionDetect()
    root.after(2, animate)

#information()
animate()
mainloop()
root.destroy()