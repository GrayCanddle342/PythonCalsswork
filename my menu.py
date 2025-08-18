from tkinter import *

window = IK()
window.title("Sample Frame")
window.geotery("300x200")

bouder_effects = [FLAT, SUNKEN RAISED, GROVEE, RIDGE ]

for r in border_effects:
    frame = Frame(master=window, relif=r, borderwidth- 5)
    frame.pick(side=LEFT)
    label = label(master=frame, text=r)
    label.pack()