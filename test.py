import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.width(3)
t.pencolor("white") 
t.fillcolor("blue")
t.begin_fill()#開始填色
t.circle(105)#畫圓
t.end_fill()#結束填色
t.circle(105, 90) #畫1/4的圓
t.width(5)
t.left(45)
t.forward(50)
for i in range(2):
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
t.left(90)
t.forward(50)
t.left(45)
t.pencolor('red')
t.circle(108)
screen.exitonclick() #讓視窗保持開啟，直到用戶點擊視窗