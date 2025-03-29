import tkinter as tk
from tkinter import messagebox
import turtle

def draw_parabola():
    # 清空畫布
    turtle.reset()
    turtle.speed(0)  # 設置繪圖速度為最快

    # 拋物線參數
    c = int(scale.get())    # 控制拋物線的焦距

    # 繪製拋物線
    turtle.penup()
    for x in range(-300, 301):  # x 的範圍從 -300 到 300
        y = 1/(4*c)*x**2
        turtle.goto(x, y)  # 移動到計算出的點
        turtle.pendown()

# 創建主窗口
root = tk.Tk()
root.title("Turtle 繪製拋物線")
root.geometry("400x200")

# 繪製按鈕
tk.Label(root, text="點擊下方按鈕繪製拋物線").pack(pady=10)
scale=tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="拋物線焦距", length=300)
scale.pack()

label = tk.Label(root, text="當前值: 0")
label.pack()

btn_draw = tk.Button(root, text="繪製圖形", command=draw_parabola)
btn_draw.pack(pady=20)

root.mainloop()