"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, SnakeColor)

    square(food.x, food.y, 9, FoodColor)
    update()
    ontimer(move, 100)

# Función para generar colores Aleatorios
def colorAleatorio():
    ListaColores = ['Black','Green','Yellow','Blue','Magenta','Cyan'] # Banco de Colores
    Posicion = randrange(0,5) # Se genera una posición aleatoria dentro del rango de la lista de colores
    return ListaColores[Posicion] # Se regresa el color con la posición aleatoria

SnakeColor = colorAleatorio() # Se genera el color de la serpient de manera aleatoria
FoodColor = colorAleatorio() # Se genera el color de la comida de manera aleatoria

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
