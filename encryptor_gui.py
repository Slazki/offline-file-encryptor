#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Crypto helpers
def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=100_000)

def encrypt_data(data, password):
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(data)
    return salt + cipher.nonce + tag + ct

def decrypt_data(blob, password):
    salt, nonce, tag, ct = blob[:16], blob[16:32], blob[32:48], blob[48:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag)

# GUI App
class EncryptorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Offline File Encryptor")
        self.geometry("400x200")
        tk.Button(self, text="Select File", command=self.pick_file).pack(pady=5)
        self.file_label = tk.Label(self, text="No file selected")
        self.file_label.pack()
        tk.Label(self, text="Password:").pack(pady=(10,0))
        self.pw_entry = tk.Entry(self, show="*")
        self.pw_entry.pack()
        frame = tk.Frame(self); frame.pack(pady=10)
        tk.Button(frame, text="Encrypt", command=self.run_encrypt).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Decrypt", command=self.run_decrypt).grid(row=0, column=1, padx=5)

    def pick_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path = path
            self.file_label.config(text=path.split("\\")[-1])

    def run_encrypt(self):
        try:
            with open(self.file_path, "rb") as f: data = f.read()
            blob = encrypt_data(data, self.pw_entry.get())
            out = filedialog.asksaveasfilename(defaultextension=".enc")
            with open(out, "wb") as f: f.write(blob)
            messagebox.showinfo("Success", f"Encrypted → {out}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_decrypt(self):
        try:
            with open(self.file_path, "rb") as f: blob = f.read()
            data = decrypt_data(blob, self.pw_entry.get())
            out = filedialog.asksaveasfilename(defaultextension=".dec")
            with open(out, "wb") as f: f.write(data)
            messagebox.showinfo("Success", f"Decrypted → {out}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    EncryptorApp().mainloop()
