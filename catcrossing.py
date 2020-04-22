import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.color = 'red'

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas_panel = tk.PanedWindow(self)

        self.canvas_label = tk.LabelFrame(self.canvas_panel, text='Canvas', width=100, height=100)

        self.canvas = tk.Canvas(self.canvas_label, bg="purple")

        self.draw(self.canvas)

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
        self.slider_label = tk.LabelFrame(self.canvas_panel, text='Options', width=100, height=100)

        self.canvas_panel.add(self.slider_label)
        self.canvas_panel.pack(side="top")

        #self.slider_panel.pack(side="right")

    def save(self):
        print("Saved (not really)")
        self.color = 'green'
        self.draw(self.canvas)


    def draw(self, canvas):
        coord = 10, 50, 240, 210
        arc = canvas.create_arc(coord, start=0, extent=150, fill=self.color)
        canvas.pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
