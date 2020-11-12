import turtle
# Черепашка пишет фразу разными цветами
turtle.shape('turtle')
turtle.speed(1)
turtle.pensize(2)
turtle.lt(90)
turtle.fd(50)
colors = ['red', 'orange', 'yellow', 'green', 'skyblue', 'blue', 'purple']
for i in colors:
    turtle.color(i)
    turtle.write('Какого цвета я сейчас?')
    turtle.fd(35)
# Дополнительное задание
turtle.reset()
turtle.speed(1)
turtle.up()
turtle.write('I start at 0. 0')
for y in [-100, 100]:
    for x in [-100, 100]:
        turtle.goto(x, y)
        turtle.write('This is ' + str(x) + '. ' + str(y))
turtle.goto(-100, 0)
turtle.down()
# Черепашка пишет введенное имя выбранным цветом
turtle.reset()
turtle.hideturtle()
name = str(input('Как Вас зовут? '))
color = str(input('Какой Ваш любимый цвет?'))
turtle.color(color)
turtle.write(name, False, align="center", font=('Times New Roman', 60, 'italic'))

turtle.exitonclick()