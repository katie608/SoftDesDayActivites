def pascal(n, k):
    if k>1 and n > k:
        return pascal(n-1, k) + pascal(n-1, k-1)
    elif k == 1:
        return n
    elif k == n:
        return 1
    else:
        return "you have broken the law"

# print(pascal(5, 4))
import turtle
t = turtle.Turtle()
t.speed(0)

def snow_flake_side(turtle, length, level):
    """Draw a side of the snowflake curve with side length length and recursion
    depth of level"""
    # turtle.pendown()
    turtle.fd(length/3)
    turtle.lt(60)
    turtle.fd(length/3)
    turtle.rt(120)
    turtle.fd(length/3)
    turtle.lt(60)
    turtle.fd(length/3)
    turtle.lt(60)
    # turtle.penup()
    # t.setx(0)
    # t.sety(0)

def snow_flake(turtle, length, level):
    if level <= 1:
        snow_flake(turtle, length/3, level-1)
    else:
        snow_flake_side(turtle, length, level)


snow_flake(t, 400, 2)

turtle.mainloop()
