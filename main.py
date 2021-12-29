from tkinter import *
import random
import time

tk = Tk()
tk.title("Ping Pong")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
angles = [-2, -3, 1, -1, 2, 3, 5]
posangles = [1, 2, 3]
negangles = [-2, -1, -3]
g = False
score = 0
print("Click the  Ping pong screen with your mouse screen and wait a bit ")
print ("Use the arrow keys to move around the paddle ")
time.sleep(4)
lives = 3
class Ball:
    def false(x):
        if x == True:
            return True
        else:
            return False

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        random.shuffle(angles)
        self.x = angles[0]
        self.y = -2
        self.live = 0 
        self.canvas_height = self.canvas.winfo_height()

    def strike(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                canvas.itemconfig(paddle, fill='blue')
                return True

        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = 0
            self.x = 0
            ball.live = 1
        if self.strike(self.canvas.coords(self.id)) == True:
            self.y = -3.4 

        if pos[0] <= 0:
            random.shuffle(negangles)
            self.x = 3
        if pos[2] >= 500:
            random.shuffle(posangles)
            self.x = -3


class paddle:
    def left(self, evt):
        self.x = -3

    def right(self, evt):
        self.x = 3
    def stop(self,evt):
      self.x = 0
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.canvas.bind_all('<KeyPress-Up>', self.stop)
        self.canvas.bind_all('<KeyPress-Down>', self.stop)
    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            if self.x == -3:
                self.x = 0
        if pos[2] >= self.canvas_width:
            if self.x == 3:
                self.x = 0
        self.canvas.move(self.id, self.x, 0)


paddle = paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
score = 0
scorestring = ("Score " + str(score))
x = canvas.create_text(65, 30, text=scorestring, font=('Times', 15))
livestring  = ("lives:"+ str(lives)) 
live = canvas.create_text(65,70,text = livestring,font=('Times',15),fill ='Black')
while 1:
    if lives !=0:
      if ball.live != 1:
        paddle.draw()
        ball.draw()
        score = score + 1
        scorestring = ("Score " + str(score))
        canvas.itemconfig(x, text=scorestring)
      else:
        lives = lives -1
        if lives != 0:
          ball.canvas.move (ball,0,300)
          ball.y = -15
          ball.x = -1.2
          ball.draw()
          livestring = ("lives:"+ str(lives)) 
          canvas.itemconfig(live,text=livestring )
          ball.live =0 
          time.sleep(1)
        else :
          livestring = ("lives:"+ str(lives)) 
          canvas.itemconfig(live,text='Lives:0')
          time.sleep(.1)
          for v in range (1,100):
            canvas.itemconfig(live,fill='White')
            tk.update()
            time.sleep(.015)
            canvas.itemconfig(live,fill='Red')
            tk.update()
            canvas.itemconfig (x,fill = 'White')
            tk.update()
            canvas.itemconfig (x,fill = 'Red')
            tk.update()
            time.sleep(.015)
          canvas.create_text(250, 50, text='Game Over', font=('Times', 30),fill= 'Red')
          tk.update_idletasks()
          tk.update()
          break
      tk.update_idletasks()
      tk.update()
      time.sleep(0.01)
    if lives==0 :
      canvas.create_text(250, 50, text='Game Over', font=('Times', 30),fill= 'Red')
      break

