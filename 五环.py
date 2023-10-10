
import turtle

pen = turtle.Pen()
pen.speed(10)
pen.pencolor('pink')
pen.pensize(5)
pen.circle(50)
pen.penup()
pen.forward(80)
pen.pendown()
pen.pencolor('black')
pen.circle(50)
pen.penup()
pen.forward(80)
pen.pendown()
pen.pencolor('red')
pen.circle(50)
pen.penup()
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.pendown()
pen.pencolor('green')
pen.circle(50)
pen.penup()
pen.forward(80)
pen.pendown()
pen.pencolor('yellow')
pen.circle(50)

# Write text
pen.penup()  # Lift the pen
pen.forward(160)  # Move the pen to a specified coordinate
pen.pendown()  # Put down the pen
pen.write('°×ÑÒËÉ', align='center', font=('ËÎÌå', '20'))  
pen.penup()  # Lift the pen
pen.forward(150)  # Move the pen to a specified coordinate
pen.pendown()  # Put down the pen
pen.write('222', align='center', font=('ËÎÌå', '20'))

turtle.done()
