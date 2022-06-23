from math import sqrt
import random
import turtle


def rand_point_on_line(start: tuple, end: tuple):
    start_x, start_y = start
    end_x, end_y = end
    # y = mx + c
    m = (end_y - start_y) / (end_x, start_x)
    c = start_y - m * start_x

    rand_x = random.randint(start_x, end_x)
    return (m * rand_x + c, rand_x)


def gen_tri_points(side_length, centre):
    centre_x, centre_y = centre
    a = (centre_x,centre_y+(sqrt(3)/3)*side_length)
    b = (centre_x-(side_length/2),centre_y-(sqrt(3)/6)*side_length)
    c = (centre_x+side_length/2, centre_y-(sqrt(3)/6)*side_length)
    return [a,b,c]

def midpoint(a, b):
    a_x, a_y = a
    b_x, b_y = b

    return ((a_x+b_x)/2, (a_y+b_y)/2)

def main():
    # Initialize screen
    s = turtle.getscreen()
    s.screensize(1000,800)
    s.tracer(0,0)
    #s.setworldcoordinates(0,0,500,500)

    # Initialize turtle
    t = turtle.getturtle()
    t.speed("fastest")
    t.width(0.05)

    side_length = 1000
    centre=(0,-150)
    tpoints = gen_tri_points(side_length, centre)
    a, b, c = tpoints

    # Draw triangle
    t.penup()
    t.goto(a)
    t.dot()
    t.goto(b)
    t.dot()
    t.goto(c)
    t.dot()
    t.goto(a)

    iterations = 200000
    count = 0
    while count < iterations:
        if count % 10000 == 0:
            s.update()
        count += 1
        # print(f"iterations: {count}")
        point = random.choice(tpoints)
        t.goto(midpoint((t.xcor(), t.ycor()), point)) # move turtle halfway to point a, b or c
        t.dot() # draw a dot

    #s.update()
    print("complete")
    s.mainloop()


if __name__ == "__main__":
    main()