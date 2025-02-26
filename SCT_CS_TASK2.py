import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption & Decryption")
        self.root.geometry("500x400")
        
        self.image_label = tk.Label(root, text="No image loaded", font=("Arial", 12))
        self.image_label.pack(pady=10)
        
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)
        
        self.key_label = tk.Label(root, text="Enter Encryption Key:")
        self.key_label.pack()
        
        self.key_entry = tk.Entry(root)
        self.key_entry.pack()
        
        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)
        
        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack(pady=5)
        
        self.image_path = ""
        self.encrypted_image_path = ""
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(self.image_path)
            img.thumbnail((250, 250))
            img_tk = ImageTk.PhotoImage(img)
            
            self.image_label.configure(image=img_tk, text="")
            self.image_label.image = img_tk
            messagebox.showinfo("Success", "Image Loaded Successfully!")
    
    def encrypt_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please load an image first!")
            return
        
        key = self.get_key()
        if key is None:
            return
        
        img = Image.open(self.image_path).convert("RGB")
        img_array = np.array(img)
        encrypted_array = img_array ^ key
        
        encrypted_img = Image.fromarray(encrypted_array)
        self.encrypted_image_path = os.path.join(os.path.dirname(self.image_path), "encrypted_img.png")
        encrypted_img.save(self.encrypted_image_path)
        
        messagebox.showinfo("Success", f"Image encrypted and saved at {self.encrypted_image_path}")
    
    def decrypt_image(self):
        if not self.encrypted_image_path:
            messagebox.showerror("Error", "No encrypted image found. Encrypt an image first!")
            return
        
        key = self.get_key()
        if key is None:
            return
        
        encrypted_img = Image.open(self.encrypted_image_path).convert("RGB")
        encrypted_array = np.array(encrypted_img)
        decrypted_array = encrypted_array ^ key
        
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_path = os.path.join(os.path.dirname(self.image_path), "decrypted_img.png")
        decrypted_img.save(decrypted_path)
        
        messagebox.showinfo("Success", f"Image decrypted and saved at {decrypted_path}")
    
    def get_key(self):
        try:
            return int(self.key_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric key!")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
