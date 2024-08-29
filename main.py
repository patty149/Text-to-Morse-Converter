from tkinter import *
from tkinter import messagebox, filedialog

app_window = Tk()

from_lang_var = StringVar(app_window)
to_lang_var = StringVar(app_window)

from_lang_var.set("Eng")
to_lang_var.set("Morse")

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def clear_all():
    input_text.delete(1.0, END)
    output_text.delete(1.0, END)


def convert_text():
    message = input_text.get("1.0", "end")[:-1]

    if from_lang_var.get() == to_lang_var.get():
        messagebox.showerror("Error", "Can't be the same language")
        return

    if from_lang_var.get() == "Eng" and to_lang_var.get() == "Morse":
        result = encrypt(message)
    elif from_lang_var.get() == "Morse" and to_lang_var.get() == "Eng":
        result = decrypt(message)
    else:
        messagebox.showerror("Error", "Please choose a valid language code.")
        return

    output_text.insert('end -1 chars', result)


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT.get(letter.upper(), '') + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher


def save_translation():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(output_text.get(1.0, END))


def load_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            input_text.delete(1.0, END)
            input_text.insert(END, text)
            convert_text()


def copy_to_clipboard():
    app_window.clipboard_clear()
    app_window.clipboard_append(output_text.get(1.0, END))
    messagebox.showinfo("Copied", "Text copied to clipboard")


if __name__ == "__main__":
    app_window.configure(background='#E3F2FD')
    app_window.geometry("800x600")
    app_window.title("Morse Code Translator")

    header_frame = Frame(app_window, bg='#0D47A1', pady=10)
    header_frame.pack(fill='x')

    header_label = Label(header_frame, text='Morse Code Translator', fg='white', bg='#0D47A1',
                         font=('Helvetica', 18, 'bold'))
    header_label.pack()

    content_frame = Frame(app_window, bg='#E3F2FD', padx=20, pady=20)
    content_frame.pack(expand=True, fill='both')

    input_label = Label(content_frame, text="Enter Text", fg='#0D47A1', bg='#E3F2FD', font=('Helvetica', 12))
    input_label.grid(row=0, column=0, pady=10, sticky='e')

    from_lang_label = Label(content_frame, text="From Language", fg='#0D47A1', bg='#E3F2FD', font=('Helvetica', 12))
    from_lang_label.grid(row=1, column=0, pady=10, sticky='e')

    to_lang_label = Label(content_frame, text="To Language", fg='#0D47A1', bg='#E3F2FD', font=('Helvetica', 12))
    to_lang_label.grid(row=2, column=0, pady=10, sticky='e')

    output_label = Label(content_frame, text="Converted Text", fg='#0D47A1', bg='#E3F2FD', font=('Helvetica', 12))
    output_label.grid(row=4, column=0, pady=10, sticky='e')

    input_text = Text(content_frame, height=5, width=50, font="Helvetica 13")
    input_text.grid(row=0, column=1, pady=10, padx=20)

    from_lang_menu = OptionMenu(content_frame, from_lang_var, "Eng", "Morse")
    from_lang_menu.config(bg='#BBDEFB', fg='#0D47A1', font=('Helvetica', 12))
    from_lang_menu.grid(row=1, column=1, pady=10, padx=20)

    to_lang_menu = OptionMenu(content_frame, to_lang_var, "Eng", "Morse")
    to_lang_menu.config(bg='#BBDEFB', fg='#0D47A1', font=('Helvetica', 12))
    to_lang_menu.grid(row=2, column=1, pady=10, padx=20)

    output_text = Text(content_frame, height=5, width=50, font="Helvetica 13")
    output_text.grid(row=4, column=1, pady=10, padx=20)

    button_frame = Frame(content_frame, bg='#E3F2FD')
    button_frame.grid(row=5, column=1, pady=20)

    convert_button = Button(button_frame, text="Convert", bg="#1976D2", fg="white", font=('Helvetica', 12, 'bold'),
                            command=convert_text)
    convert_button.grid(row=0, column=0, padx=10)

    clear_button = Button(button_frame, text="Clear", bg="#1976D2", fg="white", font=('Helvetica', 12, 'bold'),
                          command=clear_all)
    clear_button.grid(row=0, column=1, padx=10)

    save_button = Button(button_frame, text="Save", bg="#1976D2", fg="white", font=('Helvetica', 12, 'bold'),
                         command=save_translation)
    save_button.grid(row=0, column=2, padx=10)

    load_button = Button(button_frame, text="Load", bg="#1976D2", fg="white", font=('Helvetica', 12, 'bold'),
                         command=load_text)
    load_button.grid(row=0, column=3, padx=10)

    copy_button = Button(button_frame, text="Copy", bg="#1976D2", fg="white", font=('Helvetica', 12, 'bold'),
                         command=copy_to_clipboard)
    copy_button.grid(row=0, column=4, padx=10)

    app_window.mainloop()
