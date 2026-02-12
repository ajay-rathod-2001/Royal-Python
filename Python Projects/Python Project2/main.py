import tkinter as tk
import time 
from PIL import Image,ImageTk

# Main window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of Image Paths:
image_paths=[
    r"C:\Users\ajayr\OneDrive\画像\画像\d.jpg",
    r"C:\Users\ajayr\OneDrive\画像\画像\d2.jpg",
    r"C:\Users\ajayr\OneDrive\画像\画像\d3.jpg",
    r"C:\Users\ajayr\OneDrive\画像\画像\d4.jpg",
    r"C:\Users\ajayr\OneDrive\画像\画像\d5.jpg",
    
]

image_size=(700,700)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)  # Adding each image int he list
    
# Convert PIL images into Tikinter compatible images
final_images= []
for img in images:
    photo = ImageTk.PhotoImage(img)  # Converting PIL image to Tkinter compatible image
    final_images.append(photo)
    
# Label Widget to Keep Photos:

image_label = tk.Label(root)
image_label.pack(pady=30)

#SlideShow Functions:

def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)
        
# Button
play_button =tk.Button(
    root,
    text="Play the Slideshow",
    font=("Arial",17),
    command=start_slideshow
    
) 

play_button.pack(pady=40)

root.mainloop()
    