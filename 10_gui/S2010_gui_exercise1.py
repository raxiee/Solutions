"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

pady = 8

main_window = tk.Tk()
main_window.title("my first GUI")

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=20, pady=pady)

label_2 = tk.Label(frame_1, text=" ")
label_2.grid(row=1, column=1, padx=30)

label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=2, column=1, padx=30)

entry_1 = tk.Entry(frame_1, width=4)
entry_1.grid(row=3, column=1, pady=pady)
entry_1.insert(0, "")

button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=4, column=1, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
