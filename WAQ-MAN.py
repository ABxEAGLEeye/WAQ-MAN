import turtle

#setting up screen properties
wn= turtle.Screen()
wn.title("WAQ-MAN")
wn.bgcolor("black")
wn.setup(height=550,width=550)
wn.tracer(0)

#score
score=0

#y=-40 line
arr1=[70,150,190,-90,-170,-210]
#y=-60 line
arr2=[-30,-50,-70,-9,-130,-210,10,30,50,70,110,150,190]
#y=-80 line
arr3=[-130,-210,110]
#y=-100 line
arr4=[-10,-50,-90,-210,-170,30,70,150,190]
#y=-120 line
arr5=[190,110,30,-10,-50,-130,-210]
#y=-140
arr6=[-210,170,130,-90,70,110,150,190]
#y=-160
arr7=[190,150,30,-50,-90,-170,-210]
#y=-180
arr8=[110,-10,-130,-210,190]
#y=-20
arr9=[30,70,110,150,190,-50,-130]
#y=0
arr10=[-50,30]
#y=40
arr11=[-210,-90,70,150,190]
#y=60
arr12=[190,150,110,70,10,-30,-90,-130,-170]
#y=80
arr13=[-130,-210,190,110]
#y=100
arr14=[70,150,190,-210,30,-50,-90,-170]
#y=120
arr15=[-210,-130,-50,30,110,190]
#y=140
arr16=[110,150,190,-10,-90,-130,-170,-210]
#y=160
arr17=[-170,-120,-90,-50,-10,30,70,150,190]
#y=180
arr18=[190,150,70,30,-50,130,-170]
#y=200
arr19=[-170,-130,70,110]
#y=20
arr20=[30,10,70,110,150,190,-30,-50,-90,-130]


#x=-10
row1=[-20,-100,-120,-160,100,140,160,200]

#x=10
row2=[-20,-60,-160,-200,20,60,100,200]

#x=30
row3=[-20,-60,-100,-120,-160,-200,60,20,100,120,160]

#x=50
row4=[-60,-200,60,200]

#x=70
row5=[-20,-60,-100,-140,-200,20,60,100,140]

#x=90
row6=[-100,100,-200]

#x=110
row7=[-20,-60,-140,-180,20,60,140,200]

#x=130
row8=[-20,-100,-200,20,100,200]

#x=150
row9=[-20,-60,-100,-140,-160,-200,20,60,100,140]

#x=170
row10=[-200,200]

#x=190
row11=[-20,-60,-100,20]

#x=-30
row12=[-20,-60,-160,-200,20,60,100,200]

#x=-50
row13=[-20,-60,-100,-120,-160,-200,60,20,100,120,160]

#x=-70
row14=[-60,-200,60,200]

#x=-90
row15=[-20,-60,-100,-140,-200,20,60,100,140,160]

#x=-110
row16=[-100,100,-200]

#x=-130
row17=[-20,-60,-140,-180,20,60,140,200]

#x=-150
row18=[-20,-100,-200,20,100,200]

#x=-170
row19=[-20,-40,-100,-140,-160,-200,20,60,100,140]

#x=-190
row20=[-200,160,200]

#x=-210
row21=[-20,20]


#walls segment 1 top right hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=2,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(20,20)

#walls segment 1 top left hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=2,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-40,20)

#wall segment right vert 1
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(30,0)

#wall segment left vert 1
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-50,0)

#wall segment center bottom hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-10,-20)

#2nd ring

#wall segment 2nd ring right top ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(70,40)

#wall segment 2nd ring left top ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(-90,40)

#wall segment 2nd ring right top hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=4,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(40,60)

#wall segment 2nd ring left top hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=4,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-60,60)


#wall segment 2nd ring left bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(-90,-40)

#wall segment 2nd ring left top hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=4,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-60,-60)

#wall segment 2nd ring right bottom hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=4,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(40,-60)

#wall segment 2nd ring right bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(70,-40)

#3rd ring

#wall segment 3rd ring top U hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-10,100)

#wall segment 3rd ring top U right ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(30,110)

#wall segment 3rd ring top U left ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-50,110)

#wall segment 3rd ring top right cross ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=5)
wall_cell.penup()
wall_cell.goto(110,100)

#wall segment 3rd ring top right cross hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(110,100)

#wall segment 3rd ring top left cross ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=5)
wall_cell.penup()
wall_cell.goto(-130,100)

