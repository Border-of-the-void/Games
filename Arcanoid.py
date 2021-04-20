from graph import *
from random import randint


def Targets_Destroy():
    global Targets, Ball, Movex, Movey, Number
    for i in Targets:
        if yCoord(i) != -40:
            if xCoord(i) - 1 < xCoord(Ball) < xCoord(i) + 41 and yCoord(i) - 1 < yCoord(Ball) < yCoord(i) + 41:
                if yCoord(i) + 39 < yCoord(Ball) < yCoord(i) + 41:
                    Movey = 0.5
                    moveObjectBy(i, 0, -yCoord(i)-40)
                elif yCoord(i) - 1 < yCoord(Ball) < yCoord(i) + 1:
                    Movey = -0.5
                    moveObjectBy(i, 0, -yCoord(i) - 40)
                elif xCoord(i) + 39 < xCoord(Ball) < xCoord(i) + 41:
                    Movex = 0.5
                    moveObjectBy(i, 0, -yCoord(i)-40)
                elif xCoord(i) - 1 < xCoord(Ball) < xCoord(i) + 1:
                    Movex = -0.5
                    moveObjectBy(i, 0, -yCoord(i) - 40)



    for i in range(10):
        if yCoord(Targets[i]) < 0:
            Number += 1
    if Number >= 9:
        for k in Targets:
            moveObjectBy(k, 0, 40)
    Number = 0
    for i in range(0, 20):
        if yCoord(Targets[i]) < 0:
            Number += 1
    if Number >= 9:
        for k in Targets:
            moveObjectBy(k, 0, 40)
    Number = 0
    for i in range(0, 30):
        if yCoord(Targets[i]) < 0:
            Number += 1
    if Number >= 9:
        for k in Targets:
            moveObjectBy(k, 0, 40)
    Number = 0


def update():
    global Movex, Movey, Flatx
    moveObjectBy(Flat, Flatx, 0)
    moveObjectBy(Ball, Movex, Movey)
    if Started == False:
        moveObjectBy(Ball, Flatx, 0)
    Targets_Destroy()
    border()
    Lose()


def Lose():
    global Targets
    for i in Targets:
        if yCoord(i) >= 360:
            brushColor('red')
            rectangle(0, 0, 500, 500)
            for i in Targets:
                moveObjectBy(i, 1000, 1000)


def keyPressed(event):
    global Flatx, Movex, Movey, Started
    if event.keycode == VK_DOWN:
        Flatx = 0
    elif event.keycode == VK_LEFT:
        Flatx = -0.5
    elif event.keycode == VK_RIGHT:
        Flatx = 0.5
    if event.keycode == VK_UP and Started == False:
        Started = True
        x = randint(1, 2)
        if x == 1:
            x = -0.5
        else:
            x = 0.5
        Movex = x
        Movey = -0.5


def border():
    global Flatx, Movex, Movey, Started
    if xCoord(Flat) == 0:
        Flatx = 0
    if xCoord(Flat) <= -1:
        Flatx = 0.5
    if xCoord(Flat) == 300:
        Flatx = 0
    if xCoord(Flat) >= 301:
        Flatx = -0.5


    if xCoord(Ball) <= 0:
        Movex = 0.5
    if xCoord(Ball) >= 380:
        Movex = -0.5
    if yCoord(Ball) <= 0:
        Movey = 0.5
    if yCoord(Ball) >= 400:
        Movex = 0
        Movey = 0
        moveObjectBy(Ball, xCoord(Flat) - xCoord(Ball) + 40, yCoord(Flat) - yCoord(Ball) - 10)
        Started = 0
    if yCoord(Flat) + 25 >= yCoord(Ball) >= yCoord(Flat) and xCoord(Flat) <= xCoord(Ball) <= xCoord(Flat) + 100:
        Movey = -0.5
        Movex += Flatx / 2


def Start():
    global Number, Targets, Started, Movex, Movey, Flatx, Flat, Ball
    Number = 0
    Targets = []
    Started = 0
    Movex = 0
    Movey = 0
    Flatx = 0
    brushColor('cyan')
    rectangle(0, 0, 400, 400)
    brushColor('white')
    for i in range(0, 400, 40):
        Targets.append(rectangle(i, 0, i + 40, 40))
    for i in range(0, 400, 40):
        Targets.append(rectangle(i, 40, i + 40, 80))
    for i in range(0, 400, 40):
        Targets.append(rectangle(i, 80, i + 40, 120))
    Flat = rectangle(150, 375, 250, 400)
    Ball = circle(200, 375, 10)
    onKey(keyPressed)
    onTimer(update, 1)
    run()


Start()
