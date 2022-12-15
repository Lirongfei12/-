import turtle as t  #导入海龟库
t.shape('arrow')#设置画笔造型
t.penup()#抬笔
t.goto(-300,0)#设置坐标
t.pendown()#落笔

t.forward(50)#向前50像素
t.right(90)#向右转90度

t.fd(50)#向前50像素
t.right(90)#向右转90度

t.fd(50)#向前50像素
t.right(90)#向右转90度

t.fd(50)#向前50像素


##for 循环在这里的用法
t.penup()
t.goto(-200,0)
t.pendown()

for i in range(4):
    t.right(90)
    t.fd(50)


# while 循环在这里的用法
t.penup()
t.goto(-100,0)
t.pendown()

a = 0
while a<4:
    t.right(90)
    t.fd(50)
    a += 1
#turtle基础命令的使用
t.pensize(10)#画笔大小设置
t.pencolor('yellow')#画笔颜色设置
t.bgcolor('black')#背景颜色设置
t.fillcolor('white')#图形颜色设置
t.begin_fill()#开始填充
t.penup()#抬笔
t.goto(0,0)#设置坐标（0，0）
t.pendown()#落笔
for i in range(4):#遍历4遍
    t.right(90)#向右转90度
    t.forward(100)#向前移动100像素
t.end_fill()#完成填充
t.done()#完成绘制后保留窗口