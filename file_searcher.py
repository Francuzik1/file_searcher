import tkinter as tk
from threading import Timer
from tkinter import *
from tkinter import ttk
import os


def new_iteration(event):
    global catalog
    x = list_var.curselection()[0]
    for dirs, folder, files in os.walk(catalog):
        work_dirs = dirs
        work_folder = folder
        work_files = files
        break
    if list_var.get(x) not in work_files:
        if catalog[-1] != "\\":
            catalog = catalog + "\\" + list_var.get(x)
        else:
            catalog = catalog + list_var.get(x)
        for dirs, folder, files in os.walk(catalog):
            work_dirs = dirs
            work_folder = folder
            work_files = files
            break
        label["text"] = ("Текущая папка: " + work_dirs)
        list_var.delete(0, END)
        for new_files in work_files:
            list_var.insert(tk.END, new_files)
        for new_folders in work_folder:
            list_var.insert(tk.END, new_folders)
    else:
        open_file()


def backer():
    global catalog
    catalog = os.path.dirname(catalog)
    for dirs, folder, files in os.walk(catalog):
        work_dirs = dirs
        work_folder = folder
        work_files = files
        break
    label["text"] = ("Текущая папка: " + work_dirs)
    list_var.delete(0, END)
    for new_files in work_files:
        list_var.insert(tk.END, new_files)
    for new_folders in work_folder:
        list_var.insert(tk.END, new_folders)


def open_file():
    error_time = Label(text="Функция в стадии разработки")
    error_time.pack()

    def kill_error_time():
        error_time.destroy()

    t = Timer(2, kill_error_time)
    t.start()


win = Tk()
geo = win.geometry
geo("400x400")
win.title("Searcher")
catalog = os.getcwd()
list_var = tk.Listbox(win)
list_var.pack()
for dirs, folder, files in os.walk(catalog):
    work_dirs = dirs
    work_folder = folder
    work_files = files
    break
for new_files in work_files:
    list_var.insert(tk.END, new_files)
for new_folders in work_folder:
    list_var.insert(tk.END, new_folders)
list_var.bind("<<ListboxSelect>>", new_iteration)
label = Label(text="Текущая папка: " + work_dirs)
btn_1 = ttk.Button(text="<---", command=backer)
label.pack()
btn_1.pack()
win.mainloop()
