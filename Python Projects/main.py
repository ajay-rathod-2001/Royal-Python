# tkinter module and library - collection of module
# import tkinker for creating GUI apps

import tkinter as tk
from tkinter import filedialog, messagebox

root=tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# create text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica,",18)
)

text.pack(expand=True,fill=tk.BOTH)

# Main Logic Start Now :

# Function 1- to create a new file

def new_file():
    text.delete(1.0,tk.END)
    
# Function 2 -to open a new file

def open_file():
    # open file dialogue
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetype=[("text Files","*.txt")]
    )
    
    if file_path:
        #open selected file
        with open(file_path,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())
            
# Function 3 - Save the File

def save_file():
    # open save file dialogue
    file_path = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]     
    )
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0,tk.END))
            
    messagebox.showinfo("Info", "FIle Saved Successfully")
    
# Creat Menu Bar:

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)

# New , Open, Save, Exit

# add filemenu to menu bar
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# starts and keps the window open
root.mainloop()
