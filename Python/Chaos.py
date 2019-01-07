import tkinter as tk
import random
import sys

class chaos(tk.Tk):
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



    def plotPoint(self,event):
        self.w.create_rectangle(event.x,event.y,event.x+1,event.y+1,outline = 'white')
        self.startPoints.append([event.x,event.y])

    
    def start(self,event):
        self.unbind("<Button-1>")
        self.pointS = [self.startPoints[-1][0],self.startPoints[-1][1]]
        self.startPoints.pop()
        self.chaosLoop()



    def chaosPoint(self,i):          
        self.pointS[0] = (self.pointS[0] + self.startPoints[i][0])/2
        self.pointS[1] = (self.pointS[1] + self.startPoints[i][1])/2
        self.w.create_rectangle(self.pointS[0],self.pointS[1],self.pointS[0]+1,self.pointS[1]+1,outline = 'white')
        

    def close(self,event):
        sys.exit()

    def rules(self):
        i = random.randint(0,len(self.startPoints)-1)
        violation = False
        for point in self.lastPoints:
            if i == point:
                violation = True
        if not violation:
            self.lastPoints.append(i)
            if len(self.lastPoints) > (len(self.startPoints) - 3):
                self.lastPoints.pop(0)
            self.chaosPoint(i)



    def chaosLoop(self):
        self.after(1,self.chaosLoop)
        if len(self.startPoints) > 3:
            self.rules()
        else:
            self.chaosPoint(random.randint(0,len(self.startPoints)-1))

    
if __name__ == "__main__":
    chaos().mainloop()
        