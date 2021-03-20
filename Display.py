import tkinter as tk
from tkinter.constants import HORIZONTAL
from PIL import Image, ImageTk

class Display:
    
    def __init__(self, height, width):
      self.root=tk.Tk()
      self.root.title("Email Board")
      self.content = tk.Frame(self.root)
      self.frame = tk.LabelFrame(self.content, borderwidth=5, relief="ridge", width=width, height=height,text="Current Emails")
      self.enter_email = tk.Label(self.content, text="Enter email :")
      self.email_entry = tk.Entry(self.content)
      self.ok = tk.Button(self.content, text="Enter")
      self.cancel = tk.Button(self.content, text="Cancel")
      
      
      self.content.grid(column=0, row=0,sticky=(tk.N,tk. S, tk.E, tk.W))
      self.frame.grid(column=0, row=0, columnspan=3, rowspan=2,sticky=(tk.N,tk. S, tk.E, tk.W))
      self.enter_email.grid(column=3, row=0, columnspan=2,sticky=(tk.N, tk.W), padx=5)
      self.email_entry.grid(column=3, row=1, columnspan=2,sticky=(tk.N,tk.E,tk.W), pady=5, padx=5)
      self.ok.grid(column=3, row=3)
      self.cancel.grid(column=4, row=3)
      
      self.root.columnconfigure(0, weight=1)
      self.root.rowconfigure(0, weight=1)
      self.content.columnconfigure(0, weight=3)
      self.content.columnconfigure(1, weight=3)
      self.content.columnconfigure(2, weight=3)
      self.content.columnconfigure(3, weight=1)
      self.content.columnconfigure(4, weight=1)
      self.content.rowconfigure(1, weight=1)
  
    def run(self):

        self.root.mainloop()
        
    def __del__(self):
        print('Destructor called.')
         

Display(600,600).run()
      
    