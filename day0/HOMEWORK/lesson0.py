from turtle import*

#we want to paint a castle

#step 1: draw a square
speed(10)
width(7)
color("gray")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
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


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
left(20)
end_fill()

color("red")
begin_fill()
penup()
goto(20 , 170)
left(10)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

penup()
goto(175 , 170 )
pendown()
color("red")
begin_fill()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()



exitonclick()