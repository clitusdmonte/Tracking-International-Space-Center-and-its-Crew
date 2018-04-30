#Author: Clitus Dmonte
#Date: 04/06/2018
#Course Number: ITMD-513

from tkinter import *
from PIL import Image, ImageTk

#HomeWindow() def sets option menu for user to select tracking location
def HomeWindow(root):
    #setting home window
    global HomeTracking
    root.withdraw()
    HomeTracking = Toplevel()
    HomeTracking.title("Tracking Window")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    HomeTracking.geometry("%dx%d+%d+%d" % (width, height, x, y))

    #loading background image
    load = Image.open('images/bg_home.jpg')
    render = ImageTk.PhotoImage(load)
    bg_img = Label(HomeTracking, image=render)
    bg_img.image = render
    bg_img.place(x=0, y=0)

    tkvar = StringVar(HomeTracking)
    #Location options for tracking International space center
    choices = {'london', 'Tokyo', 'Space Center, Houston', 'India', 'Russia','England','Germany','China'}
    tkvar.set('Space Center, Houston')  #default location option

    popupMenu = OptionMenu(HomeTracking, tkvar, *choices)
    Label(HomeTracking,  text="Choose a Location from which ISS is to be Tracked").pack(pady=20)
    popupMenu.pack(pady=20)
    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())
    tkvar.trace('w', change_dropdown)
    btn_iss = Button(HomeTracking, text='Track ISS and its crew', width=50, command= lambda: Track(tkvar.get(), root)).pack(pady=20)

#Track() def imports tracker file and send user selected tracking location to track International space center
def Track(trackLoc, root):
    HomeTracking.destroy()
    root.destroy()
    import project.tracker;

    object1 = project.tracker.ClassA()
    object1.run(str(trackLoc))