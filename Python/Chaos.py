import tkinter as tk
import random

class chaos(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x800")
        self.point1 = [400,0,401,1]
        self.point2 = [0,799,1,800]
        self.point3 = [799,799,800,800]
        self.pointS = [450,125,451,126]


        self.w = tk.Canvas(self,width = 800,height = 800,bg = 'black')
        self.w.pack()

        self.w.create_rectangle(self.point1[0],self.point1[1],self.point1[2],self.point1[3],outline = 'white')
        self.w.create_rectangle(self.point2[0],self.point2[1],self.point2[2],self.point2[3],outline = 'white')
        self.w.create_rectangle(self.point3[0],self.point3[1],self.point3[2],self.point3[3],outline = 'white')
        self.w.create_rectangle(self.pointS[0],self.pointS[1],self.pointS[2],self.pointS[3],outline = 'white')

        self.chaosLoop()

    def chaosPoint(self):
        i = random.randint(1,4)
        if i == 1:
            self.pointS[0] = (self.pointS[0] + self.point1[0])/2
            self.pointS[1] = (self.pointS[1] + self.point1[1])/2
            self.pointS[2] = (self.pointS[2] + self.point1[2])/2
            self.pointS[3] = (self.pointS[3] + self.point1[3])/2
        if i == 2:
            self.pointS[0] = (self.pointS[0] + self.point2[0])/2
            self.pointS[1] = (self.pointS[1] + self.point2[1])/2
            self.pointS[2] = (self.pointS[2] + self.point2[2])/2
            self.pointS[3] = (self.pointS[3] + self.point2[3])/2
        if i == 3:
            self.pointS[0] = (self.pointS[0] + self.point3[0])/2
            self.pointS[1] = (self.pointS[1] + self.point3[1])/2
            self.pointS[2] = (self.pointS[2] + self.point3[2])/2
            self.pointS[3] = (self.pointS[3] + self.point3[3])/2
        self.w.create_rectangle(self.pointS[0],self.pointS[1],self.pointS[2],self.pointS[3],outline = 'white')
    



    def chaosLoop(self):
        self.after(1,self.chaosLoop)
        self.chaosPoint()

    
if __name__ == "__main__":
    chaos().mainloop()
        