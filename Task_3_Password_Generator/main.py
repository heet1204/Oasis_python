import customtkinter as ctk
import random
import string
import pyperclip


def generate_password():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        result_var.set("Select at least one character type!")
        return

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)


def copy_to_clipboard():
    password = result_var.get()
    pyperclip.copy(password)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Advanced Password Generator")
root.geometry("400x400")

length_var = ctk.StringVar(value="12")
uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
special_var = ctk.BooleanVar(value=True)
result_var = ctk.StringVar()

title_label = ctk.CTkLabel(root, text="Advanced Password Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

length_label = ctk.CTkLabel(root, text="Password Length:")
length_label.pack()
length_entry = ctk.CTkEntry(root, textvariable=length_var)
length_entry.pack()

uppercase_check = ctk.CTkCheckBox(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

lowercase_check = ctk.CTkCheckBox(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

numbers_check = ctk.CTkCheckBox(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

special_check = ctk.CTkCheckBox(root, text="Include Special Characters", variable=special_var)
special_check.pack()

generate_button = ctk.CTkButton(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_entry = ctk.CTkEntry(root, textvariable=result_var, state="readonly", width=300)
result_entry.pack(pady=10)

copy_button = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
