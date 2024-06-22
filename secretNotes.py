from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64

window = Tk()
window.title("Secret Notes")
window.minsize(width=400,height=650)
window.config(pady=20)

userMasterKeyFirst = None
userMasterKeyLast = None

def userNote_encrypted():
    userTitle = entryTitle.get()
    userText = secretText.get("1.0",END)
    global userMasterKeyFirst
    userMasterKeyFirst = masterKeyEntry.get()
    # Base64 and b64encode function takes bytes as an argument
    encoded_data = base64.b64encode(bytes(userText, "utf-8")).decode("utf-8")
    # Convert your encryption from bytes to string
    # base64_str = encoded_data.decode("utf-8")
    # print(encoded_data)
    # print(base64_str)
    creating_file(userTitle,encoded_data)
    entryTitle.delete(0,END)
    secretText.delete("1.0", END)
    masterKeyEntry.delete(0,END)

def userNote_decrypted():
    global userMasterKeyLast
    userMasterKeyLast = masterKeyEntry.get()
    if userMasterKeyFirst == userMasterKeyLast:
        encrypted_b64data = secretText.get("1.0",END)
        decrypted_data = base64.b64decode(encrypted_b64data).decode()
        secretText.delete("1.0",END)
        entryTitle.delete(0,END)
        masterKeyEntry.delete(0,END)
        #secretText.insert("1.0",decrypted_data)
        save_decrypted_data(decrypted_data)
        messagebox.showinfo("Decrypted","Process has done\nLook at your file!")
    else:
        messagebox.showwarning("Warning", "Master key is not true!")
        secretText.delete("2.0", END)
        masterKeyEntry.delete(0, END)
        #error_msg_box = Message(text="the master key that you given is not true!\nProcess has failed.")
        #error_msg_box.pack()
def creating_file(userTitle,userEncryptedNote):
    with open("secretNote.txt",mode="w") as f:
        f.write(userTitle)
    with open("secretNote.txt",mode="a") as f:
        f.write(f"\nEncrypted data: {userEncryptedNote}")

def save_decrypted_data(decrypted_data):
    with open("secretNote.txt",mode="a") as f:
        f.write(f"\nDecrypted data: {decrypted_data}")

secretImage = Image.open("SecretNotes.png")
secretImage = ImageTk.PhotoImage(secretImage)

imageLabel = Label(window,image=secretImage,pady=80,width=76,height=76)
imageLabel.pack()

FONT = ("Arial",12, "normal")
titleLabel = Label(text="Enter your title",font=FONT,pady=8)
titleLabel.pack()

entryTitle = Entry(width=40)
entryTitle.pack()

secretLabel = Label(text="Enter your secret", font=FONT, pady=8)
secretLabel.pack()

secretText = Text(width=40, height= 20)
secretText.pack()

masterKeyLabel = Label(text="Enter your master key", font=FONT,pady=8)
masterKeyLabel.pack()

masterKeyEntry = Entry(width=40)
masterKeyEntry.pack()

encryptButton = Button(text="Save & Encrypt", width=14,height=1,command=userNote_encrypted)
encryptButton.pack()

decryptButton = Button(text="Decrypt",command=userNote_decrypted)
decryptButton.pack()

window.mainloop()