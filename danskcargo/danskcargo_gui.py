import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import danskcargo_data as dcd
import danskcargo_sql as dcsql

# region global constants
pady = 8
padx_labels = 25
padx_buttons = 10
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"
# endregion global constants

# region container functions
def empty_entry():
    print("Clear Entry Boxes was pressed")
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)
# endregion container functions

# region misc functions
def read_table(tree):
    count = 0
    for record in test_data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1

def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    id_entry.delete(0, tk.END)
    id_entry.insert(0, values[0])
    weight_entry.delete(0, tk.END)
    weight_entry.insert(0, values[1])
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, values[2])
# endregion misc functions

# region test data
test_data_list = []
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))
# endregion test data

# region common widgets
main_window = ThemedTk("scidblue")
main_window.title("AspIT S2: DanskCargo")
main_window.geometry("500x500")
# endregion common widgets


# region style
style = ttk.Style(main_window)
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])
print(style.theme_names())
# endregion style

# region container functions
frame_container = tk.LabelFrame(main_window, text="Container")
frame_container.grid(row=0, column=0, padx=20, pady=pady)

tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=20)

edit_frame_container = tk.Frame(frame_container)
edit_frame_container.grid(row=1, column=0, padx=20)

button_frame_container = tk.Frame(frame_container)
button_frame_container.grid(row=2, column=0)
# endregion container functions

tree_1_scrollbar = tk.Scrollbar(tree_frame_container)
tree_1_scrollbar.grid(row=5, column=6, padx=20, pady=15, sticky="ns")
tree_1 = ttk.Treeview(tree_frame_container, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
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

tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))


# region labels
id_label = tk.Label(edit_frame_container, text="Id")
id_label.grid(row=0, column=1, padx=padx_labels)

weight_label = tk.Label(edit_frame_container, text="Weight")
weight_label.grid(row=0, column=2, padx=padx_labels)

destination_label = tk.Label(edit_frame_container, text="Destination")
destination_label.grid(row=0, column=3, padx=padx_labels)

weather_label = tk.Label(edit_frame_container, text="Weather")
weather_label.grid(row=0, column=4, padx=padx_labels)
# endregion labels

# region entries
id_entry = tk.Entry(edit_frame_container, width=4)
id_entry.grid(row=1, column=1, pady=pady)
id_entry.insert(0, "")

weight_entry = tk.Entry(edit_frame_container, width=8)
weight_entry.grid(row=1, column=2, pady=pady)
weight_entry.insert(0, "")

destination_entry = tk.Entry(edit_frame_container, width=18)
destination_entry.grid(row=1, column=3, pady=pady)
destination_entry.insert(0, "")

weather_entry = tk.Entry(edit_frame_container, width=12)
weather_entry.grid(row=1, column=4, pady=pady)
weather_entry.insert(0, "")
# endregion entries

# region buttons
create_button = tk.Button(button_frame_container, text="Create")
create_button.grid(row=0, column=1, pady=pady, padx=padx_buttons)

update_button = tk.Button(button_frame_container, text="Update")
update_button.grid(row=0, column=2, pady=pady, padx=padx_buttons)

delete_button = tk.Button(button_frame_container, text="Delete")
delete_button.grid(row=0, column=3, pady=pady, padx=padx_buttons)

clear_button = tk.Button(button_frame_container, text="Clear Entry Boxes", command=empty_entry)
clear_button.grid(row=0, column=4, pady=pady, padx=padx_buttons)
# endregion buttons

# region main
read_table(tree_1)
# endregion main

if __name__ == "__main__":
    main_window.mainloop()
