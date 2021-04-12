from graph import *
from random import randint


def Win():
    global Snake
    brushColor('white')
    penColor('white')
    Snake = rectangle(0, 0, 0, 0)
    rectangle(0, 0, 500, 500)
    penColor('black')
    brushColor('black')
    polygon([(40, 180), (60, 180), (80, 280), (60, 280)])
    polygon([(80, 180), (100, 180), (80, 280), (60, 280)])
    polygon([(80, 180), (100, 180), (120, 280), (100, 280)])
    polygon([(120, 180), (140, 180), (120, 280), (100, 280)])
    polygon([(160, 180), (220, 180), (220, 200), (200, 200), (200, 260), (220, 260), (220, 280), (160, 280), (160, 260), (180, 260), (180, 200), (160, 200), (160, 180)])
    polygon([(240, 180), (260, 180), (300, 240), (300, 180), (320, 180), (320, 280), (300, 280), (260, 220), (260, 280), (240, 280), (240, 180)])


def Grass():
    global Speed, Difficulty
    brushColor('lawn green')
    penColor('lawn green')
    rectangle(0, 0, 400, 400)
    brushColor('lime green')
    penColor('lime green')
    for i in range(0, 20, 2):
        for j in range(0, 20,2):
            rectangle(j*20, i*20, j*20 + 20, i*20 + 20)
    for i in range(1, 20, 2):
        for j in range (1, 20, 2):
            rectangle(j * 20, i * 20, j * 20 + 20, i * 20 + 20)
    penColor('black')
    brushColor('ivory3')
    rectangle(0, 400, 80, 420)
    rectangle(80, 400, 160, 420)
    rectangle(160, 400, 240, 420)
    rectangle(240, 400, 320, 420)
    rectangle(320, 400, 400, 420)
    rectangle(400, 400, 420, 420)
    brushColor('dim gray')
    if Speed > 250:
        rectangle(0, 400, 80, 420)
    else:
        rectangle(80, 400, 160, 420)
    if Difficulty == 1:
        rectangle(160, 400, 240, 420)
    elif Difficulty == 2:
        rectangle(240, 400, 320, 420)
    elif Difficulty == 3:
        rectangle(320, 400, 400, 420)
    else:
        rectangle(400, 400, 420, 420)
    brushColor('green')
    circle(40, 410, 10)
    circle(200, 410, 10)
    brushColor('yellow')
    circle(280, 410, 10)
    brushColor('red')
    circle(120, 410, 10)
    circle(360, 410, 10)
    brushColor('white')
    circle(410, 410, 10)

def Eyes():
    global Snake, Movex, Movey, First_eye, Second_eye
    if Movex == 0 and Movey == -20:
        moveObjectTo(First_eye, xCoord(Snake[0]) + 3, yCoord(Snake[0]) + 2)
        moveObjectTo(Second_eye, xCoord(Snake[0]) + 14, yCoord(Snake[0]) + 2)
    elif Movex == 0 and Movey == 20:
        moveObjectTo(First_eye, xCoord(Snake[0]) + 3, yCoord(Snake[0]) + 14)
        moveObjectTo(Second_eye, xCoord(Snake[0]) + 14, yCoord(Snake[0]) + 14)
    elif Movex == -20 and Movey == 0:
        moveObjectTo(First_eye, xCoord(Snake[0]) + 3, yCoord(Snake[0]) + 4)
        moveObjectTo(Second_eye, xCoord(Snake[0]) + 3, yCoord(Snake[0]) + 14)
    elif Movex == 20 and Movey == 0:
        moveObjectTo(First_eye, xCoord(Snake[0]) + 14, yCoord(Snake[0]) + 4)
        moveObjectTo(Second_eye, xCoord(Snake[0]) + 14, yCoord(Snake[0]) + 14)


def Apple():
    global Snake, apple, Rotation, Movex, Movey
    Applex = randint(0, 19) * 20
    Appley = randint(0, 19) * 20
    moveObjectTo(apple, Applex, Appley)