#wall segment 3rd ring top left cross hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-130,100)


#wall segment 3rd ring bottom right cross ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=5)
wall_cell.penup()
wall_cell.goto(110,-100)

#wall segment 3rd ring bottom right cross hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(110,-100)

#wall segment 3rd ring bottom left cross ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=5)
wall_cell.penup()
wall_cell.goto(-130,-100)

#wall segment 3rd ring bottom left cross hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-130,-100)

#wall segment 3rd ring bottom trio left ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-50,-110)

#wall segment 3rd ring bottom trio center ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-10,-110)

#wall segment 3rd ring bottom trio right ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(30,-110)

#4th ring

#wall segment 4th ring  left bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-170,-150)

#wall segment 4th ring  left mid bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-90,-150)

#wall segment 4th ring  right bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(150,-150)

#wall segment 4th ring  right mid bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(70,-140)

#wall segment 4th ring  right L bottom hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=3,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(130,-20)

#wall segment 4th ring  right L bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(150,-40)

#wall segment 4th ring  right L bottom hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=3,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(130,20)

#wall segment 4th ring  right L bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(150,40)

#wall segment 4th ring top center ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-10,150)


#5th ring

#wall segment 5th ring bottom T hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-10,-160)

#wall segment 5th ring bottom line
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=20,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-10,-200)

#wall segment 5th ring top line
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=11,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-30,200)

#wall segment 5th ring right top line hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(150,200)

#wall segment 5th ring right top line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=10)
wall_cell.penup()
wall_cell.goto(190,110)

#wall segment 5th ring right top small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(150,160)

#wall segment 5th ring right top mid small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(70,170)

#wall segment 5th ring top mid right small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(30,170)

#wall segment 5th ring top mid left small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-50,170)

#wall segment 5th ring left top mid small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=2)
wall_cell.penup()
wall_cell.goto(-90,150)

#wall segment 5th ring left top small line ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-130,180)

#wall segment 5th ring left bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=9)
wall_cell.penup()
wall_cell.goto(-210,-120)

#wall segment 5th ring right bottom ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=6)
wall_cell.penup()
wall_cell.goto(190,-150)

#wall segment 5th ring right mid ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=3)
wall_cell.penup()
wall_cell.goto(190,-40)

#wall segment 5th ring left mid low hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-170,-20)

#wall segment 5th ring left mid low ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-170,-40)

#wall segment 5th ring left mid up J hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=5,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-170,20)

#wall segment 5th ring left edge ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=9)
wall_cell.penup()
wall_cell.goto(-210,120)

#wall segment 5th ring left top ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=4)
wall_cell.penup()
wall_cell.goto(-170,170)

#wall segment 5th ring left A mid block
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-190,160)

#wall segment 5th ring left A top block
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-190,200)

#wall segment 5th ring left mid up small hor
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=2,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-180,60)

#wall segment 5th ring bottom left small ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-130,-180)
#wall segment 5th ring bottom mid small ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(-10,-180)

#wall segment 5th ring bottom right small ver
wall_cell=turtle.Turtle()
wall_cell.speed(0)
wall_cell.color("#1919A6")
wall_cell.shape("square")
wall_cell.shapesize(stretch_len=1,stretch_wid=1)
wall_cell.penup()
wall_cell.goto(110,-180)



#player
player=turtle.Turtle()
player.speed(0)
player.color("#FFFF00")
player.shape("circle")
player.shapesize(stretch_len=0.5,stretch_wid=0.5)
player.penup()
player.goto(-10,-40)



#player Direction change
#move up
def player_up():
    y= player.ycor()
    y=y+20
    player.sety(y)

    for arr in row1:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -10)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)

    for arr in row2:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 10)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)

    for arr in row3:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 30)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row4:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 50)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row5:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 70)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row6:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 90)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row7:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 110)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row8:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 130)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row9:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 150)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row10:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 170)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row11:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== 190)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row12:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -30)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row13:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -50)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row14:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -70)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row15:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -90)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row16:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -110)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row17:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -130)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row18:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -150)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row19:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -170)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row20:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -190)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
    for arr in row21:
        y=player.ycor()
        y2=y-20
        if (player.xcor()== -210)  and (player.ycor()== arr and (y2<y)):
            y= player.ycor()
            y= y-20
            player.sety(y)
    
   
