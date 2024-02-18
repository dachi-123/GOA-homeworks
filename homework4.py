from turtle import *



speed(1000)
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
right(-90)
penup()
forward(150)
left(90)
forward(180)
right(90)
pendown()
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

#drawing a door
forward(70)

color("green")
begin_fill()
right(90)
forward(100)     #heght of a door
left(90)       
forward(50)
left(90)
forward(100)
end_fill()

color("red")
right(90)
forward(80)
right(90)
forward(130)

# drawing windows



right(90)
begin_fill()
color("red")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
 
#drawing second window

penup()
begin_fill()
color("red")
right(-180)
forward(150)
pendown()
forward(50)
right(90)

forward(50)
left(-90)
forward(50)
right(90)
forward(50)
end_fill()

#drawing roof

right(90)
forward(50)
left(90)
forward(20)

begin_fill()
color("yellow")
right(-30)
forward(200)

left(120)
forward(200)
end_fill()

color("red")
right(-30)
forward(200)

right(90)

penup()

right(45)
forward(300)
color("yellow")
pendown()

left(45)
right(90)
begin_fill()
color("yellow")
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
end_fill()

#drawing yard

begin_fill()
color("Green")
left(90)
penup()
forward(230)
right(90)
forward(60)
pendown()
left(90)
forward(375)
left(90)
forward(950)
left(90)
forward(389)
left(90)
forward(950)
left(90)
forward(110)
end_fill()


exitonclick()
















