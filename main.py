from tkinter import *
from tkinter import ttk
from maindata import *
from tkinter import messagebox

window = Tk()
window.title("Travel Journal")
window.geometry("600x570")
window.resizable(width=False, height=False)

# design
header = Frame(window, width=600, height=50, bg="gold")
header.grid(row=0, column=0, padx=0, pady=1)

body = Frame(window, width=600, height=200, bg="white")
body.grid(row=1, column=0, padx=0, pady=1)

footer = Frame(window, width=600, height=150, bg="white", relief="flat")
footer.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky=NW)


# code

def display():
    global Structure

    listheader = ['Date', 'Start_Point', 'Destination', 'Distance_Covered', 'Best_Moments']

    demo_list = view()

    Structure = ttk.Treeview(footer, selectmode="extended", columns=listheader, show="headings")

    vscroll = ttk.Scrollbar(footer, orient="vertical", command=Structure.yview)
    hscroll = ttk.Scrollbar(footer, orient="horizontal", command=Structure.xview)

    Structure.configure(yscrollcommand=vscroll.set, xscrollcommand=hscroll.set)

    Structure.grid(column=0, row=0, sticky="nsew")
    vscroll.grid(column=1, row=0, sticky="ns")
    hscroll.grid(column=0, row=1, sticky="ew")

    Structure.heading(0, text="Date", anchor=NW)
    Structure.heading(1, text="Start Point", anchor=NW)
    Structure.heading(2, text="Destination", anchor=NW)
    Structure.heading(3, text="Distance Covered", anchor=NW)
    Structure.heading(4, text="Best Moments", anchor=NW)

    Structure.column(0, width=70, anchor="nw")
    Structure.column(1, width=100, anchor="nw")
    Structure.column(2, width=100, anchor="nw")
    Structure.column(3, width=100, anchor="nw")
    Structure.column(4, width=190, anchor="nw")

    for item in demo_list:
        Structure.insert('', 'end', values=item)


display()


def insert():
    Date = E_date.get()
    Source_Point = E_init.get()
    Destination = E_final.get()
    Distance_Covered = E_dist.get()
    Best_Moments = E_desc.get()

    data = [Date, Source_Point, Destination, Distance_Covered, Best_Moments]

    if Date == '' or Source_Point == '' or Destination == '' or Distance_Covered == '' or Best_Moments == '':
        messagebox.showwarning('Data', 'Please Fill all Fields')

    else:
        add(data)
        messagebox.showinfo('data', 'Data Added Successfully')
        E_date.delete(0, 'end')
        E_init.delete(0, 'end')
        E_final.delete(0, 'end')
        E_dist.delete(0, 'end')
        E_desc.delete(0, 'end')

        display()


def to_remove():
    try:
        structure_data = Structure.focus()
        structure_directory = Structure.item(structure_data)
        structure_list = structure_directory['values']
        structure_date = str(structure_list[0])

        remove(structure_date)

        messagebox.showinfo('Success', 'Data has been deleted Successfully')

        for widget in footer.winfo_children():
            widget.destroy()

        display()

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the Table')


def to_search():
    date = E_Search.get()
    data = search(date)

    def delete_command():
        Structure.delete(*Structure.get_children())

    delete_command()

    for item in data:
        Structure.insert('', 'end', values=item)


# widgets
title = Label(header, text="Travel Journal", height=1, font='Chiller 30 bold', bg="Gold", fg="black")
title.place(x=210, y=1)

date = Label(body, text="Date:", width=20, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
date.place(x=10, y=20)

# date
date = Label(body, text="Date:", width=30, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
date.place(x=10, y=20)
E_date = Entry(body, width=25, justify="left")
E_date.place(x=130, y=20)

# start_point
init = Label(body, text="Start Point :", width=30, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
init.place(x=10, y=50)
E_init = Entry(body, width=25, justify="left")
E_init.place(x=130, y=50)

# destination
final = Label(body, text="Destination:", width=30, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
final.place(x=10, y=80)
E_final = Entry(body, width=25, justify="left")
E_final.place(x=130, y=80)

# Distance_covered
dist = Label(body, text="Distance Covered:", width=30, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
dist.place(x=10, y=110)
E_dist = Entry(body, width=25, justify="left")
E_dist.place(x=130, y=110)

# Best Moments
desc = Label(body, text="Best Moments:", width=30, height=1, font='Ivy 10 bold', bg="white", anchor=NW)
desc.place(x=10, y=140)
E_desc = Entry(body, width=70, justify="left")
E_desc.place(x=130, y=140)

# Search
B_Search = Button(body, text="Search", height=1, font="Ivy 8 bold", command=to_search)
B_Search.place(x=345, y=20)
E_Search = Entry(body, width=25, justify="left", highlightthickness=1, relief="solid")
E_Search.place(x=400, y=20)

# view
B_view = Button(body, text="View", width=10, height=1, font="Ivy 8 bold", command=display)
B_view.place(x=345, y=50)

# Add
B_add = Button(body, text="Add", width=10, height=1, font="Ivy 8 bold", command=insert)
B_add.place(x=475, y=50)

# delete
B_delete = Button(body, text="Delete", width=10, height=1, font="Ivy 8 bold", command=to_remove)
B_delete.place(x=475, y=80)

window.mainloop()
