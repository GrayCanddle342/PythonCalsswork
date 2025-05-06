import turtle  #importing libary
turtle.Screen().bgcolour("Blue")
turtle.Screen().setup(300,000)
pologon = turtle.Turtle() #defined variable

num_sides = 6 #variable
side_length = 70
angle =360.0 / num_sides
#inrate the loop for total of number of sides
for i in range(num_sides):
    pologon.forward(side_length)
    pologon.right(angle)

turtle.done()