def border():
    global Snake, Movex, Movey, Difficulty
    if Difficulty == 3:
        if yCoord(Snake[0]) == -20:
            brushColor('red')
            rectangle(0, 0, 500, 500)
        elif yCoord(Snake[0]) == 400:
            brushColor('red')
            rectangle(0, 0, 500, 500)
        elif xCoord(Snake[0]) == -20:
            brushColor('red')
            rectangle(0, 0, 500, 500)
        elif xCoord(Snake[0]) == 400:
            brushColor('red')
            rectangle(0, 0, 500, 500)
    if Difficulty == 1 or Difficulty == 2:
        if xCoord(Snake[0]) == 0 and yCoord(Snake[0]) == 0:
            Movex = 20
            Movey = 0
        elif xCoord(Snake[0]) == 380 and yCoord(Snake[0]) == 0:
            Movex = 0
            Movey = 20
        elif xCoord(Snake[0]) == 380 and yCoord(Snake[0]) == 380:
            Movex = -20
            Movey = 0
        elif xCoord(Snake[0]) == 0 and yCoord(Snake[0]) == 380:
            Movex = 0
            Movey = -20
        elif yCoord(Snake[0]) == 0:
            Movex = 20
            Movey = 0
        elif yCoord(Snake[0]) == 380:
            Movex = -20
            Movey = 0
        elif xCoord(Snake[0]) == 0:
            Movex = 0
            Movey = -20
        elif xCoord(Snake[0]) == 380:
            Movex = 0
            Movey = 20
        elif yCoord(Snake[0]) <= -20:
            Movex = 0
            Movey = 20
        elif yCoord(Snake[0]) >= 400:
            Movex = 0
            Movey = -20
        elif xCoord(Snake[0]) <= -20:
            Movex = 20
            Movey = 0
        elif xCoord(Snake[0]) >= 400:
            Movex = -20
            Movey = 0

def update():
    global Movex, Movey, Snake, apple, Difficulty, Spine, Ridge
    moveObjectBy(Snake[0], Movex, Movey)
    for k in range(len(Snake) - 1, 0, -1):
        newCoord = coords(Snake[k-1])
        moveObjectTo(Snake[k], newCoord[0], newCoord[1])
    for k in range(len(Ridge)):
        newCoord = coords(Snake[k])
        moveObjectTo(Ridge[k], newCoord[0] + 5, newCoord[1] + 5)
    for k in range(len(Spine)):
        dx = xCoord(Ridge[k]) - xCoord(Ridge[k + 1])
        dy = yCoord(Ridge[k]) - yCoord(Ridge[k + 1])
        newCoord = coords(Ridge[k])
        moveObjectTo(Spine[k], newCoord[0] - dx//2, newCoord[1] - dy//2)
    border()
    Eyes()
    if Difficulty == 2 or Difficulty == 3:
        for i in range(2, len(Snake)):
            i = Snake[i]
            if coords(i) == coords(Snake[1]):
                brushColor('red')
                Snake = rectangle(0, 0, 0, 0)
                rectangle(0, 0, 500, 500)
    for i in Snake:
        if coords(i) == coords(apple):
            New_Snake_x = xCoord(Snake[-1])
            New_Snake_y = yCoord(Snake[-1])
            penColor('gray60')
            brushColor('gray60')
            Snake.append(rectangle(New_Snake_x, New_Snake_y, New_Snake_x + 20, New_Snake_y + 20))
            penColor('gray25')
            brushColor('gray25')
            Ridge.append(rectangle(New_Snake_x + 5, New_Snake_y + 5, New_Snake_x + 15, New_Snake_y + 15))
            Spine.append(rectangle(-10, -10, 0, 0))
            penColor('black')
            brushColor('red')
            rectangle(400, 0, 420, len(Snake))
            Apple()
            if len(Snake) == 400:
                Win()


def keyPressed(event):
    global Movex, Movey, Difficulty
    if event.keycode == VK_UP:
        Movex = 0
        Movey = -20
    elif event.keycode == VK_DOWN:
        Movex = 0
        Movey = 20
    elif event.keycode == VK_LEFT:
        Movex = -20
        Movey = 0
    elif event.keycode == VK_RIGHT:
        Movex = 20
        Movey = 0
    if Difficulty != 2 and Difficulty != 3:
        if event.keycode == VK_SPACE:
            Movex = 0
            Movey = 0


def Start():
    global Speed, Difficulty
    Speed = 500
    Difficulty = 500
    brushColor('black')
    Speed = int(input('Speed: '))
    Difficulty = int(input('Difficulty LVL(1 - 3): '))
    Main()


def Main():
    global Snake, apple, Movex, Movey, First_eye, Second_eye, Ridge, Speed, Spine
    Snake = []
    Ridge = []
    Spine = []
    Grass()
    brushColor('green')
    rectangle(400, 0, 420, 400)
    penColor('DeepPink3')
    brushColor('DeepPink3')
    apple = circle(-20, -20, 10)
    penColor('gray25')
    brushColor('gray25')
    Snake.append(rectangle(20, 0, 40, 20))
    Snake.append(rectangle(0, 0, 20, 20))
    Ridge.append(rectangle(5, 5, 15, 15))
    brushColor('black')
    penColor('black')
    First_eye = circle(-10, - 10, 2)
    Second_eye = circle(-10, - 10, 2)
    Apple()
    Movex = 0
    Movey = 0
    onKey(keyPressed)
    onTimer(update, Speed)
    run()


Start()
