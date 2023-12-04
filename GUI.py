from tkinter import * 
from tkinter import messagebox, filedialog
from rsa import RSA, Private_key, Public_key

rsa = None
current_tab = None

parent = Tk()

menu = LabelFrame(parent)
menu.pack()

def show_frame(frame):
    global current_tab
    if current_tab:
        current_tab.pack_forget()
    current_tab = frame
    frame.pack()

def gen_key(private_key_text, public_key_text):
    global rsa 
    rsa = RSA()
    public_key_text.delete('1.0', END)
    private_key_text.delete('1.0', END)
    public_key_text.insert(INSERT, rsa.get_public_key_str())
    private_key_text.insert(INSERT, rsa.get_private_key_str())
    

def save_key_to_file():
    file_path = filedialog.askdirectory()
    with open(file_path + "/public_key.txt", "w") as f:
        if rsa : 
            f.write(rsa.get_public_key_str())
            
    with open(file_path + "/private_key.txt", "w") as f:
        if rsa : 
            f.write(rsa.get_private_key_str())

    msg = messagebox.showinfo("information", "success")

gen_key_frame = Frame(parent)
encrypt_frame = Frame(parent)
decrypt_frame = Frame(parent)
        
gen_key_tab_btn = Button(menu ,text= "generate key tab", command= lambda : show_frame(gen_key_frame), width= 15).grid(row = 0, column= 0)
encrypt_tab_btn = Button(menu ,text= "encrypt tab", command= lambda : show_frame(encrypt_frame), width= 15).grid(row = 0, column= 1)
decrypt_tab_btn = Button(menu ,text= "decrypt tab", command = lambda : show_frame(decrypt_frame), width= 15).grid(row = 0, column= 2)

#gen_key_frame 
public_key_text = Text(gen_key_frame, height= 10)
private_key_text = Text(gen_key_frame, height= 10)

gen_key_btn = Button(gen_key_frame, text = "gen key", command= lambda: gen_key(private_key_text, public_key_text)).pack()

public_key_label = Label(gen_key_frame, text = "public key").pack()
public_key_text.pack()
private_key_label = Label(gen_key_frame, text = "private key").pack()
private_key_text.pack()
save_file_btn = Button(gen_key_frame, text= "save to file", command= save_key_to_file).pack()

if not current_tab:
    gen_key_frame.pack()
#end gen_key_frame

# enter private key
def gen_decrypt_frame(parent):
    decrypt_frame = Frame(parent)
    enterkeey = Frame(decrypt_frame)
    enterkeey.pack()

    private_key = StringVar()
    private_label = Label(enterkeey, text="Private key:").grid(column = 0, row = 0, sticky= W)
    key = Entry(enterkeey, width=100)
    key.focus()

    key.grid(column=1, row=0, sticky=W)

    decode_frame = Frame(decrypt_frame)

    def handle_decode(private_key, res_text):
        filename = filedialog.askopenfilename()
        arr = private_key.split(',')
        with open(filename, "rb") as f:
            cipher = f.read()
            res = RSA.decrypt(cipher, Private_key(int(arr[0]), int(arr[1])))
            res_text.insert(INSERT, res)

    genetate_label = Label(decode_frame, text="Decryption")
    genetate_label.pack()

    res_text = Text(decode_frame, height=10)

    decode_button = Button(decode_frame, text="Choose file and decrypt", command=lambda : handle_decode(key.get(), res_text))
    decode_button.pack()

    Label(decode_frame, text="Result: ", justify="left").pack()

    res_text.pack()

    decode_frame.pack()
    return decrypt_frame

def gen_encrypt_frame(parent):
    decrypt_frame = Frame(parent)
    enterkeey = Frame(decrypt_frame)
    enterkeey.pack()

    private_key = StringVar()
    private_label = Label(enterkeey, text="Public key:").grid(column = 0, row = 0, sticky= W)
    key = Entry(enterkeey, width=100)
    key.focus()

    key.grid(column=1, row=0, sticky=W)

    decode_frame = Frame(decrypt_frame)

    def handle_encode(private_key, input_text):
        filepath = filedialog.askdirectory()
        arr = private_key.split(',')
        res = RSA.encrypt(input_text, Public_key(int(arr[0]), int(arr[1])))
        with open(filepath + '/encrypt.bin', 'wb') as f:
            f.write(res)

    genetate_label = Label(decode_frame, text="Encryption")
    genetate_label.pack()

    Label(decode_frame, text="plain text: ", justify="left").pack()
    text = Text(decode_frame, height=10)
    text.pack()

    res_text = Text(decode_frame, height=10)
    # res_text.configure(state = 'disable')

    decode_button = Button(decode_frame, text="Encrypt", command=lambda : handle_encode(key.get(), text.get('1.0', 'end')))
    decode_button.pack()

    # Label(decode_frame, text="Result: ", justify="left").pack()

    decode_frame.pack()
    return decrypt_frame

decrypt_frame = gen_decrypt_frame(parent)
encrypt_frame = gen_encrypt_frame(parent)

parent.mainloop()