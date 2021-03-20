import tkinter as tk
from tkinter.constants import HORIZONTAL
from PIL import Image, ImageTk

class Display:
    
    def __init__(self, height, width,email_list):
      self.email_list=email_list
      self.root=tk.Tk()
      self.root.title("Email Board")
      self.content = tk.Frame(self.root)
      self.frame = tk.LabelFrame(self.content, borderwidth=5, relief="ridge", width=width, height=height,text="Current Emails")
      
      self.canvas = tk.Canvas(self.frame,height = height,width =width)
      self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
      self.scrollable_frame = tk.Frame(self.canvas)
      self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
      self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
      self.canvas.configure(yscrollcommand=self.scrollbar.set)
      for email in self.email_list:
            btn=tk.Button(self.scrollable_frame,bg="yellow", text=email,)
            btn["command"]=lambda btn=btn:self.deleteEmail(btn)
            btn.pack()
      self.canvas.pack(side="left", fill="both", expand=True)
      self.scrollbar.pack(side="right", fill="y")
      self.frame.pack()

      
      
      self.enter_email_label = tk.Label(self.content, text="Enter email :")
      self.email_entry = tk.Entry(self.content)
      self.ok = tk.Button(self.content, text="Enter",bg="green",command=lambda:self.pressedOk())
      self.cancel = tk.Button(self.content, text="Cancel",bg="red",command=lambda:self.pressedCancel())
      
      
      self.content.grid(column=0, row=0,sticky=(tk.N,tk. S, tk.E, tk.W))
      self.frame.grid(column=0, row=0, columnspan=3, rowspan=2,sticky=(tk.N,tk. S, tk.E, tk.W))
      self.enter_email_label.grid(column=3, row=0, columnspan=2,sticky=(tk.N, tk.W), padx=5)
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
  
    def pressedOk(self):
        value=self.email_entry.get()
        if value:
            self.email_list.append(value)
            self.addNewEmail(value)

        else:
            print("no ")
    
    def pressedCancel(self):
        self.email_entry.delete(0, 'end')
        
    def addNewEmail(self,email):
        btn=tk.Button(self.scrollable_frame,bg="yellow", text=email,)
        btn["command"]=lambda btn=btn:self.deleteEmail(btn)
        btn.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
    def deleteEmail(self,btn: tk.Button):
        self.email_list.remove(btn['text'])
        btn.destroy()

        
    def __del__(self):
        with open("emails.txt", "w") as file:
            for item in self.email_list:
                if not item:
                  continue
                file.write("%s" % item)
                file.write(" ")
             
         


########################################### this is the main code run###################################
emails=[]

with open("emails.txt", "r") as file:
    email=file.read()
    emails=email.split(" ")
    emails.pop()
    print(emails)
      
    
Display(600,600,emails).run()
      
    