import tkinter as tk
import random
import pyperclip


def __main__():
    root = tk.Tk()

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

    generate_button = tk.Button(root, text="Generate", padx=40, pady=10, command=get_password)
    generate_button.grid(column=0, row=0)

    root.mainloop()


if __name__ == "__main__":
    __main__()
