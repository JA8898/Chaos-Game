import tkinter as tk
import random
import sys
#creates a class using tkinter
class chaos(tk.Tk):
    # the init function, creates empty arrays, binds hotkeys, reates canvas to place points on
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Chaos Game")
        self.geometry("800x800")
        self.startPoints = []
        self.lastPoints = []
    
        self.w = tk.Canvas(self,width = 800,height = 800,bg = 'black')
        self.w.pack()
        self.bind("<Button-1>",self.plotPoint)
        self.bind ("s", self.start)
        self.bind("<Escape>", self.close)
        self.bind("r",self.reset)


    # this plots the points where the user clicks, allowing for the user to pick their points
    def plotPoint(self,event):
        self.w.create_rectangle(event.x,event.y,event.x+1,event.y+1,outline = 'white')
        self.startPoints.append([event.x,event.y])

    
    def start(self,event):
        #stops new points from being plotted by the user
        self.unbind("<Button-1>")
        #unbinds s
        self.unbind("s")
        #sets this equal to the last point in the array
        self.pointS = [self.startPoints[-1][0],self.startPoints[-1][1]]
        #tells the program to run
        self.running = True
        #removes the last point in the array, since it is s
        self.startPoints.pop()
        #starts the loop
        self.chaosLoop()


    #using the last point, gets the average between the last point and a random point in the startpoints list
    def chaosPoint(self,i):          
        self.pointS[0] = (self.pointS[0] + self.startPoints[i][0])/2
        self.pointS[1] = (self.pointS[1] + self.startPoints[i][1])/2
        self.w.create_rectangle(self.pointS[0],self.pointS[1],self.pointS[0]+1,self.pointS[1]+1,outline = 'white')
        
    #runs when the escape key is pressed
    def close(self,event):
        sys.exit()

    #This rules only allows 3 points to be picked, allowing the 3 least recent points.
    def rules(self):
        i = random.randint(0,len(self.startPoints)-1)
        violation = False
        #if the point is in the last points array, it gets added, and violation is flaged
        for point in self.lastPoints:
            if i == point:
                violation = True
        #if there is no violation, this runs
        if not violation:
            #the last point gets added to the list
            self.lastPoints.append(i)
            #removes any extra points that can be used again
            if len(self.lastPoints) > (len(self.startPoints) - 3):
                self.lastPoints.pop(0)
            #plots the point
            self.chaosPoint(i)

    #reset function, runs when r is pressed, removes all points, re-binds keys and sets canvas to a pre-chaos state
    def reset(self,event):
        self.running = False
        self.w.delete("all")
        self.startPoints = []
        self.lastPoints = []
        self.bind("<Button-1>",self.plotPoint)
        self.bind ("s", self.start)

        

    def chaosLoop(self):
        #if program is running, run the loop after 1 second
        if self.running == True:
            self.after(1,self.chaosLoop)
        
        #this checks if there is greater than 3 starting points, meaning that 4 or more points, not including the starting point will need rules
        if len(self.startPoints) > 3:
            #runs the algorithm with additional rules
            self.rules()
        else:
            #if there is 3 or less, no additional rules are needed
            if len(self.startPoints) > 0:
                self.chaosPoint(random.randint(0,len(self.startPoints)-1))

    
if __name__ == "__main__":
    chaos().mainloop()
        