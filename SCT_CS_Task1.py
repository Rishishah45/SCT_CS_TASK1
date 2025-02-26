import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def encrypt_text():
    message = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text.set(caesar_cipher(message, shift, encrypt=True))

def decrypt_text():
    message = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text.set(caesar_cipher(message, shift, encrypt=False))

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x300")

tk.Label(root, text="Enter Message:").pack()
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Enter Shift Value:").pack()
entry_shift = tk.Entry(root, width=5)
entry_shift.pack()

encrypted_text = tk.StringVar()
decrypted_text = tk.StringVar()

tk.Button(root, text="Encrypt", command=encrypt_text).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_text).pack(pady=5)

tk.Label(root, text="Encrypted Message:").pack()
tk.Entry(root, textvariable=encrypted_text, state='readonly', width=40).pack()

tk.Label(root, text="Decrypted Message:").pack()
tk.Entry(root, textvariable=decrypted_text, state='readonly', width=40).pack()

root.mainloop()
