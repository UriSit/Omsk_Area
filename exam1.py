import turtle # ����������� ���������� turtle
import time

turtle.color("blue") # ������������� ���� ���������
turtle.penup() # ��������� ������
turtle.goto(-110, -25) # ��������� �� ������ �����������
turtle.pendown() # �������� ������
turtle.circle(45) # ������ ���� � �������� 45

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.write("Olympic Symbol") # ������ ��� ������ ����� ������� ������� "Olympic Symbol"

time.sleep(10)

turtle.done()