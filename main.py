import tkinter as tk
import pyperclip
import gen
import os

root = tk.Tk()

password_len_tkvar = tk.IntVar()
has_lower_value = tk.BooleanVar()
has_upper_value = tk.BooleanVar()
has_special_value = tk.BooleanVar()


def file_check_lines():
    with open("pwd_vault.txt", 'r') as f:
        count = len(f.readlines())
    return count


def check_vault():
    pwd_vault = "pwd_vault.txt"
    if os.path.isfile(pwd_vault):
        # print(f'found {pwd_vault} at {os.path.dirname(__file__)} and it is {check_vault()}')
        print(f"Found {pwd_vault} at {os.path.dirname(os.path.abspath(pwd_vault))} and it is {file_check_lines()}")
    else:
        with open("pwd_vault.txt", 'x') as f:
            pass
        print("not found")
    """todo: make this a encrypted mysql or other sql base"""


def call_password():
    password = gen.get_password(8, has_lower=has_lower_value.get(),
                                has_upper=has_upper_value.get(), has_special=has_special_value.get())

    password_label = tk.Label(text=password, padx=5, pady=5, cursor='xterm')
    password_label.grid(row=4, column=0)

    copy_button = tk.Button(text="copy", command=pyperclip.copy(password))
    copy_button.grid(row=4, column=1)


def get_password_len():
    # print(password_len_tkvar.get())
    return int(password_len_tkvar.get())


check_vault()

menubar = tk.Menu(root)
file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

welcome = tk.Label(root, text="Simple Password Generator")
welcome.grid(row=0, column=0, columnspan=2)

gen_button = tk.Button(text="generate", padx=40, pady=20, command=lambda: call_password())
gen_button.grid(row=1, column=0, columnspan=1, rowspan=3)

has_lower_box = tk.Checkbutton(root, text="lower chars", variable=has_lower_value)
has_lower_box.grid(row=1, column=1)

has_upper_box = tk.Checkbutton(root, text="upper chars", variable=has_upper_value)
has_upper_box.grid(row=2, column=1)

has_upper_box = tk.Checkbutton(root, text="special chars", variable=has_special_value)
has_upper_box.grid(row=3, column=1)

get_password_len_box = tk.Entry(root, text="length", textvariable=password_len_tkvar)
get_password_len_box.grid(row=1, column=3)

get_password_len_button = tk.Button(root, text="get", command=get_password_len)
get_password_len_button.grid(row=1, column=4)

root.config(menu=menubar)
root.mainloop()