#move down
def player_down():
    y= player.ycor()
    y=y-20
    player.sety(y)
    
    for arr in row1:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -10)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row2:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 10)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row3:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 30)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row4:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 50)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row5:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 70)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row6:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 90)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row7:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 110)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row8:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 130)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row9:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 150)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row10:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 170)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row11:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== 190)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row12:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -30)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row13:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -50)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row14:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -70)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row15:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -90)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row16:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -110)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row17:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -130)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row18:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -150)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row19:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -170)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row20:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -190)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    
    for arr in row21:
        y=player.ycor()
        y2=y+20

        if (player.xcor()== -210)  and (player.ycor()==arr) and (y2>y):
            y= player.ycor()
            y=y+20
            player.sety(y)
    

#move left
def player_left():
    x= player.xcor()
    x=x-20
    player.setx(x)

    for arr in arr1:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-40) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr2:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-60) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr3:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-80) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr4:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-100) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr5:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-120) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
   

    for arr in arr6:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-140) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr7:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-160) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr8:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-180) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)


    for arr in arr9:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==-20) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr10:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==0) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr20:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==20) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr11:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==40) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr12:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==60) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr13:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==80) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr14:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==100) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr15:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==120) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr16:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==140) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr17:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==160) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr18:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==180) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    

    for arr in arr19:
        x=player.xcor()
        x2=x+20

        if (player.xcor()== arr)  and (player.ycor()==200) and (x2>x):
            x= player.xcor()
            x=x+20
            player.setx(x)
    


#move right
def player_right():
    x= player.xcor()
    x= x+20
    player.setx(x)

    for arr in arr1:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-40 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr2:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-60 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr3:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-80 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr4:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-100 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr5:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-120 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr6:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-140 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr7:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-160 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr8:
        x=player.xcor()
        x2=x-20
        if (player.xcor()== arr)  and (player.ycor()==-180 and (x2<x)):
            x= player.xcor()
            x= x-20
            player.setx(x)
    

    for arr in arr9:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==-20) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr10:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==0) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr20:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==20) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr11:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==40) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr12:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==60) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    
    
    for arr in arr13:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==80) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr14:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==100) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr15:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==120) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    
    
    for arr in arr16:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==140) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    
    
    for arr in arr17:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==160) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr18:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==180) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    

    for arr in arr19:
        x=player.xcor()
        x2=x-20

        if (player.xcor()== arr)  and (player.ycor()==200) and (x2<x):
            x= player.xcor()
            x=x-20
            player.setx(x)
    
    


#ghost 1

ghost_1=turtle.Turtle()
ghost_1.speed(1)
ghost_1.color("#FF0000")
ghost_1.shape("circle")
ghost_1.shapesize(stretch_len=0.5,stretch_wid=0.5)
ghost_1.penup()
ghost_1.goto(-10,20)   


#ghost 2

ghost_2=turtle.Turtle()
ghost_2.speed(0)
ghost_2.color("#00FFFF")
ghost_2.shape("circle")
ghost_2.shapesize(stretch_len=0.5,stretch_wid=0.5)
ghost_2.penup()
ghost_2.goto(-10,0)

#ghost 3

ghost_3=turtle.Turtle()
ghost_3.speed(1)
ghost_3.color("#FFb8FF")
ghost_3.shape("circle")
ghost_3.shapesize(stretch_len=0.5,stretch_wid=0.5)
ghost_3.penup()
ghost_3.goto(-30,0)

#ghost 4

ghost_4=turtle.Turtle()
ghost_4.speed(0)
ghost_4.color("#FFb852")
ghost_4.shape("circle")
ghost_4.shapesize(stretch_len=0.5,stretch_wid=0.5)
ghost_4.penup()
ghost_4.goto(10,0)


#arrays
ghost_arr=[ghost_1,ghost_2,ghost_3,ghost_4]

#power_up 1
power1=turtle.Turtle()
power1.color("white")
power1.shape("circle")
power1.shapesize(stretch_len=0.25,stretch_wid=0.25)
power1.penup()
power1.goto(-170,-60)

#power_up 2
power2=turtle.Turtle()
power2.color("white")
power2.shape("circle")
power2.shapesize(stretch_len=0.25,stretch_wid=0.25)
power2.penup()
power2.goto(70,-160)

#power_up 3
power3=turtle.Turtle()
power3.color("white")
power3.shape("circle")
power3.shapesize(stretch_len=0.25,stretch_wid=0.25)
power3.penup()
power3.goto(170,180)

