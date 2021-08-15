from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Dir_Location = ""

def dirlocation():
    global Dir_Location
    Dir_Location = filedialog.askdirectory()
    pathconfig.config(text = Dir_Location)

def download():
    url = linkentryvar.get()
    yt = YouTube(url)
    music = yt.streams.filter(only_audio = True).first()
    music.download(Dir_Location)
    Complete.config(text = "Download Complete")


root = Tk()
root.title("YT Downloader")
root.iconbitmap('JHLTech.ico')
root.geometry("350x350")
root.columnconfigure(0,weight=1)

pathlabel = Label(root, text = "Select Output Folder:", font = ("Helvetica",15))
pathlabel.grid()

path = Button(root, width = 10, bg = "white", fg = "black", text = "Choose Path", command = dirlocation)
path.grid()

pathconfig = Label(root, text = "", fg = "green", font = ("jost",10))
pathconfig.grid()

linklabel = Label(root, text = "Enter URL Here:", font = ("Helvetica",15))
linklabel.grid()

linkentryvar = StringVar()
linkentry = Entry(root, width = 50, textvariable = linkentryvar)
linkentry.grid()

Complete = Label(root, text = "", fg = "green", font = ("jost",10))
Complete.grid()

Downloadbtn = Button(root, text = "Download", width = 10, bg = "white", fg = "black", command = download)
Downloadbtn.grid()

devlabel = Label(root, text = "By JLund1n", fg = "purple", font = ("Helvetica",10))
devlabel.grid()

root.mainloop()