import turtle

def draw_tree(depth,length,angle):
    if depth>0:
        t.forward(length)
        t.left(angle)
        draw_tree(depth-1,length*0.75,angle)
        t.right(angle+angle)
        draw_tree(depth-1,length*0.75,angle)
        t.left(angle)
        t.backward(length)
t=turtle.Turtle()
t.setheading(90)
draw_tree(10,100,30)
