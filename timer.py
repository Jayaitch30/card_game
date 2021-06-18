import turtle
import winsound
import time
winsound.PlaySound('music.wav',winsound.SND_ASYNC)
idf = turtle.Turtle()
hamas = turtle.Turtle()
gaza = turtle.Screen()
gaza.title('Hamas on fire game')
exp = turtle.Turtle()
logo = turtle.Turtle()
attack = turtle.Turtle()
exp.hideturtle()
idf.hideturtle()
hamas.hideturtle()
logo.hideturtle()
attack.hideturtle()
gaza.setup(1000,800)
gaza.bgpic("start.gif")
score = turtle.Turtle()
score.speed(100000)
score.penup()
score.goto(-400, 350)
score.hideturtle()
hamas.penup()
idf.penup()
idf.speed(20)
hamas.speed(20)
hamas.left(180)
gaza.addshape("explostion.gif")
gaza.addshape("rocket.gif")
gaza.addshape("terrorist.gif")
gaza.addshape("logo.gif")
gaza.addshape("terrorist1.gif")
gaza.addshape("terrorist2.gif")
gaza.addshape("rocket2.gif")
gaza.addshape("plane.gif")
gaza.addshape("tank.gif")
gaza.addshape("tank_rocket.gif")
gaza.addshape("plane_bombs.gif")
gaza.addshape("plane_exp.gif")
gaza.addshape("tank_exp.gif")
exp.shape('explostion.gif')
logo.shape("logo.gif")
logo.penup()
logo.goto(-370, -200)
exp.penup()
attack.penup()
def setup():
    idf.speed(20)
    idf.setpos(0,350)
    hamas.speed(20)
    hamas.setpos(450, -350)
def enemyshop():
    if gaza.bgpic() == "ilan.gif" or gaza.bgpic() == "start.gif":
        gaza.bgpic("enemyshop.gif")
        hamas.hideturtle()
        idf.hideturtle()
        def buttonclick(x, y):
            if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "enemyshop.gif":
                hamas.shape("terrorist.gif")
                rocketshop()
            elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "enemyshop.gif":
                hamas.shape("terrorist2.gif")
                rocketshop()
        gaza.onscreenclick(buttonclick, 1)
        gaza.listen()
def rocketshop():
    gaza.bgpic("rocketshop.gif")
    def buttonclick2(x, y):
        if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "rocketshop.gif":
            idf.shape("rocket2.gif")
            game_function()
        elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "rocketshop.gif":
            idf.shape("rocket.gif")
            game_function()
    gaza.onscreenclick(buttonclick2, 1)
    gaza.listen()

