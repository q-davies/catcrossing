import tkinter as tk
from tkinter import *
from random import seed
from random import random
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
        self.xrSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.xrSlide.pack()
        self.xrLabel = Label(self.slider_label, text="xrNoise")
        self.xrLabel.pack()
        #yrSlide
        self.yrSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.yrSlide.pack()
        self.yrLabel = Label(self.slider_label, text="yrNoise")
        self.yrLabel.pack()
        #xbSlide
        self.xbSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.xbSlide.pack()
        self.xbLabel = Label(self.slider_label, text="xbNoise")
        self.xbLabel.pack()
        #ybSlide
        self.ybSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.ybSlide.pack()
        self.ybLabel = Label(self.slider_label, text="ybNoise")
        self.ybLabel.pack()
        #xgSlide
        self.xgSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.xgSlide.pack()
        self.xgLabel = Label(self.slider_label, text="xgNoise")
        self.xgLabel.pack()
        #ygSlide
        self.ygSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.ygSlide.pack()
        self.ygLabel = Label(self.slider_label, text="ygNoise")
        self.ygLabel.pack()
        #xaSlide
        self.xaSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.xaSlide.pack()
        self.xaLabel = Label(self.slider_label, text="xaNoise")
        self.xaLabel.pack()
        #yaSlide
        self.yaSlide = Scale(self.slider_label, from_=1,to=10,orient=HORIZONTAL)
        self.yaSlide.pack()
        self.yaLabel = Label(self.slider_label, text="yaNoise")
        self.yaLabel.pack()
        #gridSlide
        self.gridSlide = Scale(self.slider_label, from_=5,to=30,orient=HORIZONTAL)
        self.gridSlide.pack()
        self.gridLabel = Label(self.slider_label, text="gridSize")
        self.gridLabel.pack()
        #strokeSlide
        self.strokeSlide = Scale(self.slider_label, from_=2,to=4,orient=HORIZONTAL)
        self.strokeSlide.pack()
        self.strokeLabel = Label(self.slider_label, text="strokeDiv")
        self.strokeLabel.pack()
        
        self.slider_panel.pack(side="top")

        self.canvas_panel.add(self.slider_label)
        self.canvas_panel.pack(side="top")

        #self.slider_panel.pack(side="right")

        
    def hexColor(self, rgb):
        return "#%02x%02x%02x" % rgb
    
    def save(self):
        print("Saved (not really)")
        #self.color = 'green'
        #self.draw(self.canvas,self.rSlide,self.gSlide,self.bSlide)

    def update(self):
        self.draw(self.canvas,self.xrSlide,self.yrSlide,self.xbSlide,self.ybSlide,self.xgSlide,self.ygSlide,self.xaSlide,self.yaSlide,self.gridSlide,self.strokeSlide)
        
    def draw(self, canvas, xrNoise, yrNoise, xbNoise, ybNoise, xgNoise, ygNoise, xaNoise, yaNoise, gridSize, strokeDiv):
        canvas.delete("all")
        noiseScale = 0.1
        width = 1500
        height = 1000
        x = 0
        seed(1)
        while x <= width + gridSize.get():
            yrNoiseStart = yrNoise.get()
            ybNoiseStart = ybNoise.get()
            ygNoiseStart = ygNoise.get()
            y = 0
            while y <= height + gridSize.get(): 
                red = int(255 * random())
                blue = int(255 * random())
                green = int(255 * random())
                
                if(random() > 0.5):
                    canvas.create_line(x,y,x+gridSize.get(),y+gridSize.get(), fill=self.hexColor((red,blue,green)), width = gridSize.get()/strokeDiv.get(),smooth=True)
                else:
                    canvas.create_line(x,y+gridSize.get(),x+gridSize.get(),y, fill=self.hexColor((red,blue,green)), width = gridSize.get()/strokeDiv.get(),smooth=True)
                y += gridSize.get()
            x += gridSize.get()
                    
        
        canvas.pack()
    


root = tk.Tk()
app = Application(master=root)
app.mainloop()
