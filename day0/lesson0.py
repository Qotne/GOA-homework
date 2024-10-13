from turtle import*

#we want to paint a castle

#step 1: draw a square
speed(30)
width(7)
color("gray")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawin a door

forward(70)
color("yellow")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("gray")
right(150)
forward(200)
left(120)
forward(200)
left(20)

penup()
goto(0,0)
pendown()
color("gray")
begin_fill()
forward(150)
left(100)
forward(250)
left(99)
forward(150)
end_fill()




exitonclick()