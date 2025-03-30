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

def draw_hyperbola():
    # 清空畫布
    turtle.reset()
    draw_axes()
    turtle.speed(0)  # 設置繪圖速度為最快

    a = int(scale_a.get())  # 雙曲線的半貫軸
    b = int(scale_b.get())  # 雙曲線的半共軛軸

    # 繪製雙曲線的右支
    turtle.penup()
    step = 1  # 設置步長，控制繪製精度
    for x in range(a, 300, step):  # x 的範圍從 a 到正無窮
        value = (x**2 / a**2) - 1
        if value < 0:  # 檢查是否為非負數
            continue
        y = b * math.sqrt(value)  # 計算 y
        turtle.goto(x, y)  # 繪製上半部分
        turtle.pendown()
    turtle.penup()
    for x in range(300, a - 1, -step):  # x 的範圍從正無窮到 a
        value = (x**2 / a**2) - 1
        if value < 0:  # 檢查是否為非負數
            continue
        y = -b * math.sqrt(value)  # 計算 y（下半部分）
        turtle.goto(x, y)
        turtle.pendown()

    # 繪製雙曲線的左支
    turtle.penup()
    for x in range(-a, -300, -step):  # x 的範圍從 -a 到負無窮
        value = (x**2 / a**2) - 1
        if value < 0:  # 檢查是否為非負數
            continue
        y = b * math.sqrt(value)  # 計算 y
        turtle.goto(x, y)  # 繪製上半部分
        turtle.pendown()
    turtle.penup()
    for x in range(-300, -a + 1, step):  # x 的範圍從負無窮到 -a
        value = (x**2 / a**2) - 1
        if value < 0:  # 檢查是否為非負數
            continue
        y = -b * math.sqrt(value)  # 計算 y（下半部分）
        turtle.goto(x, y)
        turtle.pendown()

# 創建主窗口
root = tk.Tk()
root.title("Turtle 繪製雙曲線")
root.geometry("400x200")

scale_a = tk.Scale(root, from_=10, to=150, orient=tk.HORIZONTAL, label="半貫軸長", length=300)  # 半貫軸
scale_a.pack()

scale_b = tk.Scale(root, from_=10, to=150, orient=tk.HORIZONTAL, label="半共軛軸長", length=300)  # 半共軛軸
scale_b.pack()

btn_draw = tk.Button(root, text="繪製圖形", command=draw_hyperbola)
btn_draw.pack(pady=20)

root.mainloop()