import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import shutil

what_copy = None
region = None
what_move = None
move_mode = False
map = None


def new_iteration(event):
    global catalog
    global work_files
    global work_folder
    global work_dirs
    global list_var
    w = list_var.curselection()
    y = None
    if len(w) > 0:
        y = list_var.curselection()[0]
    if y is not None:
        for dirs, folder, files in os.walk(catalog):
            work_dirs = dirs
            work_folder = folder
            work_files = files
            break
        if list_var.get(y) not in work_files:
            if catalog[-1] != "\\":
                catalog = catalog + "\\" + list_var.get(y)
            else:
                catalog = catalog + list_var.get(y)
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


def new_iteration_2(event):
    global catalog_2
    global work_files_2
    global work_folder_2
    global work_dirs_2
    global list_var_2
    g = list_var_2.curselection()
    x = None
    if len(g) > 0:
        x = list_var_2.curselection()[0]
    if x is not None:
        for dirs_2, folder_2, files_2 in os.walk(catalog_2):
            work_dirs_2 = dirs_2
            work_folder_2 = folder_2
            work_files_2 = files_2
            break
        if list_var_2.get(x) not in work_files_2:
            if catalog_2[-1] != "\\":
                catalog_2 = catalog_2 + "\\" + list_var_2.get(x)
            else:
                catalog_2 = catalog_2 + list_var_2.get(x)
            for dirs_2, folder_2, files_2 in os.walk(catalog_2):
                work_dirs_2 = dirs_2
                work_folder_2 = folder_2
                work_files_2 = files_2
                break
            label_2["text"] = ("Текущая папка: " + work_dirs_2)
            list_var_2.delete(0, END)
            for new_files_2 in work_files_2:
                list_var_2.insert(tk.END, new_files_2)
            for new_folders_2 in work_folder_2:
                list_var_2.insert(tk.END, new_folders_2)
        else:
            open_file()


def backer():
    global catalog
    global work_files
    global work_folder
    global work_dirs
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


def backer_2():
    global catalog_2
    global work_files_2
    global work_folder_2
    global work_dirs_2
    catalog_2 = os.path.dirname(catalog_2)
    for dirs_2, folder_2, files_2 in os.walk(catalog_2):
        work_dirs_2 = dirs_2
        work_folder_2 = folder_2
        work_files_2 = files_2
        break
    label_2["text"] = ("Текущая папка: " + work_dirs_2)
    list_var_2.delete(0, END)
    for new_files_2 in work_files_2:
        list_var_2.insert(tk.END, new_files_2)
    for new_folders_2 in work_folder_2:
        list_var_2.insert(tk.END, new_folders_2)


def open_file():
    z = None
    map = None
    if len(list_var_2.curselection()) > 0:
        x = list_var_2.curselection()[0]
        z = list_var_2.get(x)
        if catalog_2[-1] != "\\":
            map = catalog_2 + "\\" + z
        else:
            map = catalog_2 + z
    elif len(list_var.curselection()) > 0:
        y = list_var.curselection()[0]
        z = list_var.get(y)
        if catalog[-1] != "\\":
            map = catalog + "\\" + z
        else:
            map = catalog + z
    open_text = open(str(map), 'r')
    a = Toplevel()
    a.geometry('200x150')
    Label(a, text=open_text.read()).pack(expand=1)

    def kill_error():
        a.destroy()

    Button(a, text="OK", command=kill_error).pack(expand=2)


def info():
    win_info = Toplevel()
    win_info.geometry('200x150')
    Label(win_info, text="INFO").pack(expand=1)


def help():
    win_help = Toplevel()
    win_help.geometry('200x150')
    Label(win_help, text="HELP").pack(expand=1)


def popup(event):
    global work_dirs
    global catalog
    global region
    region = work_dirs
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


def popup_2(event):
    global work_dirs_2
    global region
    global catalog_2
    region = work_dirs_2
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


def copier():
    global catalog
    global catalog_2
    global what_copy
    global work_files_2
    global work_folder_2
    global work_dirs_2
    global work_files
    global work_folder
    global work_dirs
    g = list_var.curselection()
    z = list_var_2.curselection()
    x = None
    what_copy = None
    if len(g) > 0:
        x = list_var.curselection()[0]
        if catalog[-1] == "\\":
            what_copy = catalog + list_var.get(x)
        else:
            what_copy = catalog + "\\" + list_var.get(x)
    elif len(z) > 0:
        x = list_var_2.curselection()[0]
        what_copy = list_var_2.get(x)
        if catalog_2[-1] == "\\":
            what_copy = catalog_2 + list_var.get(x)
        else:
            what_copy = catalog_2 + "\\" + list_var_2.get(x)


