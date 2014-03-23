#!/usr/bin/python

import urllib

#streaming via a capable browser (Chromium works well, Iceweasel doesn't)
#import webbrowser

#streaming with vlc
import subprocess

# gui
from Tkinter import *

class takeInput(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)
        self.root.bind("<Return>", self.gettext2)
        

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Link')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='Fatto',command=self.gettext)
        b.pack(side='right')
        b2 = Button(r,text='Incolla il link',command=lambda: self.e.event_generate("<<Paste>>"))
        b2.pack(side='right')
        

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def gettext2(self,key):
        self.string = self.e.get()
        self.root.destroy()    

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()

def getText(requestMessage):
    msgBox = takeInput(requestMessage)
    #loop until the user makes a decision and the window is destroyed
    msgBox.waitForInput()
    return msgBox.getString()

link = getText("Inserisci il link")
# gui (rimuovere tutto e decommentare il successivo se
# si preferisce da riga di comando)
#link = raw_input("Inserisci il link: ")
source = urllib.urlopen(link)
for line in source:
  if "videoURL_MP4" in line:
    vidTemp = line.split("\"") 
vidUrl = vidTemp[1]

#browser streaming
#webbrowser.open_new(vidUrl)

#vlc streaming
subprocess.call(["vlc", vidUrl])
