import tkinter as tk
from tkinter import *
from random import seed
from random import random
from PIL import ImageGrab
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.color = 'red'

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas_panel = tk.PanedWindow(self)

        self.canvas_label = tk.LabelFrame(self.canvas_panel, text='Canvas', width=1500, height=1000)

        self.canvas = tk.Canvas(self.canvas_label, bg="white", width=3000, height=1000)

        #self.draw(self.canvas,self.rSlide,self.gSlide,self.bSlide)

        self.canvas_panel.add(self.canvas_label)    
        
        self.save_panel = tk.PanedWindow(self)
        self.save_button = tk.Button(self.save_panel)
        self.save_button["text"] = "Save"
        self.save_button["command"] = self.save

        self.save_panel.add(self.save_button)

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)

        self.save_panel.add(self.quit)
        self.save_panel.pack(side="bottom")

#        self.slider_panel = tk.PanedWindow(self)
        self.slider_label = tk.LabelFrame(self.canvas_panel, text='Options', width=500, height=100)
        self.slider_panel = tk.PanedWindow(self.slider_label)
        self.slider_panel.add(self.slider_label)
        
        self.update_button = tk.Button(self.slider_panel)
        self.update_button["text"] = "Update"
        self.update_button["command"] = self.update
        self.slider_panel.add(self.update_button)
        
        #xrSlide
        self.xrSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.xrSlide.pack()
        self.xrLabel = Label(self.slider_label, text="xrNoise")
        self.xrLabel.pack()
        #yrSlide
        self.yrSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.yrSlide.pack()
        self.yrLabel = Label(self.slider_label, text="yrNoise")
        self.yrLabel.pack()
        #xbSlide
        self.xbSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.xbSlide.pack()
        self.xbLabel = Label(self.slider_label, text="xbNoise")
        self.xbLabel.pack()
        #ybSlide
        self.ybSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.ybSlide.pack()
        self.ybLabel = Label(self.slider_label, text="ybNoise")
        self.ybLabel.pack()
        #xgSlide
        self.xgSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.xgSlide.pack()
        self.xgLabel = Label(self.slider_label, text="xgNoise")
        self.xgLabel.pack()
        #ygSlide
        self.ygSlide = Scale(self.slider_label, from_=1,to=20,orient=HORIZONTAL)
        self.ygSlide.pack()
        self.ygLabel = Label(self.slider_label, text="ygNoise")
        self.ygLabel.pack()
        #gridSlide
        self.gridSlide = Scale(self.slider_label, from_=5,to=32,orient=HORIZONTAL)
        self.gridSlide.pack()
        self.gridLabel = Label(self.slider_label, text="gridSize")
        self.gridLabel.pack()
        #strokeSlide
        self.strokeSlide = Scale(self.slider_label, from_=2,to=4,orient=HORIZONTAL)
        self.strokeSlide.pack()
        self.strokeLabel = Label(self.slider_label, text="strokeDiv")
        self.strokeLabel.pack()
        #blackground
        self.blackground = IntVar()
        self.check = Checkbutton(self.slider_label, text="for dark mode", variable=self.blackground)
        self.check.pack()
        
        self.slider_panel.pack(side="top")

        self.canvas_panel.add(self.slider_label)
        self.canvas_panel.pack(side="top")

        #self.slider_panel.pack(side="right")

        
    def hexColor(self, rgb):
        return "#%02x%02x%02x" % rgb
    
    def save(self):
        #print("Saved (not really)")
        #self.color = 'green'
        #self.draw(self.canvas,self.rSlide,self.gSlide,self.bSlide)
        x=root.winfo_rootx()+self.canvas.winfo_x()
        y=root.winfo_rooty()+self.canvas.winfo_y()
        x1 = x+self.canvas.winfo_width()
        y1=y+self.canvas.winfo_height()
        ImageGrab.grab().crop((x+3,y+3,x1-3,y1-3)).save("catcrossing.png")
    def darkmode(self):
        if self.blackground.get() == 1:
            self.canvas["bg"] = "black"
        else:
            self.canvas["bg"] = "white"

    def update(self):
        self.darkmode()
        self.draw(self.canvas,self.xrSlide,self.yrSlide,self.xbSlide,self.ybSlide,self.xgSlide,self.ygSlide,self.gridSlide,self.strokeSlide)
        
    def noise(self, y, x):
        n = y * x / 100.0
        
        n = n - int(n)
        
        if n > 1:
            print(str(y) + " " + str(x))
            
        return n 
    
    def draw(self, canvas, xrNoise, yrNoise, xbNoise, ybNoise, xgNoise, ygNoise, gridSize, strokeDiv):
        canvas.delete("all")
        noiseScale = 0.1
        width = 1500
        height = 1000
        x = 0
        seed(1)
        xrNoiseSet = xrNoise.get()
        xbNoiseSet = xbNoise.get()
        xgNoiseSet = xgNoise.get()
        
        while x <= width + gridSize.get():
            yrNoiseStart = yrNoise.get()
            ybNoiseStart = ybNoise.get()
            ygNoiseStart = ygNoise.get()
            yrNoiseSet = yrNoiseStart
            ybNoiseSet = ybNoiseStart
            ygNoiseSet = ygNoiseStart
            y = 0
            while y <= height + gridSize.get(): 
                red = int(255 * self.noise(yrNoiseSet, xrNoiseSet))
                blue = int(255 * self.noise(ybNoiseSet, xbNoiseSet))
                green = int(255 * self.noise(ygNoiseSet, xgNoiseSet))
                
                
                if(random() > 0.5):
                    canvas.create_line(x,y,x+gridSize.get(),y+gridSize.get(), fill=self.hexColor((red,blue,green)), width = gridSize.get()/strokeDiv.get(),smooth=True,splinesteps=24)
                else:
                    canvas.create_line(x,y+gridSize.get(),x+gridSize.get(),y, fill=self.hexColor((red,blue,green)), width = gridSize.get()/strokeDiv.get(),smooth=True,splinesteps=24)
                y += gridSize.get()
                
                yrNoiseSet += noiseScale
                ybNoiseSet += noiseScale
                ygNoiseSet += noiseScale
                
            x += gridSize.get()
            
            xrNoiseSet += noiseScale
            xbNoiseSet += noiseScale
            xgNoiseSet += noiseScale
                    
        
        canvas.pack()
    


root = tk.Tk()
app = Application(master=root)
app.mainloop()
