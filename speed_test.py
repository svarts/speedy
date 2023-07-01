import tkinter as tk 
import speedtest_cli as speedtest

root = tk.Tk()
root.title("SPEEDY")
root.geometry("310x550")
root.resizable(False, False)
root.configure(bg="#1f1d2d")

#icon
image_icon = tk.PhotoImage(file='logo.png')
root.iconphoto(False, image_icon)

#images
Top = tk.PhotoImage(file='indicators.png')
label = tk.Label(root, image=Top, bg='#1f1d2d').pack() 

Main = tk.PhotoImage(file='main.png')
label = tk.Label(root, image=Main, bg='#1f1d2d').pack()

Button = tk.PhotoImage(file='button.png')
label = tk.Label(root, image=Button, bg='#1f1d2d').pack()

root.mainloop()