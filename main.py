import tkinter as tk
import random
import pyperclip
import string
import gen

root = tk.Tk()
print(string.ascii_lowercase)
print(string.ascii_uppercase)
i=0
while i < 10:
    cases = []
    cases.append(str(i))
    i+=1
print(str(cases))



def get_password():
    password_lenght: int = 10
    password: str = ""

    for i in range(password_lenght):
        password += str(random.randint(0, 9))
        i += 1

    print_password_in_label = tk.Label(root, text=password)
    copy_button = tk.Button(root, text="copy", command=pyperclip.copy(password))
    print_password_in_label.grid(column=0, row=1)
    copy_button.grid(column=1, row=1)


generate_button = tk.Button(root, text="Generate", padx=40, pady=10, command=gen.get_password)
generate_button.grid(column=0, row=0)

root.mainloop()
