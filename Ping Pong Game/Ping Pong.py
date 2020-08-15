import turtle

#make GUI window for game
wind=turtle.Screen()
#set Title of window
wind.title("Ping Pong Game")
#Set background Color of window
wind.bgcolor("black")

#set Width and height of window
wind.setup(width=800,height=600)
#stop the window from updating automatically
wind.tracer(0)


#Ball_racket1
import turtle
Racket1=turtle.Turtle() #initalizes Turtle object
Racket1.speed(0) #set speed of the animation
Racket1.shape("square") #Type of object
Racket1.color("Blue") #Color of object
Racket1.shapesize(stretch_wid=5,stretch_len=1) #Size of the object
Racket1.penup() #Stop object from drawing lines
Racket1.goto(-350,0) #set position of the object (X,Y)

#Ball_racket2
Racket2=turtle.Turtle()
Racket2.speed(0)
Racket2.shape("square")
Racket2.color("Red")
Racket2.shapesize(stretch_wid=5,stretch_len=1)
Racket2.penup()
Racket2.goto(350,0)

#Ball
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx=0.2 #to move ball 2.5 pixels in +x coordinate
Ball.dy=0.2 #to move ball 2.5 pixels in +y coordinate

# Scores
score1=0
score2=0
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle() # To view Text that write in object not object like ball and Rackets !
score.goto(0,260)
score.write("Player1:0                     Player2:0",align="center",font=("Courier",24,"normal"))

#Fuctions
def Racket1_up():
    y=Racket1.ycor() #get Y coordinate
    y+=20 # increase Y by 20
    Racket1.sety(y) #set Y of Rocket1 to new coordinate

def Racket1_down():
    y=Racket1.ycor()
    y-=20 # decrease Y by 20
    Racket1.sety(y)


def Racket2_up():
    y=Racket2.ycor()
    y+=20
    Racket2.sety(y)

def Racket2_down():
    y=Racket2.ycor()
    y-=20
    Racket2.sety(y)
#Window Binding

wind.listen() #Tell windows to expect keyboard input
wind.onkeypress(Racket1_up,"w") # when key 'w' is pressed then call function Racket1_up
wind.onkeypress(Racket1_down,"s") #when key 's' is pressed then call function Racket1_down

wind.onkeypress(Racket2_up,"Up")
wind.onkeypress(Racket2_down,"Down")


#game loop
while True:
    wind.update() #update screen every time loop run

    # Move the ball
    Ball.setx(Ball.xcor()+Ball.dx) #Ball start at 0 axis and every time loop run  increase +0.2 x axis
    Ball.sety(Ball.ycor() + Ball.dy) #Ball start at 0 axis and every time loop run  increase +0.2 y axis

    #Border Check Y axis
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1


    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1

    # Border Check X axis
    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score1+=1
        score.clear()
        score.write("Player1:{}                    Player2:{}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() <-390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1:{}                    Player2:{}".format(score1, score2), align="center",font=("Courier", 24, "normal"))

    #Crash Ball and Rackets
    if(Ball.xcor()>340 and Ball.xcor()<350) and (
            Ball.ycor()<Racket2.ycor()+40 and Ball.ycor()>Racket2.ycor()-40 ):
        Ball.setx(340)
        Ball.dx*=-1

    if (Ball.xcor() > -340 and Ball.xcor() < -350) and(
        Ball.ycor() < Racket1.ycor() + 40 and Ball.ycor() > Racket1.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
