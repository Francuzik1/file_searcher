from threading import Timer
from tkinter import *
from tkinter import ttk
import os

catalog = os.getcwd()


def backer(open=None):
    global catalog
    if open == None:
        catalog = os.path.dirname(catalog)
        for dirs, folder, files in os.walk(catalog):
            work_dirs = dirs
            work_folder = folder
            work_files = files
            break
        label["text"] = ("Текущая папка: " + work_dirs +
                       "\n Вложенные папки: " + str(work_folder) +
                       "\n Вложенные файлы:" + str(work_files))
    else:
        if catalog[-1] == "\\":
            catalog = catalog + open
        else:
            catalog = catalog + "\\" + open
        for dirs, folder, files in os.walk(catalog):
            work_dirs = dirs
            work_folder = folder
            work_files = files
            break
        label["text"] = ("Текущая папка: " + work_dirs +
                       "\n Вложенные папки: " + str(work_folder) +
                       "\n Вложенные файлы:" + str(work_files))


def open_file():
    error_time = Label(text="Функция в стадии разработки")
    error_time.grid(row=5, column=2)

    def kill_error_time():
        error_time.destroy()

    t = Timer(2, kill_error_time)
    t.start()


def open_folder():
    for dirs, folder, files in os.walk(catalog):
        work_folder = folder
        break
    new_folder = search_folder.get()
    if new_folder in work_folder:
        backer(new_folder)
    else:
        error_folder = Label(text="Такой папки в данной папке нет !")
        error_folder.grid(row=5, column=2)

        def kill_error_folder_Label():
            error_folder.destroy()
        t = Timer(2, kill_error_folder_Label)
        t.start()


for dirs, folder, files in os.walk(catalog):
    work_dirs = dirs
    work_folder = folder
    work_files = files
    break
root = Tk()
root.title("Searcher")
root.geometry("1000x250")
label = Label(text="Текущая папка: " + work_dirs +
                   "\n Вложенные папки: " + str(work_folder) +
                   "\n Вложенные файлы:" + str(work_files))
btn_1 = ttk.Button(text="<---", command=backer)
btn_2 = ttk.Button(text="Открыть файл", command=open_file)
btn_3 = ttk.Button(text="Открыть папку", command=open_folder)
search_folder = ttk.Entry()
search_file = ttk.Entry()
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=3, column=1)
label.grid(row=2, column=2)
search_file.grid(row=2, column=1)
search_folder.grid(row=4, column=1)
root.mainloop()
