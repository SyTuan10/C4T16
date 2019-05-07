from turtle import *

n = int(input("Nhap n: "))
for i in range(n):
    forward(100)
    left(360/n)
mainloop()