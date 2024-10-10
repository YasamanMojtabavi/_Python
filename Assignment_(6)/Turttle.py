import turtle
p=turtle.Pen()
p.width(2)
colors=["orange","red","purple","blue","green","yellow"]
j=10
h=1.5
z=0
for n in range(3,80):
 angle = ((n-2)*180)/n
 p.left(180-(angle/2))
 if z<len(colors):
   p.pencolor(colors[z])
 else:
   z=0
   p.pencolor(colors[z])
 z+=1
 j=j+5
 h+=2.153
 for i in range(n,0,-1):
  p.forward(j)
  p.left(180-angle)
 p.right(180-(angle/2))
 p.penup()
 p.forward(h)
 p.down()

turtle.done()
