import tkinter as tk 
import speedtest 

root = tk.Tk()
label = tk.Label(root, text="Hello, tkinter!")
label.pack()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")

root.mainloop()