from tkinter import*

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handel_keypress(event):
    """""Print the character associated to the key pressed"""""
    print(event.char)

window.blind("<Key>", handel_keypress)

def handel_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.blind("<Button-1>", handel_click)

window.mainloop