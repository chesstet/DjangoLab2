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

    name_label = Label(root, text="Ім'я")
    name_label.grid(row=0, column=0, pady=(10, 0))
    grade_label = Label(root, text="Оцінка")
    grade_label.grid(row=1, column=0)
    speciality_label = Label(root, text="Спеціальність")
    speciality_label.grid(row=2, column=0)
    course_label = Label(root, text="Курс")
    course_label.grid(row=3, column=0)
    cohort_label = Label(root, text="Група")
    cohort_label.grid(row=4, column=0)
    discipline_label = Label(root, text="Дисципліна")
    discipline_label.grid(row=5, column=0)
    id_box_label = Label(root, text="Вибір ID")
    id_box_label.grid(row=9, column=0, pady=5)

    def create_button():
        db_name = name.get()
        db_grade = grade.get()
        db_speciality = speciality.get()
        db_course = course.get()
        db_cohort = cohort.get()
        db_discipline = discipline.get()

        if db_grade != '':
            db_grade = int(db_grade)
        if db_speciality != '':
            db_speciality = int(db_speciality)
        if db_course != '':
            db_course = int(db_course)

        data_arr = [db_name, db_grade, db_speciality, db_course, db_cohort, db_discipline]


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

    submit_btn = Button(root, text="Додати запис до бази даних", command=create_button)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

    query_btn = Button(root, text="Показати записи", command=read_button)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    delete_btn = Button(root, text="Видалити запис", command=delete_button)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

    edit_btn = Button(root, text="Відредагувати запис", command=update_button)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=113)

    exportMySql_btn = Button(root, text="Експорт до MySQL", command=exportToMySQL)
    exportMySql_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=117)

    exportSQLite_btn = Button(root, text="Експорт до SQLite", command=exportToSQLite)
    exportSQLite_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=119)

    root.mainloop()
