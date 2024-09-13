from graph import *
from random import randint

            
class Apple:
    x = 0
    y = 0
    obj = 0
    def GenerateApple():
        penColor('DeepPink3')
        brushColor('DeepPink3')
        Apple.obj = circle(-20, -20, 10)
        apple.x = randint(0, 19) * 20
        apple.y = randint(0, 19) * 20
        moveObjectTo(apple.obj, apple.x, apple.y)


    def MoveApple():
        apple.x = randint(0, 19) * 20
        apple.y = randint(0, 19) * 20
        space.ChangeLocate()
        moveObjectTo(apple.obj, apple.x, apple.y)


class Space:
    x = set()
    y = set()
    xBusy = set()
    yBusy = set()
    for i in range(0, 400, 20):
        x.add(i)
        y.add(i)

        
    def ChangeLocate():
        xBusy = set()
        yBusy = set()
        for k in range(len(snake.Body)):
            space.xBusy.add(xCoord(snake.Body[k]))
            space.yBusy.add(yCoord(snake.Body[k]))
        x = list(space.x - xBusy)
        y = list(space.y - yBusy)
        apple.x = x[randint(0, len(x)-1)]
        apple.y = x[randint(0, len(y)-1)]
        
        
class Snake:
    Body = []
    Movex = 0
    Movey = 0
    Eye1 = 0
    Eye1 = 0


    def Move():
        for k in range(len(Snake.Body) - 1, 0, -1): moveObjectTo(Snake.Body[k], xCoord(Snake.Body[k-1]), yCoord(Snake.Body[k-1]))
        moveObjectBy(Snake.Body[0], Snake.Movex, Snake.Movey)
        moveObjectBy(Snake.Eye1, Snake.Movex, Snake.Movey)
        moveObjectBy(Snake.Eye2, Snake.Movex, Snake.Movey)
        x = xCoord(Snake.Body[0])
        y = yCoord(Snake.Body[0])
        for k in range(2, len(Snake.Body)):
            if xCoord(Snake.Body[k]) == x and yCoord(Snake.Body[k]) == y:
                Snake.DeadSnake()
        if xCoord(Snake.Body[0]) == Apple.x and yCoord(Snake.Body[0]) == Apple.y:
            penColor('gray25')
            brushColor('gray25')
            Snake.Body.append(rectangle(xCoord(Snake.Body[-1]), yCoord(Snake.Body[-1]), xCoord(Snake.Body[-1]) + 20, yCoord(Snake.Body[-1]) + 20))
            Apple.MoveApple()

            
    def HeadCoordinates(): return xCoord(Snake.Body[0]), yCoord(Snake.Body[0])

    
    def DeadSnake(): moveObjectTo(Snake.Body[0], 1000, 1000)

    
    def GenerateSnake():
        penColor('gray25')
        brushColor('gray25')
        Snake.Body.append(rectangle(40, 0, 20, 20))
        Snake.Body.append(rectangle(0, 0, 20, 20))
        brushColor('black')
        penColor('black')
        Snake.Eye1 = circle(-10, - 10, 2)
        Snake.Eye2 = circle(-10, - 10, 2)

      
    def MoveU():
        Snake.Movex, Snake.Movey = 0, -20
        moveObjectTo(Snake.Eye1, xCoord(Snake.Body[0]) + 3, yCoord(Snake.Body[0]) + 2)
        moveObjectTo(Snake.Eye2, xCoord(Snake.Body[0]) + 14, yCoord(Snake.Body[0]) + 2)

        
    def MoveD():
        Snake.Movex, Snake.Movey = 0, 20
        moveObjectTo(Snake.Eye1, xCoord(Snake.Body[0]) + 3, yCoord(Snake.Body[0]) + 14)
        moveObjectTo(Snake.Eye2, xCoord(Snake.Body[0]) + 14, yCoord(Snake.Body[0]) + 14)

        
    def MoveL():
        Snake.Movex, Snake.Movey = -20, 0
        moveObjectTo(Snake.Eye1, xCoord(Snake.Body[0]) + 3, yCoord(Snake.Body[0]) + 4)
        moveObjectTo(Snake.Eye2, xCoord(Snake.Body[0]) + 3, yCoord(Snake.Body[0]) + 14)

        
    def MoveR():
        Snake.Movex, Snake.Movey = 20, 0
        moveObjectTo(Snake.Eye1, xCoord(Snake.Body[0]) + 14, yCoord(Snake.Body[0]) + 4)
        moveObjectTo(Snake.Eye2, xCoord(Snake.Body[0]) + 14, yCoord(Snake.Body[0]) + 14)


def update():
    onKey(Interpreter)
    snake.Move()
    Observer()
    

def Interpreter(event):
    if event.keycode == VK_UP: snake.MoveU()
    elif event.keycode == VK_DOWN: snake.MoveD()
    elif event.keycode == VK_LEFT: snake.MoveL()
    elif event.keycode == VK_RIGHT: snake.MoveR()


def Observer():
    x, y = snake.HeadCoordinates()
    if y <= -20 or y >= 400 or x <= -20 or x >= 400: snake.DeadSnake()
    
        
def Grass():
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


def Generation():
    global snake, apple, space
    Grass()
    snake, apple, space = Snake, Apple, Space
    snake.GenerateSnake()
    apple.GenerateApple()
    onTimer(update, 2000)
    run()


Generation()
