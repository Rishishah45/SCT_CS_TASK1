import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()

    # Checking conditions
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Score calculation
    score = sum([length, has_upper, has_lower, has_digit, has_special])

    # Assigning strength levels
    if score == 5:
        strength = "Strong 💪"
        color = "green"
    elif score >= 3:
        strength = "Moderate ⚠️"
        color = "orange"
    else:
        strength = "Weak ❌"
        color = "red"

    # Displaying result
    label_result.config(text=f"Strength: {strength}", fg=color)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12))
button.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

root.mainloop()
