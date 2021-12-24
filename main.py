from tkinter import *
import random
import time
tk = Tk()
tk.title("Ping Pong")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
angles = [-2,-3,1,-1,2,3,5]
posangles = [1,2,3]
negangles = [-2,-1,-3]
class Ball:
  def __init__(self,canvas,color):
    self.canvas = canvas
    self.id = canvas.create_oval(10,10,25,25,fill=color)
    self.canvas.move(self.id,245,100)
    self.x = 0
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
  def draw(self):
    self.canvas.move(self.id,self.x,self.y)
    pos = self.canvas.coords(self.id )
    if pos[1] <= 0:
      self.y = 2
      random.shuffle(angles)
      self.x = angles[1] 
    if pos[3] >=self.canvas_height:
      self.y = -2
      random.shuffle(angles)
      self.x = angles[2] 
    if pos[0] <= 0:
      random.shuffle(negangles)
      self.x = 3
    if pos[2] >= 500:
      random.shuffle(posangles)
      self.x = -3

class paddle:
  def left(self,evt):
    self.x = 2
  
  def right(self,evt):
    self.x = 2
  def __init__(self,canvas,color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(0,0,100,10,fill=color)
    self.canvas.move(self.id,200,300)
    self.x = 0
    self.canvas_width = self.canvas.winfo_width()
    self.canvas.bind_all('<KeyPress-Left>',self.left)
    self.canvas.bind_all('<KeyPress-Right>',self.right)
  
  def draw(self):
    self.canvas.move(self.id,self.x,0)
    pos = self.canvas.coords(self.id)
    if pos[0] <= 0 :
      self.x = 0
    if pos[2] >= self.canvas_width:
      self.x = 0
ball = Ball(canvas,'red')
paddle(canvas,'green')
while True:
  paddle.draw
  ball.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)