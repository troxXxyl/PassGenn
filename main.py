import tkinter as tk
from tkinter import *
from tkinter import ttk
import string
import random

#Генератор сложных паролей!!!!!!!


def PassGen():
    lenght = int(pas_len.get())
    for i in range(lenght):
        character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for j in range(lenght))
    Fin_pas.delete(0.0, END)
    Fin_pas.insert(0.0, password)
    print(password)

#Окно программы
window = Tk()
window.title("PassGen")
window.geometry("400x200")

#Окно ввода длины пароля
pas_len = ttk.Entry()
pas_len.pack(pady=25)

#Кнопка для запуска функции
btn = ttk.Button(text = "Сгенерировать пароль", command=PassGen)
btn.pack(pady = 1)

#Готовый пароль
Fin_pas = Text()
Fin_pas.pack()

window.mainloop()