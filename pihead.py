import turtle as t
t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((255,155,192),"pink")
t.setup(840,500)
t.speed(10)


t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30)
t.circle(100,-60)
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
a=0.4
for i in range(60):
    if 0<=i<30 or 60<=i<90:
        a=a+0.08
        t.lt(3) 
        t.fd(a) 
    else:
        a=a-0.08
        t.lt(3)
        t.fd(a)
