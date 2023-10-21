import turtle
t=turtle.Pen()

colors=['red','yellow','blue','green','purple']
for i in range(0,50):
    t.write("6",font=("Arial",int(i+5/5),"bold"))
    t.pencolor(colors[i%5])
    t.penup()
    t.forward(i*8)
    t.pendown()
    t.left(74)