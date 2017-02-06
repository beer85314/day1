# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightgreen")# 設定畫布底色為淺綠色

john = turtle.Turtle()         # 建立一個海龜turtle，它的名字叫marry
john.color("hotpink")          # 設定畫筆顏色為粉紅色
john.pensize(5)                        # 設定畫筆粗細為5個像素


def a (t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

for i in range(5):
    a(john, 50) 
    john.penup()
    john.forward(100)
    john.pendown()

window.exitonclick()
