#!/usr/bin/python

import urllib

## streaming via a capable browser (Chromium works well, Iceweasel doesn't)
#import webbrowser

## streaming with vlc
import subprocess

## comment from HERE
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
    ## loop until the user makes a decision and the window is destroyed
    msgBox.waitForInput()
    return msgBox.getString()

link = getText("Inserisci il link")
## to HERE if you want a CLI

## decomment this for CLI 
#link = raw_input("Inserisci il link: ")

## this fetches the link to mp4 version of the video
## and puts it inside variable vidUrl
source = urllib.urlopen(link)
for line in source:
  if "videoURL_MP4" in line:
    vidTemp = line.split("\"") 
vidUrl = vidTemp[1]

## browser streaming
#webbrowser.open_new(vidUrl)

## vlc streaming
subprocess.call(["vlc", vidUrl])

################################################################################
## use this if you prefer to copy the link in the clipboard
## and then paste it in your favourite streaming program
## This doesn't work on Gnome :-(

#text = str(vidUrl)
#r = Tk()
#r.withdraw()
#r.clipboard_clear()
#r.clipboard_append(text)
#r.destroy()
################################################################################

################################################################################
## clipboard version for Gnome

#import pygtk
#pygtk.require('2.0')
#import gtk

## get the clipboard
#clipboard = gtk.clipboard_get()

#text = str(vidUrl)
## set the clipboard text data
#clipboard.set_text(text)

## make our data available to other applications
#clipboard.store()
################################################################################