def mover():
    global catalog
    global catalog_2
    global what_copy
    global work_files_2
    global work_folder_2
    global work_dirs_2
    global work_files
    global work_folder
    global work_dirs
    global what_move
    global move_mode
    what_copy = None
    what_move = None
    g = list_var.curselection()
    z = list_var_2.curselection()
    x = None
    if len(g) > 0:
        x = list_var.curselection()[0]
        if catalog[-1] == "\\":
            what_move = catalog + list_var.get(x)
        else:
            what_move = catalog + "\\" + list_var.get(x)
        move_mode = True
    elif len(z) > 0:
        x = list_var_2.curselection()[0]
        what_move = list_var_2.get(x)
        if catalog_2[-1] == "\\":
            what_move = catalog_2 + list_var.get(x)
        else:
            what_move = catalog_2 + "\\" + list_var_2.get(x)
        move_mode = True


def inserter():
    global what_copy
    global region
    global move_mode
    g = list_var.curselection()
    z = list_var_2.curselection()
    x = None
    where_insert = None
    if len(g) > 0:
        x = list_var.curselection()[0]
        if list_var.get(x) not in work_files:
            if catalog[-1] == "\\":
                where_insert = catalog + list_var.get(x)
            else:
                where_insert = catalog + "\\" + list_var.get(x)
        else:
            where_insert = None
    elif len(z) > 0:
        x = list_var_2.curselection()[0]
        if list_var_2.get(x) not in work_files_2:
            if catalog_2[-1] == "\\":
                where_insert = catalog_2 + list_var_2.get(x)
            else:
                where_insert = catalog_2 + "\\" + list_var_2.get(x)
        else:
            where_insert = None
    if what_copy is not None and where_insert is not None and move_mode is False:
        if what_copy == where_insert:
            where_insert = region
        print(str(what_copy), str(where_insert))
        print("copy")
        # shutil.copy(str(what_copy), str(where_insert))
    if what_move is not None and where_insert is not None and move_mode is True:
        if what_move == where_insert:
            where_insert = region
        print(str(what_move), str(where_insert))
        print("move")
        move_mode = False
        # shutil.move(what_move, where_insert)


def closer(event):
    win.destroy()


win = Tk()
geo = win.geometry
geo("400x400")
win.title("Searcher")
catalog = os.getcwd()
catalog_2 = os.getcwd()
list_var = tk.Listbox(win)
list_var.grid(column=1, row=0, padx=6, pady=6)
list_var_2 = tk.Listbox(win)
list_var_2.grid(column=4, row=0, padx=6, pady=6)
work_dirs = None
work_files = None
work_folder = None
work_dirs_2 = None
work_files_2 = None
work_folder_2 = None
for dirs, folder, files in os.walk(catalog):
    work_dirs = dirs
    work_folder = folder
    work_files = files
    break
for dirs_2, folder_2, files_2 in os.walk(catalog_2):
    work_dirs_2 = dirs_2
    work_folder_2 = folder_2
    work_files_2 = files_2
    break
for new_files in work_files:
    list_var.insert(tk.END, new_files)
for new_folders in work_folder:
    list_var.insert(tk.END, new_folders)
for new_files_2 in work_files_2:
    list_var_2.insert(tk.END, new_files_2)
for new_folders_2 in work_folder_2:
    list_var_2.insert(tk.END, new_folders_2)
#list_var.bind("<<ListboxSelect>>")
#list_var_2.bind("<<ListboxSelect>>")
list_var.bind("<Double-Button-1>", new_iteration)
list_var_2.bind("<Double-Button-1>", new_iteration_2)
label = Label(text="Текущая папка: " + work_dirs)
label_2 = Label(text="Текущая папка: " + work_dirs_2)
btn_1 = ttk.Button(text="<---", command=backer)
btn_2 = ttk.Button(text="<---", command=backer_2)
label.grid(column=1, row=7)
btn_1.grid(column=1, row=8)
label_2.grid(column=4, row=7)
btn_2.grid(column=4, row=8)
# menu_code
main_menu = Menu(win)
win.config(menu=main_menu)
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="Помощь", command=help)
help_menu.add_command(label="О программе", command=info)
main_menu.add_command(label='Выход', command=lambda: win.destroy())
main_menu.add_cascade(label="Справка", menu=help_menu)
# con_menu
list_var.bind("<Button-3>", popup)
list_var_2.bind("<Button-3>", popup_2)
menu = Menu(tearoff=0)
menu.add_command(label="Копировать", command=copier)
menu.add_command(label="Вставить", command=inserter)
menu.add_command(label="Переместить", command=mover)
# hot_key
win.bind('<Control-h>', closer)
win.mainloop()
