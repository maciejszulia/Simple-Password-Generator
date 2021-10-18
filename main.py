import tkinter as tk
import random
import pyperclip
import string
import gen

root = tk.Tk()

global password
global tickbox
tickbox = tk.BooleanVar()


def call_password(password_len=8, has_lower=True, has_upper=True, has_special=False):
    password = gen.get_password(has_lower=tickbox)

    password_label = tk.Label(text=password, padx=5, pady=5, cursor='xterm')
    password_label.grid(row=1, column=0)

    copy_button = tk.Button(text="copy", command=pyperclip.copy(password))
    copy_button.grid(row=1, column=1)




has_lower_box = tk.Checkbutton(text="lower chars", variable=tickbox)
has_lower_box.grid(row=0, column=1)

gen_button = tk.Button(text="generate", padx=40, pady=20, command=lambda: call_password(has_lower=tickbox))
gen_button.grid(row=0, column=0, columnspan=1)

root.mainloop()

# while True:
#     print(tickbox)
