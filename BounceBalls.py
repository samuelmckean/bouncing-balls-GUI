from Ball import Ball
from tkinter import *

class BounceBalls:
    def __init__(self):
        self.ballList = [] # create a list to store balls

        window = Tk() # create a window
        window.title("Bouncing Balls") # set a title

        self.width = 350 # width of canvas
        self.height = 150 # height of canvas
        self.canvas = Canvas(window, bg = "white", width = self.width,
                        height = self.height)
        self.canvas.pack()

        # create buttons to stop, resume, add, and remove balls and a
        # frame to hold buttons
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        
        self.sleepTime = 100 # set a sleep time
        self.isStopped = False
        self.animate()

        window.mainloop() # create event loop;

    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def remove(self):
        self.ballList.pop()

    def animate(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # sleep
            self.canvas.update() # update canvas
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
            ball.x + ball.radius, ball.y + ball.radius, fill = ball.color,
            tags = "ball")

BounceBalls() # create GUI
