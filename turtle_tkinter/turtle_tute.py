#亀が走り回ってる画像が描ける

import turtle

turtle.pencolor('green')
# turtle.color('red', 'yellow')
for i in range(60):
    # turtle.forward(100 + i * 10)
    # turtle.right(360 / 5 * 2)
    turtle.fd(50)
    turtle.left(360/3 + 10)
turtle.end_fill()
turtle.done()