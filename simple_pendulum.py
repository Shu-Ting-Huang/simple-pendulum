from tkinter import Tk,Canvas
from math import cos,sin,pi
root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

w = 1250
h = 600

(x0,y0) = (w//2,h//2)
L=200
r=15

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=10)

class Pendulum:
    def __init__(self,theta=0,omega=-1):
        self.theta = theta
        self.omega = omega
        self.position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.rod = my_canvas.create_line(x0,y0,self.position[0],self.position[1],width=2)
        self.bob = my_canvas.create_oval(self.position[0]-r,self.position[1]-r,\
                                            self.position[0]+r,self.position[1]+r,fill="red")

pendulum = Pendulum()
root.mainloop()