import tkinter as tk
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
    c = math.sqrt(a**2 + b**2)  # 焦點距離
    direction = derection_var.get()  # 獲取方向選擇

    step = 1  # 設置步長，控制繪製精度

    if direction == "左右":
        # 繪製左右開口的雙曲線
        turtle.penup()
        for x in range(a, 301, step):  # x 的範圍從 a 到正無窮
            value = (x**2 / a**2) - 1
            if value < 0:
                continue
            y = b * math.sqrt(value)  # 計算 y
            turtle.goto(x, y)  # 繪製上半部分
            turtle.pendown()
        turtle.penup()
        for x in range(a, 301, step):
            value = (x**2 / a**2) - 1
            if value < 0:
                continue
            y = -b * math.sqrt(value)  # 計算 y（下半部分）
            turtle.goto(x, y)
            turtle.pendown()

        # 繪製左半部分
        turtle.penup()
        for x in range(-a, -301, -step):  # x 的範圍從 -a 到負無窮
            value = (x**2 / a**2) - 1
            if value < 0:
                continue
            y = b * math.sqrt(value)  # 計算 y
            turtle.goto(x, y)  # 繪製上半部分
            turtle.pendown()
        turtle.penup()
        for x in range(-a, -301, -step):
            value = (x**2 / a**2) - 1
            if value < 0:
                continue
            y = -b * math.sqrt(value)  # 計算 y（下半部分）
            turtle.goto(x, y)
            turtle.pendown()

    elif direction == "上下":
        # 繪製上下開口的雙曲線
        turtle.penup()
        for y in range(b, 301, step):  # y 的範圍從 b 到正無窮
            value = (y**2 / b**2) - 1
            if value < 0:
                continue
            x = a * math.sqrt(value)  # 計算 x
            turtle.goto(x, y)  # 繪製右半部分
            turtle.pendown()
        turtle.penup()
        for y in range(b, 301, step):
            value = (y**2 / b**2) - 1
            if value < 0:
                continue
            x = -a * math.sqrt(value)  # 計算 x（左半部分）
            turtle.goto(x, y)
            turtle.pendown()

        # 繪製下半部分
        turtle.penup()
        for y in range(-b, -301, -step):  # y 的範圍從 -b 到負無窮
            value = (y**2 / b**2) - 1
            if value < 0:
                continue
            x = a * math.sqrt(value)  # 計算 x
            turtle.goto(x, y)  # 繪製右半部分
            turtle.pendown()
        turtle.penup()
        for y in range(-b, -301, -step):
            value = (y**2 / b**2) - 1
            if value < 0:
                continue
            x = -a * math.sqrt(value)  # 計算 x（左半部分）
            turtle.goto(x, y)
            turtle.pendown()

    # 繪製漸進線
    turtle.penup()
    turtle.color("blue")
    if direction == "左右":
        for x in range(-300, 301, step):  # x 的範圍從 -300 到 300
            y = (b / a) * x
            turtle.goto(x, y)  # 漸進線 y = (b/a) * x
            turtle.pendown()
        turtle.penup()
        for x in range(-300, 301, step):
            y = -(b / a) * x
            turtle.goto(x, y)  # 漸進線 y = -(b/a) * x
            turtle.pendown()
    elif direction == "上下":
        for y in range(-300, 301, step):  # y 的範圍從 -300 到 300
            x = (a / b) * y
            turtle.goto(x, y)  # 漸進線 x = (a/b) * y
            turtle.pendown()
        turtle.penup()
        for y in range(-300, 301, step):
            x = -(a / b) * y
            turtle.goto(x, y)  # 漸進線 x = -(a/b) * y
            turtle.pendown()

    # 繪製焦點
    turtle.penup()
    if direction == "左右":
        turtle.goto(c, 0)
        turtle.dot(5, "red")
        turtle.goto(-c, 0)
        turtle.dot(5, "red")
    elif direction == "上下":
        turtle.goto(0, c)
        turtle.dot(5, "red")
        turtle.goto(0, -c)
        turtle.dot(5, "red")

# 創建主窗口
root = tk.Tk()
root.title("Turtle 繪製雙曲線")
root.geometry("600x400")  # 調整視窗大小

# 方向選擇
derection_var = tk.StringVar(value="左右")
tk.Radiobutton(root, text="左右開口", variable=derection_var, value="左右").pack(pady=5)
tk.Radiobutton(root, text="上下開口", variable=derection_var, value="上下").pack(pady=5)

# 半貫軸長度滑桿
scale_a = tk.Scale(root, from_=10, to=150, orient=tk.HORIZONTAL, label="半貫軸長", length=300)  # 半貫軸
scale_a.pack(pady=10)

# 半共軛軸長度滑桿
scale_b = tk.Scale(root, from_=10, to=150, orient=tk.HORIZONTAL, label="半共軛軸長", length=300)  # 半共軛軸
scale_b.pack(pady=10)

# 繪製按鈕
btn_draw = tk.Button(root, text="繪製圖形", command=draw_hyperbola)
btn_draw.pack(pady=20)

root.mainloop()