from tkinter import*
import time

# Initialize main window
win=Tk()
win.title("Digital Clock")
win.geometry("500x200")
win.configure(bg="#0f0d11")

# Time label
Label=Label(win,font=("Arial",60,"bold"),bg="#ac9c54",fg="black",bd="25",padx=20, pady=20)
Label.grid(row=0,column=1)
Label.pack(pady=30)

# Clock function
def clock():
    t1=time.strftime("%H:%M:%S")
    Label.config(text=t1)
    Label.after(1000,clock)

clock()
win.mainloop()
