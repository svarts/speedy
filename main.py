import tkinter as tk 
import speedtest_cli as speedtest

root = tk.Tk()
root.title("SPEEDY")
root.geometry("310x550")
root.resizable(False, False)
root.configure(bg="#1f1d2d")

#icon
image_icon = tk.PhotoImage(file='img/logo.png')
root.iconphoto(False, image_icon)

#images
Top = tk.PhotoImage(file='img/indicators.png')
label = tk.Label(root, image=Top, bg='#1f1d2d').pack() 

Main = tk.PhotoImage(file='img/main.png')
label = tk.Label(root, image=Main, bg='#1f1d2d').pack(pady=(5,0)) 

Button = tk.PhotoImage(file='img/button.png')
button_label = tk.Label(root, image=Button, bg='#1f1d2d', bd=0, activebackground="#1f1d2d", cursor="hand2")
button_label.pack(pady=2)

#label
tk.Label(root, text='PING', font='helvetica 13 normal', bg='#0E0D1B').place(x=43, y=18)
tk.Label(root, text='DOWNLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=116, y=18)
tk.Label(root, text='UPLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=220, y=18)

root.mainloop()