#power_up 4
power4=turtle.Turtle()
power4.color("white")
power4.shape("circle")
power4.shapesize(stretch_len=0.25,stretch_wid=0.25)
power4.penup()
power4.goto(-190,180)

#power_up 5
power5=turtle.Turtle()
power5.color("yellow")
power5.shape("circle")
power5.shapesize(stretch_len=0.25,stretch_wid=0.25)
power5.penup()
power5.goto(-10,0)


#pen for Game name:

pen1=turtle.Turtle()
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(-110,220)
pen1.write("WAQ-MAN",align="center",font=("Arial",15,"normal"))

#pen for Score:

pen=turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(90,220)
pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))


#Keyboard binding
wn.listen()
wn.onkeypress(player_up, "w" )
wn.onkeypress(player_down, "s" )
wn.onkeypress(player_left, "a" )
wn.onkeypress(player_right, "d" )

#Window update
while True:
    wn.update()
    
    #player and ghost touch condition

    for ghost in ghost_arr:
        if (player.xcor()==ghost.xcor()) and (player.ycor()== ghost.ycor()):
            break
    
    #score update
    score=score+1
    pen.clear()
    pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))           

#ghost_1 Movement

    if ghost_1.xcor()==-10 and ghost_1.ycor()==20:
        ghost_1.left(90)
    ghost_1.forward(1)
    
    if ghost_1.xcor()==-10 and ghost_1.ycor()>80:
        ghost_1.left(90)
        ghost_1.setx(-10)
        ghost_1.sety(80)

    if ghost_1.xcor()==-110 and ghost_1.ycor()==80:
        ghost_1.left(90)

    if ghost_1.xcor()==-110 and ghost_1.ycor()==-80:
        ghost_1.left(90)
    
    if ghost_1.xcor()== 90 and ghost_1.ycor()==-80:
        ghost_1.left(90)

    if ghost_1.xcor()== 90 and ghost_1.ycor()==80:
        ghost_1.left(90)
    
#ghost_2 Movement
    
    if ghost_2.xcor()==-10 and ghost_2.ycor()==0:
        ghost_2.left(90)
        ghost_2.setx(-10)
        ghost_2.sety(0)

    ghost_2.forward(1)
    
    if ghost_2.xcor()==-10 and ghost_2.ycor()>80 and ghost_2.ycor()<90:
        ghost_2.left(90)
        ghost_2.setx(-10)
        ghost_2.sety(80)
    
    if ghost_2.xcor()==-70 and ghost_2.ycor()==80:
        ghost_2.right(90)
        ghost_2.setx(-70)
        ghost_2.sety(80)

    if ghost_2.xcor()==-70 and ghost_2.ycor()==140:
        ghost_2.right(90)
        ghost_2.setx(-70)
        ghost_2.sety(140)

    if ghost_2.xcor()==-30 and ghost_2.ycor()==140:
        ghost_2.left(270)
        ghost_2.setx(-30)
        ghost_2.sety(140)

    if ghost_2.xcor()==-30 and ghost_2.ycor()==120:
        ghost_2.left(90)
        ghost_2.setx(-30)
        ghost_2.sety(120)

    if ghost_2.xcor()==10 and ghost_2.ycor()==120:
        ghost_2.left(90)
        ghost_2.setx(10)
        ghost_2.sety(120)

    if (ghost_2.xcor()<=10 and ghost_2.xcor()>9) and ghost_2.ycor()==140:
        ghost_2.right(90)
        ghost_2.setx(10)
        ghost_2.sety(140)

    if ghost_2.xcor()==50 and ghost_2.ycor()==140:
        ghost_2.right(90)
        ghost_2.setx(50)
        ghost_2.sety(140)

    if ghost_2.xcor()==50 and ghost_2.ycor()==80:
        ghost_2.right(90)
        ghost_2.setx(50)
        ghost_2.sety(80)



