from tkinter import Tk,Canvas,Label
from math import cos,sin,acos,pi,sqrt
from scipy.integrate import quad,odeint
from numpy import linspace
from decimal import Decimal
root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

w = 1250
h = 600
time_step=1

c = 1 #This constant is g/L
(theta0,omega0) = (0.001,-0.0) #Initial condition
E = omega0**2-2*c*cos(theta0) #Total energy (omit the constant (1/2)*m*L^2)
oscillating = (E-2*c < -0.01)
if oscillating == True:
    #Find the period here
    theta_max = acos( cos(theta0)-(omega0**2)/(2*c) )
    f=(lambda theta: 2*sqrt(2/c)/sqrt(cos(theta)-cos(theta_max)) )
    period = quad(f,0,theta_max)[0]
    #solve the ODE in one period
    t = linspace(0,period,int(period*1000/time_step),endpoint=False) # period*1000/time_step counts how many timesteps
    pend_ode = (lambda y,t: [y[1],-c*sin(y[0])])
    ode_sol = odeint(pend_ode,[theta0,omega0], t)

    theta_test = linspace(0,0.001*pi,len(t),endpoint=False)

(x0,y0) = (w//2,h//2)
L=200
r=15

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack()

class Pendulum:
    def __init__(self,theta=theta0,omega=omega0):
        self.theta = theta
        self.omega = omega
        self.time_ind = 0 # The current time should be t[self.time_ind]
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.rod = my_canvas.create_line(x0,y0,position[0],position[1],width=2)
        self.bob = my_canvas.create_oval(position[0]-r,position[1]-r,\
                                            position[0]+r,position[1]+r,fill="red")
        self.activate_motion()

    def redraw(self):
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        my_canvas.coords(self.rod,x0,y0,position[0],position[1])
        my_canvas.coords(self.bob,position[0]-r,position[1]-r,position[0]+r,position[1]+r)
        my_label.config(text="theta="+str(Decimal(self.theta).quantize(Decimal("1.000"))))

    def update_data(self):
        self.time_ind += 1
        self.time_ind %= len(t)
        self.theta += theta_test[self.time_ind]
        #self.omega += ode_sol[self.time_ind][1]

    def activate_motion(self):
        self.update_data()
        self.redraw()
        root.after(time_step,self.activate_motion)
    

my_label = Label(root,text="This is my label")
my_label.pack(pady=20)

pendulum = Pendulum()
root.mainloop()

import matplotlib.pyplot as plt

plt.plot(t, theta_test[:], 'b', label='theta_test(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()