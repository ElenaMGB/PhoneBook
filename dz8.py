# ДЗ Телефонный справочник
# Домашнее задание

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
# 7-9 пунктов (сохранить, открыть, добавить, удалить, найти)

# сделать поиск по имени и по телефону вне зависимости от регистра

import tkinter as tk
from tkinter import messagebox, filedialog
# import json

class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Телефонный справочник")

        self.phonebook = {}

        # Входные поля
        self.family_label = tk.Label(root, text="Фамилия")
        self.family_label.grid(row=0, column=0)
        self.family_entry = tk.Entry(root)
        self.family_entry.grid(row=0, column=1)

        self.name_label = tk.Label(root, text="Имя")
        self.name_label.grid(row=0, column=2)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=3)

        self.phone_label = tk.Label(root, text="Телефон")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)
        
        self.about_label = tk.Label(root, text="Описание")
        self.about_label.grid(row=1, column=2)
        self.about_entry = tk.Entry(root)
        self.about_entry.grid(row=1, column=3)

        # Кнопки
        self.add_button = tk.Button(root, text="Добавить", command=self.add_contact)
        self.add_button.grid(row=5, column=0)

        self.delete_button = tk.Button(root, text="Удалить", command=self.delete_contact)
        self.delete_button.grid(row=5, column=2)

        self.update_button = tk.Button(root, text="Обновить", command=self.update_contact)
        self.update_button.grid(row=5, column=1)

        self.search_button = tk.Button(root, text="Поиск", command=self.search_contact)
        self.search_button.grid(row=3, column=2)

        self.display_button = tk.Button(root, text="Показать все", command=self.display_contacts)
        self.display_button.grid(row=3, column=0)

        self.clear_button = tk.Button(root, text="Очистить поля", command=self.clear_entries)
        self.clear_button.grid(row=3, column=1)

        self.save_button = tk.Button(root, text="Сохранить", command=self.save_phonebook)
        self.save_button.grid(row=7, column=2)

        self.load_button = tk.Button(root, text="Загрузить", command=self.load_phonebook)
        self.load_button.grid(row=7, column=0)

        self.exit_button = tk.Button(root, text="Выход", command=root.quit)
        self.exit_button.grid(row=10, column=0, columnspan=2)

        # Поле для отображения телефонного справочника
        self.contacts_text = tk.Text(root, height=10, width=50)
        self.contacts_text.grid(row=9, column=1, columnspan=2)

    def add_contact(self):
        family = self.family_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        about = self.about_entry.get()
        if family and phone:
            self.phonebook[family] = {"phone": phone, "name": name, "about": about}
            messagebox.showinfo("Готово", "Контакт добавлен")
            self.clear_entries()
        else:
            messagebox.showerror("Ошибка", "Заполните обязательные поля (фамилия и телефон)")


    def delete_contact(self):
        family = self.family_entry.get()
        if family in self.phonebook:
            del self.phonebook[family]
            messagebox.showinfo("Готово", "Контакт удален")
            self.clear_entries()
        else:
            messagebox.showerror("Ошибка", "Контакт не найден")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        family = self.family_entry.get()
        about = self.about_entry.get()
        if family in self.phonebook:
            self.phonebook[family] = {"phone": phone, "name": name, "about": about}
            messagebox.showinfo("Готово", "Контакт обновлен")
            self.clear_entries()            
        else:
            messagebox.showerror("Ошибка", "Контакт не найден")

    def search_contact(self):
        family = self.family_entry.get()
        if family in self.phonebook:
            self.contacts_text.delete(1.0, tk.END)
            self.contacts_text.insert(tk.END, f"{family}: {self.phonebook[family]}\n")
        else:
            messagebox.showerror("Ошибка", "Контакт не найден")

    def display_contacts(self):
        self.contacts_text.delete(1.0, tk.END)
        for family, details in self.phonebook.items():
            phone = details.get("phone", "")
            name = details.get("name", "")
            about = details.get("about", "")
            # self.contacts_text.insert(tk.END, f"{name}: {phone}, {family}, {about}\n")
            self.contacts_text.insert(tk.END, f"{phone}: {family} {name}, {about}\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.family_entry.delete(0, tk.END)
        self.about_entry.delete(0, tk.END)


    def save_phonebook(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                for family, details in self.phonebook.items():
                    name = details['name']
                    phone = details['phone']
                    about = details['about']
                    f.write(f"Family: {family}, Name: {name}, Phone: {phone},  About: {about}\n")
            messagebox.showinfo("Готово", "Телефонный справочник сохранен в txt файле")

    def load_phonebook(self):
        filepath = filedialog.askopenfilename(defaultextension=".txt")
        if filepath:
            self.phonebook = {}
            with open(filepath, 'r') as f:
                for line in f:
                    if line.strip():  # Пропускаем пустые строки
                        data = line.strip().split(', ')
                        family = data[0].split(': ')[1]
                        name = data[1].split(': ')[1]
                        phone = data[2].split(': ')[1]                        
                        about = data[3].split(': ')[1]
                        self.phonebook[family] = {"name": name,"phone": phone,  "about": about}
            messagebox.showinfo("Готово", "Телефонный справочник загружен")
            self.display_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
