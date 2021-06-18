import turtle
import time
import winsound
import random
table = turtle.Screen()
table.setup(800, 800)
table.bgcolor("medium sea green")
cards_pile = turtle.Turtle()
score1 = turtle.Turtle()
score2 = turtle.Turtle()
chips = turtle.Turtle()
card = turtle.Turtle()
card2 = turtle.Turtle()
button = turtle.Turtle()
game_over = turtle.Turtle()
win = turtle.Turtle()
table.addshape("2D.gif")
table.addshape("3D.gif")
table.addshape("4D.gif")
table.addshape("5D.gif")
table.addshape("6D.gif")
table.addshape("7D.gif")
table.addshape("8D.gif")
table.addshape("9D.gif")
table.addshape("10D.gif")
table.addshape("JD.gif")
table.addshape("QD.gif")
table.addshape("KD.gif")
table.addshape("AD.gif")
cards = {
    2 : '2D',
    3 : '3D',
    4 : '4D',
    5 : '5D',
    6 : '6D',
    7 : '7D',
    8 : '8D',
    9 : '9D',
    10 : '10D',
    11 : 'JD',
    12 : 'QD',
    13 : 'KD',
    14 : 'AD'
}
cvalue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
score1.hideturtle()
score1.penup()
score2.hideturtle()
score2.penup()
card.hideturtle()
card.penup()
card2.hideturtle()
card2.penup()
table.addshape("card_pile.gif")
cards_pile.shape("card_pile.gif")
table.addshape("chips.gif")
chips.shape("chips.gif")
cards_pile.penup()
chips.penup()
button.hideturtle()
button.penup()
game_over.hideturtle()
game_over.speed(100000)
win.hideturtle()
win.speed(100000)
win.penup()

def setup():
    cards_pile.speed(100000)
    score2.speed(100000)
    score1.speed(100000)
    cards_pile.goto(0, 250)
    cards_pile.stamp()
    cards_pile.goto(0, -250)
    chips.speed(100000)
    chips.goto(-250,270)
    chips.stamp()
    chips.goto(250, 270)
    chips.stamp()
    chips.goto(-250, -270)
    chips.stamp()
    chips.goto(250, -270)
    chips.stamp()
    score1.goto(-200, 0)
    score2.goto(200, 0)
    score1.write("player 1 - 0", align="center", font=("Comic Sans MS", 24, "normal"))
    score2.write("player 2 - 0", align="center", font=("Comic Sans MS", 24, "normal"))
    button.speed(100000)
    button.goto(-60, -100)
    button.pendown()
    for i in range(2):
        button.forward(120)
        button.left(90)
        button.forward(30)
        button.left(90)
    button.penup()
    button.goto(-30, -94)
    button.write('press me', font=("Comic Sans MS", 12, "normal"))
points1 = 0
points2 = 0
def game():
    winsound.PlaySound('elevator_music.wav', winsound.SND_ASYNC)
    setup()
    card.speed(100000)
    card2.speed(100000)
    def buttonclick(x, y):
        if x > -60 and x < 61 and y > -100 and y < -70:
            c1 = random.choice(cvalue)
            c2 = random.choice(cvalue)
            card.shape(cards[c1] + '.gif')
            card2.shape(cards[c2] + '.gif')
            card.goto(0, 250)
            card2.goto(0, -250)
            card.showturtle()
            card2.showturtle()
            if c1 > c2:
                points1_calc()
            elif c2 > c1:
                points2_calc()




    table.onscreenclick(buttonclick, 1)
    turtle.listen()
    def points1_calc():
        score1.clear()
        global points1
        points1 += 1
        score1.write("player 1 - {}".format(points1), align="center", font=("Comic Sans MS", 24, "normal"))
        if points1 == 20:
            game_over.goto(0, 0)
            game_over.write("GAME OVER", align="center", font=("Comic Sans MS", 18, "normal"))
            win.goto(-250, -100)
            win.write("Player 1 WON", align="center", font=("Comic Sans MS", 18, "normal"))
            time.sleep(3.5)
            table.bye()
    def points2_calc():
        score2.clear()
        global points2
        points2 += 1
        score2.write("player 2 - {}".format(points2), align="center", font=("Comic Sans MS", 25, "normal"))
        if points2 == 20:
            game_over.goto(0, 0)
            game_over.write("GAME OVER", align="center", font=("Comic Sans MS", 18, "normal"))
            win.goto(250, -100)
            win.write("Player 2 WON", align="center", font=("Comic Sans MS", 18, "normal"))
            time.sleep(3.5)
            table.bye()

game()
# input time in seconds


# function call
table.mainloop()