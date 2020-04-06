import turtle

X = int(input("Enter the size of the first line: "))
N = 3
org = turtle.Turtle()
org = turtle.Pen()
org.pensize(X)
org.speed(1)
window = turtle.Screen()
def draw_3_lines_2(h, g):
    # Get turtle t to draw three lines in wide 3, 30 units gap between each and 200 height.
    nuofLine = N
    for k in range (nuofLine):
        org.left(90)
        org.forward(h)
        org.penup()
        org.backward(h)
        org.right(90)
        org.forward(g)
        org.pendown()
        
def main():
    h = 200
    g = 30
    draw_3_lines_2(h,g)
    window.exitonclick()
if __name__ == '__main__':
    main()
    
