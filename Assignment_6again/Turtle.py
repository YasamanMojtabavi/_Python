import turtle

t=turtle.Pen()
colors=["green","yellow","orange","red","pink","hot pink","fuchsia","purple","blue","Teal","lime"]
t.width(2)
h=1.5
j=10

for n in range(3,80):
    t.pencolor(colors[n%11])
    angle = ((n-2)*180)/n
    t.left(180-(angle/2))
    j+=5
    h+=2.05
    for i in range(n,0,-1):
        t.forward(j)
        t.left(180-angle)
    t.right(180-(angle/2))
    t.penup()
    t.forward(h)
    t.down()

        

turtle.done()