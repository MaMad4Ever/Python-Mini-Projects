from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('450x300')
root.title("Youtube Video Downloader")

Label(root, text='Youtube Video Downloader',
      font='arial 15 bold').pack()

link = StringVar()
filename = StringVar()

Label(root, text='Paste Link Here:', font='arial 13 bold').place(x=160, y=40)
link_enter = Entry(root, width=45, textvariable=link).place(
    x=50, y=90)

def Download():

    Label(root, text='Downloading', font='arial 13').place(x=180, y=210)

    url = YouTube(str(link.get()))

    video = url.streams.get_highest_resolution()

    video.download()

    Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)


Button(root, text='Download', font='arial 15 bold',
       padx=2, command=Download).place(x=180, y=150)

root.mainloop()
