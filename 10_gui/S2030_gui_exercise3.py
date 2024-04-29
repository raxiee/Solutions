"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).


Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk

pady = 8
padx_labels = 25
padx_buttons = 10
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"

def empty_entry():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)

main_window = tk.Tk()
main_window.title("my first GUI")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=20, pady=pady)

frame_trees = tk.Frame(frame_1)
frame_trees.grid(row=0, column=0, padx=20)

frame_labels = tk.Frame(frame_1)
frame_labels.grid(row=1, column=0, padx=20)

frame_buttons = tk.Frame(frame_1)
frame_buttons.grid(row=2, column=0)

tree_1_scrollbar = tk.Scrollbar(frame_trees)
tree_1_scrollbar.grid(row=5, column=6, padx=20, pady=15, sticky="ns")
tree_1 = ttk.Treeview(frame_trees, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=15)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1["columns"] = ("Id", "Weight", "Destination")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("Id", anchor=tk.E, width=40)
tree_1.column("Weight", anchor=tk.W, width=80)
tree_1.column("Destination", anchor=tk.W, width=180)

tree_1.heading("Id", text="Id", anchor=tk.CENTER)
tree_1.heading("Weight", text="Weight", anchor=tk.CENTER)
tree_1.heading("Destination", text="Destination", anchor=tk.CENTER)

label_1 = tk.Label(frame_labels, text="Id")
label_1.grid(row=0, column=1, padx=padx_labels)

label_2 = tk.Label(frame_labels, text="Weight")
label_2.grid(row=0, column=2, padx=padx_labels)

label_3 = tk.Label(frame_labels, text="Destination")
label_3.grid(row=0, column=3, padx=padx_labels)

label_4 = tk.Label(frame_labels, text="Weather")
label_4.grid(row=0, column=4, padx=padx_labels)

entry_1 = tk.Entry(frame_labels, width=4)
entry_1.grid(row=1, column=1, pady=pady)
entry_1.insert(0, "")

entry_2 = tk.Entry(frame_labels, width=8)
entry_2.grid(row=1, column=2, pady=pady)
entry_2.insert(0, "")

entry_3 = tk.Entry(frame_labels, width=18)
entry_3.grid(row=1, column=3, pady=pady)
entry_3.insert(0, "")

entry_4 = tk.Entry(frame_labels, width=12)
entry_4.grid(row=1, column=4, pady=pady)
entry_4.insert(0, "")

button_1 = tk.Button(frame_buttons, text="Create")
button_1.grid(row=0, column=1, pady=pady, padx=padx_buttons)

button_2 = tk.Button(frame_buttons, text="Update")
button_2.grid(row=0, column=2, pady=pady, padx=padx_buttons)

button_3 = tk.Button(frame_buttons, text="Delete")
button_3.grid(row=0, column=3, pady=pady, padx=padx_buttons)

button_4 = tk.Button(frame_buttons, text="Clear Entry Boxes", command=empty_entry)
button_4.grid(row=0, column=4, pady=pady, padx=padx_buttons)

if __name__ == "__main__":
    main_window.mainloop()
