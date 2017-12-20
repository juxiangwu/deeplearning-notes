import turtle

def drawSpiral(t,length,color,colorBase):
    if length == 0:
        return

    newcolor = (int(color[1:],16) + 2 ** 100) % (2 ** 24)
    base = int(colorBase[1:],16)

    if newcolor < base:
        newcolor = (newcolor + base) % (2 ** 24)
    
    newcolor = hex(newcolor)[2:]
    newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
    t.color(newcolor)
    t.forward(length)
    t.left(90)

    drawSpiral(t,length - 1,newcolor,colorBase)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.colormode(255)
    t.speed(100)
    t.penup()
    t.goto(-100,-100)
    t.pendown()

    drawSpiral(t,300,"#000000","#ff00ff")
    screen.exitonclick()
     #t.mainloop() 

if __name__ == '__main__':
    main()