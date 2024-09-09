from tkinter import *
from pytube import YouTube
from moviepy.editor import *
from tkinter import filedialog

import shutil

def getPath():
    path=filedialog.askdirectory()
    pathLabel.config(text=path) 

def download():
    videoPath=urlEntry.get()
    downloadPath=pathLabel.cget("text")
    msg=Label(root,text="Download Started.....")
    canvas.create_window(205,255,window=msg)
    mp4=YouTube(videoPath).streams.get_highest_resolution().download()
    videoClip=VideoFileClip(mp4)

    #audio
    audiioFile=videoClip.audio
    audiioFile.write_audiofile('audio123.mp3')
    audiioFile.close()
    shutil.move('audio123.mp3', downloadPath)
    #audio
    videoClip.close()
    shutil.move(mp4, downloadPath)
    msg=Label(root,text="Download complete")
    canvas.create_window(200,250,window=msg)


root=Tk()
root.title("Video Downloader")
canvas=Canvas(root, width=400, height=300)
canvas.pack()

#app label
applabel=Label(text="Video Downloader", fg="Red", font=("Arial",20))
canvas.create_window(200,20,window=applabel)

#entry2 accept vdourl
urlLabel=Label(text="Enter Video Url🔗", fg="Black", font=("Arial"))
urlEntry=Entry(root)
canvas.create_window(200,80,window=urlLabel)
canvas.create_window(200,100,window=urlEntry)

#select download folder
pathLabel=Label(text="Select path to download", fg="Black", font=("Arial"))
pathBtn=Button(text="Select path📂", command=getPath)
canvas.create_window(200,140,window=pathLabel)
canvas.create_window(200,170,window=pathBtn)


#download
downloadBtn=Button(root,text="Download",fg="White", bg="red", command=download)
canvas.create_window(200,220,window=downloadBtn)


root.mainloop()