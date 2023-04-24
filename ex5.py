# _*_ coding: utf-8 _*_

name = "Abhishek K. Singh"
age = 29
height = 69 # inches
weight = 75 # kilograms
eyes = "Brown"
teeth = "White"
hair = "Grey"


print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d kilograms heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to gret it exactly right
print("If I add %d, %d and %d, I get %d." % (age, height, weight, age + height + weight))