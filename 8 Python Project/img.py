from fileinput import filename
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageEnhance, ImageTk,ImageDraw
from PIL import Image
root = tk.Tk()
root.geometry("600x400") 
root.title("Image Processing")
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(root, text='Upload Images', width=45, font=my_font1)
l1.grid(row=1, column=1, columnspan=4)
b1 = tk.Button(root, text='Click here to Upload',width=30, command=lambda: upload_file())
b1.grid(row=2, column=1, columnspan=10)

def upload_file():
    global image
    f_types = [('JPG Files', '*.jpg'),('JPEG Files', '*.jpeg'),('WebP Files', '*..webp'),('PNG Files', '*.png'), ("all files", ".")]
    filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)    
    for f in filename:  
       while TRUE:
            print("1.  Open Image")
            print("2.  Convert to PNG")
            print("3.  Resize Image")
            print("4.  Keep Aspect ratio as it is")
            print("5.  Crop Image")
            print("6.  Paste Image")
            print("7.  Rotate Image")
            print("8.  Flipped Image")
            print("9.  Change into Grayscale")
            print("10. Change contrast of Image")
            print("11. Circular Image")
            print("12. Circular Edge")
            print("13. Exit")
            choice = int(input("Enter above choice to perform operations on image : "))
            if(choice == 1):
                image = Image.open(f)
                image.show()
            elif(choice == 2):
                image = Image.open(f)
                image.save(r"typechanged.png")
            elif(choice == 3):
                image = Image.open(f)
                a = int(input("Enter height:"))
                b = int(input("Enter width:"))
                new_image = image.resize((a, b))
                new_image.save('resized.jpg')
            elif(choice == 4):
                image = Image.open(f)
                image.thumbnail((400, 400))
                image.save('keepasit.jpg')
            elif(choice == 5):
                image = Image.open(f)
                box = (400, 400, 800, 600)
                cropped_image = image.crop(box)
                cropped_image.save('crop.jpg')
                image = Image.open(f)
            elif(choice == 6):
                logo = Image.open(r"C:\Users\Chaitanya\Videos\Tasks\dyp.png")
                image_copy = image.copy()
                position = ((image_copy.width - logo.width),(image_copy.height - logo.height))
                image_copy.paste(logo, position)
                image_copy.save('pasted_img.jpg')
            elif(choice == 7):
                image = Image.open(f)
                c = int(input("Enter the degree in which we have to rotate the image:"))
                image_rot_ = image.rotate(c)
                image_rot_.save('rotatedimage.jpg')
            elif(choice == 8):
                image = Image.open(f)
                image_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
                image_flip.save('flip_img.jpg')
            elif(choice == 9):
                image = Image.open(f)
                greyscale_image = image.convert('L')
                greyscale_image.save('greyscale.jpg')   
            elif(choice == 10):
                image = Image.open(f)
                contrast1 = ImageEnhance.Contrast(image)
                contrast1.enhance(1.5).save('contrast.jpg')
            elif(choice == 11):
                img=Image.open(f)
                npImage=np.array(img)
                h,w=img.size
                alpha = Image.new('L', img.size,0)
                draw = ImageDraw.Draw(alpha)
                draw.pieslice([0,0,h,w],0,360,fill=255)
                npAlpha=np.array(alpha)
                npImage=np.dstack((npImage,npAlpha))
                Image.fromarray(npImage).save('circular.png')
            elif(choice==12):
                def add_corners(im, rad):
                 circle = Image.new('L', (rad * 2, rad * 2), 0)
                 draw = ImageDraw.Draw(circle)
                 draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
                 alpha = Image.new('L', im.size, 255)
                 w, h = im.size
                 alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
                 alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
                 alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
                 alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
                 im.putalpha(alpha)
                 return im
                im = Image.open(f)
                im = add_corners(im, 100)
                im.save('EDGE.png')
            elif(choice==13):
                break
            else:
               print("Please enter the correct choice")
    img = ImageTk.PhotoImage(Image.open(filename))            
root.mainloop()  