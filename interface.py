#!/usr/bin/env python2



from Tkinter import *

import rockpaperscissors


root = Tk()
root.title("A few Games to toy around with Python")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text= "Welcome to my page! Please select the game to play: ")
intro.pack(side=TOP)

rps_button = Button(mainframe, text= "Rock, Paper, Scissors", command = rockpaperscissors.gui)
rps_button.pack()

exit_button = Button(mainframe, text= "Quit", command= root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()