from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def create_file():
    file_name = "my_secret"
    one = sn_entry_1.get()
    two = sn_entry_2.get()
    three = sn_text.get("1.0",END)
    if len(one) == 0 or len(two) == 0 or len(three) == 0:
        messagebox.showerror("Hata", "Bilgiler eksik")
    else:
        try:
            with open(file_name, "w") as file:
                file.write("")
            messagebox.showinfo("Başarılı", f"{file_name} dosyası oluşturuldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya oluşturma sırasında bir hata oluştu: {str(e)}")
    message_encrypted = encode(sn_entry_2.get(), sn_text.get("1.0", "end-1c"))
    try:
        with open(file_name, mode="a") as myNewFile:
            myNewFile.write(sn_entry_1.get())  # Parantez ekleyerek sn_entry_1.get() fonksiyonunu çağırın
            myNewFile.write("\n")
            myNewFile.write(message_encrypted)  # Aynı şekilde sn_text.get() fonksiyonunu çağırın
    except FileNotFoundError:
        with open(file_name, "w") as myNewFile:
            myNewFile.write(sn_entry_1.get())  # Parantez ekleyerek sn_entry_1.get() fonksiyonunu çağırın
            myNewFile.write("\n")
            myNewFile.write(message_encrypted)  # Aynı şekilde sn_text.get() fonksiyonunu çağırın
    finally:
        sn_entry_1.delete(0, END)
        sn_entry_2.delete(0,END)
        sn_text.delete(1.0, END)

def decrypt_notes():
    message_encrypted = sn_text.get("1.0", END)
    master_secret = sn_entry_2.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            sn_text.delete("1.0", END)
            sn_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")


sn_window = Tk()
sn_window.title("secret notes with python")
sn_window.config(padx=20, pady=20)
#sn_window.minsize(width=150, height = 200)

"""
path = "img.png"
original_img = Image.open(path)
resized_img = original_img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(image = img)
img_label.pack(fill = "both", expand = "yes")
img_label.config(padx=50, pady=50)
------------------------------------
photo = PhotoImage(file = "img.png")
photo_label = Label(image=photo)
photo_label.pack()
"""

photo = PhotoImage(file = "img.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=photo )
canvas.pack()

sn_label_1 = Label(text ="enter your title")
sn_label_1.pack()

sn_entry_1 = Entry(width=25)
sn_entry_1.focus()
sn_entry_1.pack()

sn_label_2 = Label(text="enter your secret")
sn_label_2.pack()

sn_text = Text(width=25, height= 10)
sn_text.pack()

sn_label_3 = Label(text="enter master key")
sn_label_3.pack()

sn_entry_2 = Entry(width=25)
sn_entry_2.pack()

spacer1 = Label(text="")
spacer1.pack()

sn_button_1 = Button(text ="save & encrypt", command=create_file)
sn_button_1.config(width=15,height=1)
sn_button_1.pack()

spacer2 = Label(text="")
spacer2.config(padx=3,pady=0.5)
spacer2.pack()

sn_button_2 = Button(text ="decrypt",command=decrypt_notes)
sn_button_2.config(width=15,height=1)
sn_button_2.pack()

sn_window.mainloop()
