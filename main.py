import tkinter as tk 
import speedtest_cli as speedtest

root = tk.Tk()
root.title("Speddy")
root.geometry("310x550")
root.resizable(False, False)
root.configure(bg="#1f1d2d")

def Checkbutton():
    test = speedtest.Speedtest()

    Uploading = round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)

    downloading = round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames = []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)
    
#icon
image_icon = tk.PhotoImage(file='img/logo.png')
root.iconphoto(False, image_icon)

#images
Top = tk.PhotoImage(file='img/indicators.png')
label = tk.Label(root, image=Top, bg='#1f1d2d').pack() 

Main = tk.PhotoImage(file='img/main.png')
label = tk.Label(root, image=Main, bg='#1f1d2d').pack(pady=(5,0)) 

button = tk.PhotoImage(file='img/button.png')
Button = tk.Button(root, image=button, bg="#1f1d2d", bd="0", activebackground="#1f1d2d", width=199, height=49, cursor="hand", command=tk.Checkbutton)
Button.configure(bg="#1f1d2d")
Button.pack(pady=5)

#main's text

#indicator's text
tk.Label(root, text='PING', font='helvetica 13 normal', bg='#0E0D1B').place(x=43, y=18)
tk.Label(root, text='DOWNLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=116, y=18)
tk.Label(root, text='UPLOAD', font='helvetica 13 normal', bg='#0E0D1B').place(x=220, y=18)

#speed
tk.Label(root, text='MS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=53, y=92)
tk.Label(root, text='MBPS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=140, y=92)
tk.Label(root, text='MBPS', font='helvetica 10 normal', bg='#0E0D1B', fg='white').place(x=234, y=92)

tk.Label(root, text='Download', font='helvetica 16 normal', bg='#0E0D1B', fg='white').place(x=120, y=260)
tk.Label(root, text='MBPS', font='helvetica 16 normal', bg='#0E0D1B', fg='white').place(x=132, y=370)

ping = tk.Label(root, text='00', font='helvetica 16 normal',bg='#0E0D1B', fg='white')
ping.place(x=52, y=64)

download = tk.Label(root, text='00', font='helvetica 16 normal',bg='#0E0D1B', fg='white')
download.place(x=145, y=64)

upload = tk.Label(root, text='00', font='helvetica 16 normal',bg='#0E0D1B', fg='white')
upload.place(x=238, y=64)

Download = tk.Label(root, text='00', font='helvetica 38 bold',bg='#0E0D1B', fg='aqua')
Download.place(x=160, y=320, anchor='center')

root.mainloop()

