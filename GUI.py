from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrollbar = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def run():
    root = Tk()
    root.title('Working with db')
    root.geometry("400x600")

    name = Entry(root, width=30)
    name.grid(row=0, column=1, padx=20, pady=(10, 0))
    grade = Entry(root, width=30)
    grade.grid(row=1, column=1)
    speciality = Entry(root, width=30)
    speciality.grid(row=2, column=1)
    course = Entry(root, width=30)
    course.grid(row=3, column=1)
    cohort = Entry(root, width=30)
    cohort.grid(row=4, column=1)
    discipline = Entry(root, width=30)
    discipline.grid(row=5, column=1)
    id_box = Entry(root, width=30)
    id_box.grid(row=9, column=1, pady=5)

    name_label = Label(root, text="name")
    name_label.grid(row=0, column=0, pady=(10, 0))
    grade_label = Label(root, text="grade")
    grade_label.grid(row=1, column=0)
    speciality_label = Label(root, text="speciality")
    speciality_label.grid(row=2, column=0)
    course_label = Label(root, text="course")
    course_label.grid(row=3, column=0)
    cohort_label = Label(root, text="cohort")
    cohort_label.grid(row=4, column=0)
    discipline_label = Label(root, text="discipline")
    discipline_label.grid(row=5, column=0)
    id_box_label = Label(root, text="Select ID")
    id_box_label.grid(row=9, column=0, pady=5)

    def create_button():
        pass

    def read_button():
        pass

    def delete_button():
        pass

    def update_button():
        pass

    def exportToMySQL():
        pass

    def exportToSQLite():
        pass

    submit_btn = Button(root, text="Add Record To Database", command=create_button)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    query_btn = Button(root, text="Show Records", command=read_button)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    delete_btn = Button(root, text="Delete Record", command=delete_button)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    edit_btn = Button(root, text="Edit Record", command=update_button)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    exportMySql_btn = Button(root, text="Export to MySQL", command=exportToMySQL)
    exportMySql_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    exportSQLite_btn = Button(root, text="Export to SQLite", command=exportToSQLite)
    exportSQLite_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    root.mainloop()
