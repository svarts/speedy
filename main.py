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

button = tk.PhotoImage(file='img/button.png')
Button = tk.Button(root, image=button, bg="#1f1d2d", bd="0", activebackground="#1f1d2d", width=199, height=49, cursor="hand")
Button.configure(bg="#1f1d2d")
Button.pack(pady=2)

#main's text


#indicator's text
tk.Label(root, text='PING', font='helvetica 13 normal', bg='#0E0D1B').place(x=43, y=18)
tk.Label(root, text='DOWNLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=116, y=18)
tk.Label(root, text='UPLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=220, y=18)

#speed
tk.Label(root, text='MS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=53, y=92)
tk.Label(root, text='MBPS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=140, y=92)
tk.Label(root, text='MBPS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=234, y=92)

root.mainloop()