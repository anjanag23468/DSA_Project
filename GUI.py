import tkinter as tk
from compress_image import compress_image, img_size
from PIL import Image, ImageTk


root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Compression')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 60, window=label1)

label2 = tk.Label(root, text='Enter your file:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry2 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry2)

label3 = tk.Label(root, text='Enter new file name:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 180, window=label3)

entry3 = tk.Entry(root)
canvas1.create_window(200, 220, window=entry3)

label4 = tk.Label(root, text='Threshold:')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 260, window=label4)

entry4 = tk.Entry(root)
canvas1.create_window(200, 300, window=entry4)

label5 = tk.Label(root, text='', font=('helvetica', 10))
canvas1.create_window(200, 340, window=label5)

def buttonClickHandler():
    img_path = entry2.get()
    save_name = entry3.get()
    threshold = int(entry4.get())

    label5.configure(text='Preparing image. Please wait, this may take a while...')
    root.update()

    compress_image(img_path, save_name, threshold)

    canvas1.delete("all")

    basewidth = 500

    img1 = Image.open(img_path)
    wpercent = (basewidth/float(img1.size[0]))
    hsize = int((float(img1.size[1])*float(wpercent)))
    img1 = img1.resize((basewidth,hsize), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)

    frame1 = tk.Frame(canvas1)
    label6 = tk.Label(frame1, text=f'Original Image Size: {img_size(img_path)} KB', font=('helvetica', 10))
    label6.pack()
    label7 = tk.Label(frame1, image=img1)
    label7.image = img1
    label7.pack()
    frame1.pack(side='left')

    img2 = Image.open(save_name)
    img2 = img2.resize((basewidth,hsize), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    frame2 = tk.Frame(canvas1)
    label8 = tk.Label(frame2, text=f'Compressed Image Size: {img_size(save_name)} KB', font=('helvetica', 10))
    label8.pack()
    label9 = tk.Label(frame2, image=img2)
    label9.image = img2
    label9.pack()
    frame2.pack(side='left')

button1 = tk.Button(text='Compress Image', command=buttonClickHandler, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 380, window=button1)

root.mainloop()
