"""

Cannon, hitting targets with projectiles.

"""

# Librerias que van a estar siendo usadas
from random import randrange
from turtle import *

from freegames import vector

# Posicion inicial del balon
ball = vector(-200, -200)
# Vector de velocidad para el balon
speed = vector(0, 0)
# Cosas a las que se le tiene que pegar
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    "Move ball and targets."
    # Ver si se va a agregar otro target
    if randrange(40) == 0:
        # Posicion aletoria en el eje y
        y = randrange(-150, 150)
        target = vector(200, y)
        # Agregarlo a la lista de proyectiles existente
        targets.append(target)

    # Movimiento de los target en x
    for target in targets:
        target.x -= 0.5

    # Generar movimiento del balon
    if inside(ball):
        # Modificar el valor del vector de velocidad para simular tiro parabolico
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    # Poblar targets de solo targets que no han sido golpeados
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Posicionar los elementos
    draw()

    # Por cada target, ver si ya llego al borde de la izquierda
    for target in targets:
        if not inside(target):
            # Si ese es el caso, posicionarlo en la salida derecha
            target.x = 200

    # Repetir cada 1 milisegundo
    ontimer(move, 1)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()