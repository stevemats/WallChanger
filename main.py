#!/usr/bin/python
# -*- coding: utf-8 -*-
# Wallpaper Changer By Steve

from tkinter import *
from tkinter import filedialog
# from wallpaper import set_wallpaper

try:
    from wallpaper import set_wallpaper
except ImportError:
    import os
    print ("wallpaper isn\'t installed, installing now.")
    os.system('python -m pip install --user wallpaper')
    print ('wallpaper has been installed, restarting WallChanger.')

# user define funtion
def change_wall():
    
    # set your photo
    try:
        set_wallpaper(str(path.get()))
        check = "success"
  
    except:
  
        check = "Wallpaper not found !"
    result.set(check)
  
  
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select an Image",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    path.set(filename)
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    return filename
  
  
# tkinter object & bg color
master = Tk()
master.title('WallChanger')
master.iconbitmap('resources\logo\wall.ico')
master.configure(bg='light grey')
master.geometry('930x250')
master.resizable(0, 0)
  
# Variable Classes in tkinter
result = StringVar()
path = StringVar()
  
  
label_file_explorer = Label(
    master, text="Select a image", width=100, fg="blue")
  
  
# Creating label for each info
# name using widget Label
Label(master, text="New image : ", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Status :", bg="light grey").grid(row=3, sticky=W)
  
  
# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
      bg="light grey").grid(row=3, column=1, sticky=W)
  
# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Select Image", command=browseFiles, bg="white")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
  
label_file_explorer.grid(column=1, row=1)
  
c = Button(master, text="Apply Image", command=change_wall, bg="white")
c.grid(row=2, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
  
mainloop()