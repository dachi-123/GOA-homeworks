from turtle import *


#we want to paint a house



print("Dachi Tavadze")
#step 1:  draw a square

speed(30)
width(5)
color("red")
forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of squere
 
 #drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

left(30)
color("red")
forward(70)
left(90)

begin_fill()
color("red")

penup()
pendown()
forward(50)

left(90)
forward(50)
right(-90)
forward(50)
end_fill()

penup()
right(180)
forward(150)

begin_fill()

pendown()
forward(50)
right(90)

forward(50)
color("red")
left(-90)
forward(50)
right(90)
forward(50)
end_fill()








exitonclick()