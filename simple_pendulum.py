from tkinter import Tk,Canvas
root = Tk()
root.title('Simple Pendulum')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window

w = 1250
h = 600

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=10)

root.mainloop()