from tkinter import Tk,Canvas,PhotoImage
from math import cos,sin,acos,pi,sqrt
from scipy.integrate import quad,odeint
from numpy import linspace
from PIL import Image,ImageTk

w = 1250
h = 600
time_step=1

c = 36 #This constant is g/L
(theta0,omega0) = (pi/4,-0.0) #Initial condition
E = omega0**2-2*c*cos(theta0) #Total energy (omit the constant (1/2)*m*L^2)
oscillating = (E-2*c < -0.01)
if oscillating == True:
    #Find the period here
    theta_max = acos( cos(theta0)-(omega0**2)/(2*c) )
    f = (lambda theta: 2*sqrt(2/c)/sqrt(cos(theta)-cos(theta_max)) )
    period = quad(f,0,theta_max)[0]
    #solve the ODE in one period
    t = linspace(0,period,int(period*1000/time_step),endpoint=False) # period*1000/time_step counts how many timesteps
    pend_ode = (lambda y,t: [y[1],-c*sin(y[0])])
    ode_sol = odeint(pend_ode,[theta0,omega0], t)

(x0,y0) = (w//2,h//2)
L=200
r=15

class Pendulum:
    def __init__(self,main,theta=theta0,omega=omega0):
        self.canvas = Canvas(main,width=w,height=h,bg="white")
        self.canvas.pack(pady=10)
        self.theta = theta
        self.omega = omega
        self.time_ind = 0 # The current time should be t[self.time_ind]
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.rod = self.canvas.create_line(x0,y0,position[0],position[1],width=2)
        global img
        img = Image.open("brown.png").resize((120,120),Image.ANTIALIAS)
        self.img_rotated = ImageTk.PhotoImage(img.rotate(self.theta*(180/pi)))
        self.bob = self.canvas.create_image(position[0],position[1],image=self.img_rotated)
        self.activate_motion()

    def redraw(self):
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.canvas.coords(self.rod,x0,y0,position[0],position[1])
        self.canvas.coords(self.bob,position[0],position[1])
        self.img_rotated = ImageTk.PhotoImage(img.rotate(self.theta*(180/pi)))
        self.canvas.itemconfig(self.bob,image=self.img_rotated)

    def update_data(self):
        self.time_ind += 1
        self.time_ind %= len(t)
        self.theta = ode_sol[self.time_ind][0]
        self.omega = ode_sol[self.time_ind][1]

    def activate_motion(self):
        self.update_data()
        self.redraw()
        root.after(time_step,self.activate_motion)

root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

pendulum = Pendulum(root)
root.mainloop()