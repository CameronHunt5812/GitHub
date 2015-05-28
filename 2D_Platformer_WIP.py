from Tkinter import *

root = Tk()

info = Label(root, text = 'info')
info.pack(side = 'top')

drawpad = Canvas(root, width=400, height=400)
drawpad.pack()

ground = drawpad.create_rectangle(0, 380, 410, 410, fill = 'green')
ob1 = drawpad.create_rectangle(200, 280, 250, 340)
ob2 = drawpad.create_rectangle(120, 320, 180, 340)
ob3 = drawpad.create_rectangle(30, 250, 100, 280)
ob4 = drawpad.create_rectangle(100, 200, 160, 230)
ob5 = drawpad.create_rectangle(300, 150, 340, 160)
ob6 = drawpad.create_rectangle(180, 200, 240, 220)
#ob7 = drawpad.create_rectangle(, , , )

objects = [ground, ob1, ob2, ob3, ob4, ob5]

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

def end (iput):
    root.destroy()

root.bind('<Key>', KeyStorage)
root.bind('<space>', hop)
root.bind('<Escape>', end)

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
    px1, py1, px2, py2 = drawpad.coords(player)
    for i in (objects):
        ox1, oy1, ox2, oy2 = drawpad.coords(i)
        if ((px1 > ox1 and px1 < ox2) or (px2 > ox1 and px2 < ox2)):
            if (py1 < oy2) and (py2 > oy2):
                drawpad.move(player, 0, oy2 - py1)
                airTime = 0

            if (py2 >= oy1) and (py1 < oy1):
                drawpad.move(player, 0, oy1 - py2)
                airTime = 0
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

animate()
mainloop()