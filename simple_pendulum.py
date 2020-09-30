from tkinter import Tk,Canvas
from math import cos,sin,acos,pi,sqrt
from scipy.integrate import quad
root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

w = 1250
h = 600
time_step=1

c = 1 #This constant is g/L
(theta0,omega0) = (0,-0.5) #Initial condition
E = omega0**2-2*c*cos(theta0) #Total energy (omit the constant (1/2)*m*L^2)
periodic = (E-2*c < -0.01)
if periodic == True:
    #Find the period here
    theta_max = acos( cos(theta0)-(omega0**2)/(2*c) )
    f=(lambda theta: 2*sqrt(2/c)/sqrt(cos(theta)-cos(theta_max)))
    period = quad(f,0,theta_max)[0]

(x0,y0) = (w//2,h//2)
L=200
r=15

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=10)

class Pendulum:
    def __init__(self,theta=theta0,omega=omega0):
        self.theta = theta
        self.omega = omega
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.rod = my_canvas.create_line(x0,y0,position[0],position[1],width=2)
        self.bob = my_canvas.create_oval(position[0]-r,position[1]-r,\
                                            position[0]+r,position[1]+r,fill="red")
        self.activate_motion()

    def redraw(self):
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        my_canvas.coords(self.rod,x0,y0,position[0],position[1])
        my_canvas.coords(self.bob,position[0]-r,position[1]-r,position[0]+r,position[1]+r)

    def update_data(self):
        self.theta += self.omega*time_step/1000

    def activate_motion(self):
        self.update_data()
        self.redraw()
        root.after(time_step,self.activate_motion)
    
pendulum = Pendulum()
root.mainloop()