#ghost_3 Movement

    ghost_3.forward(1)
    
    

    if ghost_3.xcor()==-10 and ghost_3.ycor()==0:
        ghost_3.left(90)
        ghost_3.setx(-10)
        ghost_3.sety(0)

    if ghost_3.xcor()==-10 and ghost_3.ycor()>40:
        ghost_3.left(90)
        ghost_3.setx(-10)
        ghost_3.sety(40)

    if ghost_3.xcor()<-70 and ghost_3.ycor()==40:
        ghost_3.left(90)
        ghost_3.setx(-70)
        ghost_3.sety(40)

    if ghost_3.xcor()==-70 and ghost_3.ycor()<-40:
        ghost_3.left(90)
        ghost_3.setx(-70)
        ghost_3.sety(-40)

    if ghost_3.xcor()==50 and ghost_3.ycor()==-40:
        ghost_3.left(90)
        ghost_3.setx(50)
        ghost_3.sety(-40)

    if ghost_3.xcor()==50 and ghost_3.ycor()==40:
        ghost_3.left(90)
        ghost_3.setx(50)
        ghost_3.sety(40)

    
#ghost_4 Movement
    

    if ghost_4.xcor()==10 and ghost_4.ycor()==0:
        
        ghost_4.setx(-10)
        ghost_4.sety(40)
        

    ghost_4.forward(1)

    if ghost_4.xcor()==50 and ghost_4.ycor()==40:
        ghost_4.right(90)
        ghost_4.setx(50)
        ghost_4.sety(40)

    if ghost_4.xcor()==50 and ghost_4.ycor()==-40:
        ghost_4.right(90)
        ghost_4.setx(50)
        ghost_4.sety(-40)
    
    if ghost_4.xcor()==-9 and ghost_4.ycor()==-40:
        ghost_4.left(90)
        ghost_4.setx(-10)
        ghost_4.sety(-40)
        
    if ghost_4.xcor()==-11 and ghost_4.ycor()==-40:
        ghost_4.right(90)
        ghost_4.setx(-10)
        ghost_4.sety(-40)


    if ghost_4.xcor()==-10 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(-10)
        ghost_4.sety(-80)

    if ghost_4.xcor()== 90 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(90)
        ghost_4.sety(-80)

    if ghost_4.xcor()== 90 and ghost_4.ycor()==-40:
        ghost_4.right(90)
        ghost_4.setx(90)
        ghost_4.sety(-40)

    if ghost_4.xcor()== 130 and ghost_4.ycor()==-40:
        ghost_4.right(90)
        ghost_4.setx(130)
        ghost_4.sety(-40)

    if ghost_4.xcor()== 130 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(130)
        ghost_4.sety(-80)

    if ghost_4.xcor()== 170 and ghost_4.ycor()==-80:
        ghost_4.right(90)
        ghost_4.setx(170)
        ghost_4.sety(-80)

    if ghost_4.xcor()== 170 and ghost_4.ycor()==-120:
        ghost_4.right(90)
        ghost_4.setx(170)
        ghost_4.sety(-120)

    if ghost_4.xcor()== 130 and ghost_4.ycor()==-120:
        ghost_4.left(90)
        ghost_4.setx(130)
        ghost_4.sety(-120)

    if ghost_4.xcor()== 130 and ghost_4.ycor()==-160:
        ghost_4.right(90)
        ghost_4.setx(130)
        ghost_4.sety(-160)

    if ghost_4.xcor()== 50 and ghost_4.ycor()==-160:
        ghost_4.right(90)
        ghost_4.setx(50)
        ghost_4.sety(-160)

    if ghost_4.xcor()== 50 and ghost_4.ycor()==-140:
        ghost_4.left(90)
        ghost_4.setx(50)
        ghost_4.sety(-140)

    if ghost_4.xcor()== -30 and ghost_4.ycor()==-140:
        ghost_4.right(90)
        ghost_4.setx(-30)
        ghost_4.sety(-140)

    if ghost_4.xcor()== -30 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(-30)
        ghost_4.sety(-80)

    if ghost_4.xcor()== -70 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(-70)
        ghost_4.sety(-80)

    if ghost_4.xcor()== -70 and ghost_4.ycor()==-120:
        ghost_4.right(90)
        ghost_4.setx(-70)
        ghost_4.sety(-120)

    if ghost_4.xcor()== -110 and ghost_4.ycor()==-120:
        ghost_4.left(90)
        ghost_4.setx(-110)
        ghost_4.sety(-120)

    if ghost_4.xcor()== -110 and ghost_4.ycor()==-160:
        ghost_4.right(90)
        ghost_4.setx(-110)
        ghost_4.sety(-160)

    if ghost_4.xcor()== -150 and ghost_4.ycor()==-160:
        ghost_4.right(90)
        ghost_4.setx(-150)
        ghost_4.sety(-160)

    if ghost_4.xcor()== -150 and ghost_4.ycor()==-120:
        ghost_4.left(90)
        ghost_4.setx(-150)
        ghost_4.sety(-120)

    if ghost_4.xcor()== -190 and ghost_4.ycor()==-120:
        ghost_4.right(90)
        ghost_4.setx(-190)
        ghost_4.sety(-120)

    if ghost_4.xcor()== -190 and ghost_4.ycor()==-80:
        ghost_4.right(90)
        ghost_4.setx(-190)
        ghost_4.sety(-80)

    if ghost_4.xcor()== -150 and ghost_4.ycor()==-80:
        ghost_4.left(90)
        ghost_4.setx(-150)
        ghost_4.sety(-80)

    if ghost_4.xcor()== -150 and ghost_4.ycor()==-40:
        ghost_4.right(90)
        ghost_4.setx(-150)
        ghost_4.sety(-40)

    if ghost_4.xcor()== -110 and ghost_4.ycor()==-40:
        ghost_4.left(90)
        ghost_4.setx(-110)
        ghost_4.sety(-40)

    if ghost_4.xcor()== -110 and ghost_4.ycor()==80:
        ghost_4.right(90)
        ghost_4.setx(-110)
        ghost_4.sety(80)


    if ghost_4.xcor()== -10 and ghost_4.ycor()==80:
        ghost_4.right(90)
        ghost_4.setx(-10)
        ghost_4.sety(80)

    if ghost_4.xcor()== -10 and ghost_4.ycor()==40:
        ghost_4.right(90)
        ghost_4.setx(-10)
        ghost_4.sety(40)

    if ghost_4.xcor()== -70 and ghost_4.ycor()==40:
        ghost_4.left(90)
        ghost_4.setx(-70)
        ghost_4.sety(40)

    if ghost_4.xcor()== -70 and ghost_4.ycor()==-40:
        ghost_4.left(90)
        ghost_4.setx(-70)
        ghost_4.sety(-40)

    
    #Teleportation

    if player.xcor()==90 and player.ycor()==220:
        player.goto(-150,200)

    if player.xcor()==-150 and player.ycor()==220:
        player.goto(90,200)

    if player.xcor()==210 and player.ycor()==0:
        player.goto(-210,0)

    if player.xcor()==-230 and player.ycor()==0:
        player.goto(190,0)

    if player.xcor()==210 and player.ycor()==-80:
        player.goto(-190,180)

    if player.xcor()==-210 and player.ycor()==180:
        player.goto(190,-80)
    
    #if player touches power up 1
    if player.xcor()==power1.xcor() and player.ycor()==power1.ycor():
        power1.hideturtle()

        #score update if plyer touches power up
        score=score+2
        score=score-1
        pen.clear()
        pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))
    

    

    #if player touches power up 2
    if player.xcor()==power2.xcor() and player.ycor()==power2.ycor():
        power2.hideturtle()

        #score update if plyer touches power up
        score=score+2
        score=score-1
        pen.clear()
        pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))


    #if player touches power up 3
    if player.xcor()==power3.xcor() and player.ycor()==power3.ycor():
        power3.hideturtle()

        #score update if plyer touches power up
        score=score+2
        score=score-1
        pen.clear()
        pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))

    #if player touches power up 4
    if player.xcor()==power4.xcor() and player.ycor()==power4.ycor():
        power4.hideturtle()

        #score update if plyer touches power up
        score=score+2
        score=score-1
        pen.clear()
        pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))

    #if player touches power up 5
    if player.xcor()==power5.xcor() and player.ycor()==power5.ycor():
        player.color("green")
        power5.hideturtle()

        #score update if plyer touches power up
        score=score+2
        score=score-1
        pen.clear()
        pen.write("Score: {}".format(score) ,align="center",font=("Arial",15,"normal"))

    #If ghost touches player, game stops
    if (ghost_1.xcor()==player.xcor() and ghost_1.ycor()==player.ycor()) or (ghost_3.xcor()==player.xcor() and ghost_3.ycor()==player.ycor()) or (ghost_4.xcor()==player.xcor() and ghost_4.ycor()==player.ycor()) or (ghost_2.xcor()==player.xcor() and ghost_2.ycor()==player.ycor()):
        break

    


    
   

    
    
            
        
    
    
            
            

    

    
    
    

    

