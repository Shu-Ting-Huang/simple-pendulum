from tkinter import Tk,Canvas,PhotoImage
from math import cos,sin,pi
from PIL import Image,ImageTk
root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

w = 1250
h = 600
time_step=1

(x0,y0) = (w//2,h//2)
L=200
r=15

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=10)

class Pendulum:
    def __init__(self,theta=-pi/4,omega=-0.5):
        self.theta = theta
        self.omega = omega
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        self.rod = my_canvas.create_line(x0,y0,position[0],position[1],width=2)
        global img,img_rotated
        img = Image.open("brown.png").resize((120,120),Image.ANTIALIAS)
        img_rotated = ImageTk.PhotoImage(img.rotate(self.theta*(180/pi)))
        self.bob = my_canvas.create_image(position[0],position[1],image=img_rotated)
        self.activate_motion()

    def redraw(self):
        position = (x0+L*sin(self.theta),y0+L*cos(self.theta))
        my_canvas.coords(self.rod,x0,y0,position[0],position[1])
        my_canvas.coords(self.bob,position[0],position[1])

    def update_data(self):
        self.theta += self.omega*time_step/1000

    def activate_motion(self):
        self.update_data()
        self.redraw()
        root.after(time_step,self.activate_motion)
    
pendulum = Pendulum()
root.mainloop()