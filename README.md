# Simple-Password-Generator

A password generator in Python with a Tkinter GUI.

A small project of my own from my Computer Science studies at UWM (2020–2024). I wrote the code by hand; the commit history is unchanged. This README was added in November 2026.

Years of work: 2021–2023 (first commit on 17 October 2021, last commit on 8 February 2023).

## Contents

- `gen.py`: `get_password`, which builds a password of a given length from digits and, on request, lower-case, upper-case and special characters.
- `main.py`: the Tkinter window; it copies the password with `pyperclip`.
- `check_vault.py`, `file_check_lines.py`: helpers for a password file.
- `setup.txt`: the dependencies (`tk`, `pyperclip`).

## Running

```
python3 -c "import gen; print(gen.get_password(12))"
```

Result on 26 November 2026 (Python 3.14): 2 random passwords; `gen.py` prints the first one when it is imported, and the second one has 12 characters. The window in `main.py` needs Tk, which this machine does not have.

## Original note

# Simple-Password-Generator

Just a project that I took on few years ago. Thought that it might be a good idea to develop it.

To install python depencies: <br>
`$ pip install -r setup.txt`

## Po polsku

Repozytorium zawiera mój własny generator haseł w Pythonie z interfejsem Tkinter. Kod napisałem ręcznie w latach 2021–2023.
