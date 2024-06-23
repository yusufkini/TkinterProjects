import hashlib
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import hashlib

window = Tk()
window.title("MD5 Hash Cracking")
window.minsize(width=400,height=400)
window.config(pady=30)

FONT = ("Arial",12,"bold")

def md5_decrypt():
    result_flag = False
    result_hash = None
    user_hash = md5_entry.get()
    file_name = fileName_entry.get()
    try:
        with open(file_name,mode="r") as f:
            lines = f.readlines()

            if len(user_hash) == 32 and type(user_hash) == str:

                for line_index in lines:
                    passwd = line_index.strip()
                    last_hash = hashlib.md5(passwd.encode('utf-8')).hexdigest()
                    if last_hash == user_hash:
                        result_hash = passwd
                        result_flag = True
                        md5_entry.delete(0, END)
                        fileName_entry.delete(0, END)
                        result_entry.delete(0, END)
                        break

                if result_flag == True:
                    messagebox.showinfo(title="Decrypted", message="Process has done!")
                    result_entry.insert(0, result_hash)
                else:
                    messagebox.showwarning(title="Failed", message="Process has failed!")
            else:
                messagebox.showwarning(title="Warning", message="Please enter md5 hash")
    except:
        messagebox.showwarning(title="Warning",message="Please enter a file with extension (.txt)")


md5Image = Image.open("password.png")
md5Image = ImageTk.PhotoImage(md5Image)

imageLabel = Label(window,image=md5Image,width=100,height=100)
imageLabel.pack()

textLabel = Label(text="Enter your hash as hexadecimal",font=FONT,pady=8)
textLabel.pack()

md5_entry = Entry(width=50,)
md5_entry.pack()

fileName_label = Label(text="Enter file name (password list)", font=FONT,pady=8)
fileName_label.pack()

fileName_entry = Entry(width=50)
fileName_entry.pack()

decrypt_button = Button(text="decrypt",width=10,height=2,command=md5_decrypt)
decrypt_button.place(x=160,y=230)

result_label = Label(text="Result", font=FONT)
result_label.place(x=200-27.5,y=280)
result_label.update()
print(result_label.winfo_width())
print(result_label.winfo_height())

result_entry = Entry(width=50)
result_entry.place(x=200-152,y=310)

window.mainloop()

