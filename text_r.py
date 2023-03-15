import tkinter as tk
import pyttsx3 as p3
import os
os.system('cls')

eg = p3.init()

def read_text():
    """Function to read the text inputted in the text box"""
    text = textbox.get("1.0", "end-1c")  
    eg.say(text)  
    eg.runAndWait()

def clear_text():
    """Function to clear the text in the text box"""
    textbox.delete("1.0", "end")

window = tk.Tk()

label = tk.Label(window, text="Enter text:")
label.pack()
textbox = tk.Text(window, height=10, width=50)
textbox.pack()


read_button = tk.Button(window, text="play", command=read_text)
read_button.pack()


clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack()


window.mainloop()