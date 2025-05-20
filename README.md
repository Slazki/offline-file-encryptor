# Offline File Encryptor

A simple, offline file encryptor with both **CLI** and **GUI** frontends.  
Encrypt and decrypt files locally using AES‑GCM without ever touching the internet.

---

## Features

- **AES‑GCM** encryption for confidentiality ​& integrity  
- Two modes:
  - **CLI**: `encryptor.py`
  - **GUI**: `encryptor_gui.py` (Tkinter‑based desktop app)  
- Packaged as a single, double‑clickable Windows `.exe` via PyInstaller  

---

## Prerequisites for .py method

- **Python 3.7+**  
- **pip** (comes with Python)  
- On Windows, **Tkinter** is bundled with most Python installers


---

## How to use the actual app

1. **Select File**  
- Click the **Select File** button.  
- In the dialog, choose the file you want to encrypt (`.txt`, `.pdf`, etc.) or decrypt (`.enc`).  
- The filename appears next to the button.

2. **Enter Password**  
- Type the passphrase you will use to lock or unlck the file.  
- Make sure to remember it without it, you can’t decrypt your data!

3. **Encrypt or Decrypt**  
- **Encrypt**:  
  - Click **Encrypt**.  
  - In the save dialog, pick a name (default extension `.enc`).  
  - Click **Save**.
  - Once encryption is complete, you can safely delete the original file and its contents are preserved in the encrypted copy and can be decrypted whenever you need it
  - A popup will confirm “Encrypted → `<your‑filename>.enc`”.

- **Decrypt**:  
  - Click **Decrypt**.  
  - In the save dialog, pick a name (default extension `.dec` or original).  
  - Click **Save**.  
  - A popup will confirm “Decrypted → `<your‑filename>.dec`”.

4. **Success!**  
- Your encrypted files end in `.enc`.  
- Your decrypted files end in `.dec` (or whatever name you chose).  

---

### Tips

- Use a **strong, memorable** password (at least 8 characters, mix of letters/numbers/symbols).  
- Keep backups if you lose your password, your data is irrecoverable.

Thanks for reading and using it.


MIT License

Copyright (c) 2025 Fahad Majidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights   
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.                                

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

