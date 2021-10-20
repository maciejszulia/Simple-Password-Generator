import tkinter as tk
from tkinter import ttk
import random
import pyperclip
import string
import gen

root = tk.Tk()

password_len = tk.IntVar()
has_lower_value = tk.BooleanVar()
has_upper_value = tk.BooleanVar()
has_special_value = tk.BooleanVar()


def call_password(password_len=8, has_lower=True, has_upper=False, has_special=False):
    password = gen.get_password(8, has_lower=has_lower_value.get(),
                                has_upper=has_upper_value.get(), has_special=has_special_value.get())

    password_label = tk.Label(text=password, padx=5, pady=5, cursor='xterm')
    password_label.grid(row=2, column=0)

    copy_button = tk.Button(text="copy", command=pyperclip.copy(password))
    copy_button.grid(row=2, column=1)
    print(has_upper_value.get())


has_lower_box = tk.Checkbutton(root, text="lower chars", variable=has_lower_value)
has_lower_box.grid(row=0, column=1)

has_upper_box = tk.Checkbutton(root, text="upper chars", variable=has_upper_value)
has_upper_box.grid(row=1, column=1)

gen_button = tk.Button(text="generate", padx=40, pady=20, command=lambda: call_password())
gen_button.grid(row=0, column=0, columnspan=1, rowspan=2)

root.mainloop()
print(has_upper_value.get())
# while True:
#     print(tickbox)