def game_function():
    setup()
    gaza.bgpic("ilan.gif")
    idf.showturtle()
    hamas.showturtle()
    logo.showturtle()
    speed = 10
    def kL():
        idf.goto(idf.xcor()-10, idf.ycor())
    def kR():
        idf.goto(idf.xcor()+10, idf.ycor())
    def kSpace():
        idf.speed(2)
        while idf.ycor() == 350:
            bombdrop()
    def kr():
        if idf.ycor() == 350 or idf.ycor() <= -350:
            if 1000 - (idf.xcor() - hamas.xcor()) == 1000 or idf.ycor() <= -351:
                idf.hideturtle()
                hamas.hideturtle()
                score.clear()
                gaza.bgpic("attacks.gif")
                winsound.PlaySound('music.wav',winsound.SND_ASYNC)
                def buttonclick3(x, y):
                    if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "attacks.gif":
                        attack.shape("plane.gif")
                        plane_attack()
                    elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "attacks.gif":
                        attack.shape("tank.gif")
                        tank_attack()
                    else:
                        if gaza.bgpic() == "attacks.gif":
                            restart()
                gaza.onscreenclick(buttonclick3, 1)
                gaza.listen()
            else:
                restart()
    def plane_attack():
        gaza.bgpic("ilan.gif")
        current_shape = idf.shape()
        hamas.goto(0, -350)
        hamas.showturtle()
        attack.speed(10000)
        attack.goto(400, 350)
        attack.speed(3)
        attack.showturtle()
        while attack.xcor() > idf.xcor():
            attack.goto(attack.xcor()-3, attack.ycor()-1)
        idf.goto(0, attack.ycor()-20)
        idf.shape("plane_bombs.gif")
        idf.showturtle()
        exp.shape("plane_exp.gif")
        bombdrop()
        attack.goto(-600, 350)
        attack.hideturtle()
        idf.shape(current_shape)
        exp.shape("explostion.gif")
        hamas.hideturtle()
        gaza.bgpic("plane_mission.gif")
        winsound.PlaySound('plane_music.wav', winsound.SND_ASYNC)
    def bombdrop():
        winsound.PlaySound('bombdrop.wav', winsound.SND_ASYNC)
        idf.goto(idf.xcor(), -350)
        if exp.shape() == "plane_exp.gif":
            exp.goto(idf.xcor(), -330)
        else:
            exp.goto(idf.xcor(), -300)
        idf.hideturtle()
        exp.showturtle()
        time.sleep(1.5)
        exp.hideturtle()
    def tank_attack():
        gaza.bgpic("ilan.gif")
        hamas.goto(0, -350)
        hamas.showturtle()
        current_shape2 = idf.shape()
        idf.shape("tank_rocket.gif")
        exp.shape("tank_exp.gif")
        attack.speed(10000)
        attack.goto(1200, -350)
        attack.speed(2)
        attack.showturtle()
        attack.goto(380, -350)
        idf.goto(400,-350)
        idf.showturtle()
        idf.goto(30, -351)
        exp.speed(10000)
        exp.goto(0, -350)
        idf.hideturtle()
        exp.showturtle()
        winsound.PlaySound('tank_bomb.wav', winsound.SND_ASYNC)
        time.sleep(1.5)
        exp.hideturtle()
        exp.shape("explostion.gif")
        idf.shape(current_shape2)
        attack.hideturtle()
        hamas.hideturtle()
        gaza.bgpic("tank_mission.gif")
        winsound.PlaySound('tank_music.wav', winsound.SND_ASYNC)

    def restart():
        idf.hideturtle()
        hamas.hideturtle()
        score.clear()
        exp.hideturtle()
        gaza.bgpic("ilan.gif")
        winsound.PlaySound('music.wav', winsound.SND_ASYNC)
        game_function()


    gaza.listen()
    while idf.ycor() != -350 :
        hamas.goto(hamas.xcor() + speed, hamas.ycor())
        if hamas.xcor() <= -451:
            if hamas.shape() == "terrorist.gif":
                hamas.shape("terrorist1.gif")
            hamas.left(180)
            speed = -speed
        elif hamas.xcor() >= 451:
            if hamas.shape() == "terrorist1.gif":
                hamas.shape("terrorist.gif")
            hamas.left(180)
            speed = -speed

        gaza.onkeypress(kL, "Left")
        gaza.onkeypress(kR, "Right")
        gaza.onkey(kSpace, "space")
        gaza.onkeyrelease(kr, "r")
        if idf.xcor() >= 450:
            idf.goto(idf.xcor()-25, idf.ycor())
        elif idf.xcor() <= -450:
            idf.goto(idf.xcor()+25, idf.ycor())
    if idf.xcor() > hamas.xcor():
        if 1000 - (idf.xcor() - hamas.xcor()) >= 900:
            gaza.bgpic("ilan2.gif")
            winsound.PlaySound('almost.wav', winsound.SND_ASYNC)
        else:
            gaza.bgpic("close.gif")
            winsound.PlaySound('bambam.wav', winsound.SND_ASYNC)
        idf.hideturtle()
        hamas.hideturtle()
        score.write("points: {}".format(1000 - (idf.xcor() - hamas.xcor())), align="center", font=("Comic Sans MS", 24, "normal"))
    elif hamas.xcor() > idf.xcor():
        if 1000 - (hamas.xcor() - idf.xcor()) >= 900:
            gaza.bgpic("ilan2.gif")
            winsound.PlaySound('almost.wav', winsound.SND_ASYNC)
        else:
            gaza.bgpic("close.gif")
            winsound.PlaySound('bambam.wav', winsound.SND_ASYNC)
        idf.hideturtle()
        hamas.hideturtle()
        score.write("points: {}".format(1000 - (hamas.xcor() - idf.xcor())), align="center", font=("Comic Sans MS", 24, "normal"))
    else:
        exp.hideturtle()
        winsound.PlaySound("hatikva", winsound.SND_ASYNC)
        gaza.bgpic("perfect.gif")
        idf.hideturtle()
        hamas.hideturtle()
        score.write("points: {}".format(1000), align="center", font=("Comic Sans MS", 24, "normal"))
def kESC():
    gaza.bye()
gaza.onkey(kESC, "Escape")
gaza.onkey(enemyshop, "Return")
gaza.listen()
gaza.mainloop()