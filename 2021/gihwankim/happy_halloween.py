import turtle 

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_background():
    color='#660099'
    turtle.Screen().bgcolor(color)

def draw_face():
    color='#ff7518'
    move(0,-100)    
    t.fillcolor(color)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    
def draw_eyes():
    color='#000000'
    def draw_eye(x,y):
        move(x,y)
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(3):
            t.forward(50)
            t.left(120)
        t.end_fill()
    
    draw_eye(25,20)
    draw_eye(-75,20)
    
def draw_nose():
    color='#000000'
    move(-20,-10)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

def draw_mouth():
    color='#000000'
    t.fillcolor(color)
    
    for step in range(5):
        move(-50+20*step,-30)
        t.begin_fill()
        for _ in range(3):
            t.forward(20)
            t.right(120)
        t.end_fill()
        
    for step in range(5):
        move(-50+20*step,-70)
        t.begin_fill()
        for _ in range(3):
            t.forward(20)
            t.left(120)
        t.end_fill()

def halloween_messages():
    color='#FBFCF8'
    font=('bold',50,'underline')
    move(-200,200)
    t.color(color)
    t.write('PsedoLab',font=font)
    move(-200,-200)
    t.write('Happy Halloween!!',font=font)
    

    
if __name__ == "__main__":
    
    t=turtle.Turtle()
    t.shape('turtle')
    draw_background()
    draw_face()
    draw_eyes()
    draw_nose()
    draw_mouth()
    halloween_messages()
    turtle.exitonclick()
    

