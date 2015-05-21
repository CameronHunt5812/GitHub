from Tkinter import *

root = Tk()

drawpad = Canvas(root, width=630, height=630, background='white')
drawpad.pack()
player = drawpad.create_line(20,20,80,20)
derection = 0
key = None
def KeyStorage (c):
    global key
    key = c.char

def KeyInput(Key):
    global key
    derection = 0
    if (key != None):
        if (key == 'a'):
            derection = -5
        elif (key == 'd'):
            derection = 5
        key = None
    return derection

def collisionDetect ():
    if 
    
def animate():
    derection = KeyInput(key)
    drawpad.move(player,derection,0)
    drawpad.after(10, animate)

root.bind("<Key>", KeyStorage)
root.bind("<Space>", jump)
animate()
root.mainloop()