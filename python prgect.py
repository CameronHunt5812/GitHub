f = open("C:\Users\S581267\Documents\python progect",'r')


line3 = 3
lookFore = [0 for w in range(line3)]
hith = f.readline()
width = 5
position = [[0 for x in range(width)]for y in range(hith)]
for y in range (len(position)):
    for x in range (len(position[y])):
        letter = "entb"#pull data from docum
        position[y][x] = letter 

                