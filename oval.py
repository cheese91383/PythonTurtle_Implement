import tkinter as tk
from tkinter import messagebox
import turtle
import math
def draw_axes():
    """繪製象限坐標軸"""
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 0)  # 繪製 X 軸
    turtle.pendown()
    turtle.goto(300, 0)
    turtle.penup()
    turtle.goto(0, -300)  # 繪製 Y 軸
    turtle.pendown()
    turtle.goto(0, 300)
    turtle.penup()


def draw_oval():
    # 清空畫布
    turtle.reset()
    draw_axes()
    turtle.speed(0)  # 設置繪圖速度為最快

    a = int(scale_a.get())  # 橢圓x長度
    b = int(scale_b.get())  # 橢圓y長度
    c = math.sqrt(abs(a**2 - b**2))  # 焦點距離

    # 繪製橢圓
    turtle.penup()
    step = 1  # 設置步長，控制繪製精度
    for x in range(-a, a + 1, step):  # x 的範圍從 -a 到 a
        value = 1 - (x**2 / a**2)
        if value < 0:  # 檢查是否為非負數
            continue
        y = b * math.sqrt(value)  # 計算 y
        turtle.goto(x, y)  # 繪製上半部分
        turtle.pendown()

    for x in range(a, -a - 1, -step):  # x 的範圍從 a 到 -a
        value = 1 - (x**2 / a**2)
        if value < 0:  # 檢查是否為非負數
            continue
        y = -b * math.sqrt(value)  # 計算 y（下半部分）
        turtle.goto(x, y)
        turtle.pendown()
    if a > b:
        turtle.penup()
        turtle.goto(c, 0)
        turtle.dot(5,"blue")
        turtle.penup()
        turtle.goto(-c, 0)
        turtle.dot(5,"blue")
    else:
        turtle.penup()
        turtle.goto(0, c)
        turtle.dot(5,"blue")
        turtle.penup()
        turtle.goto(0, -c)
        turtle.dot(5,"blue")
        
# 創建主窗口
root = tk.Tk()
root.title("繪製橢圓")
root.geometry("400x200")

scale_a = tk.Scale(root, from_=1, to=150, orient=tk.HORIZONTAL, label="橢圓x長度", length=300)  # 長半徑
scale_a.pack()

scale_b = tk.Scale(root, from_=1, to=150, orient=tk.HORIZONTAL, label="橢圓y長度", length=300)  # 短半徑
scale_b.pack()

btn_draw = tk.Button(root, text="繪製圖形", command=draw_oval)
btn_draw.pack(pady=20)

root.mainloop()