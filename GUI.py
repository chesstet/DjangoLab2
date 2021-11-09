from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
import tkinter.ttk as ttk
import CRUD
from postgreSQL import PostgreSQLStudent
from MySQL import MySQLStudent


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

        CRUD.executeCommand(CRUD.create, PostgreSQLStudent, data_arr)


    def read_button():
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

        queried = CRUD.executeCommand(CRUD.read, PostgreSQLStudent, data_arr)


        global reader
        reader = Tk()
        table = Table(reader, headings=('id', 'name', 'grade', 'speciality', 'course', 'cohort', 'discipline'),
                      rows=queried)
        table.pack(expand=tk.YES, fill=tk.BOTH)

    def update_button():
        def button_pusher():
            db_name = name_editor.get()
            db_grade = grade_editor.get()
            db_speciality = speciality_editor.get()
            db_course = course_editor.get()
            db_cohort = cohort_editor.get()
            db_discipline = discipline_editor.get()

            data_arr = [db_name, db_grade, db_speciality, db_course, db_cohort, db_discipline]

            CRUD.executeCommand(CRUD.update, PostgreSQLStudent, data_arr, record_id)

            editor.destroy()
            root.deiconify()

        root.withdraw()

        global editor
        try:
            editor = Tk()
            editor.title('Update A Record')
            editor.geometry("400x300")

            record_id = int(id_box.get())
            records = CRUD.executeCommand(CRUD.readById, PostgreSQLStudent, record_id)

            name_editor = Entry(editor, width=30)
            name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
            grade_editor = Entry(editor, width=30)
            grade_editor.grid(row=1, column=1)
            speciality_editor = Entry(editor, width=30)
            speciality_editor.grid(row=2, column=1)
            course_editor = Entry(editor, width=30)
            course_editor.grid(row=3, column=1)
            cohort_editor = Entry(editor, width=30)
            cohort_editor.grid(row=4, column=1)
            discipline_editor = Entry(editor, width=30)
            discipline_editor.grid(row=5, column=1)

            name_editor.insert(0, records[1])
            grade_editor.insert(0, records[2])
            speciality_editor.insert(0, records[3])
            course_editor.insert(0, records[4])
            cohort_editor.insert(0, records[5])
            discipline_editor.insert(0, records[6])

            name_label = Label(editor, text="name")
            name_label.grid(row=0, column=0, pady=(10, 0))
            grade_label = Label(editor, text="grade")
            grade_label.grid(row=1, column=0)
            speciality_label = Label(editor, text="speciality")
            speciality_label.grid(row=2, column=0)
            course_label = Label(editor, text="course")
            course_label.grid(row=3, column=0)
            cohort_label = Label(editor, text="cohort")
            cohort_label.grid(row=4, column=0)
            discipline_label = Label(editor, text="discipline")
            discipline_label.grid(row=5, column=0)

            edit_btn = Button(editor, text="Save Record", command=button_pusher)
            edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

        except ValueError:
            mb.showerror(title='Oops, smth go wrong', message='id must be a number')
            editor.destroy()
            root.deiconify()
        except TypeError:
            mb.showerror(title='Oops, smth go wrong', message='id doesnt exist')
            editor.destroy()
            root.deiconify()

    def delete_button():
        db_id = int(id_box.get())

        CRUD.executeCommand(CRUD.delete, PostgreSQLStudent, db_id)

    def exportToMySQL():
        try:
            data_arr = ['' for i in range(6)]

            rows = CRUD.executeCommand(CRUD.read, PostgreSQLStudent, data_arr)
            columns = ("id", "name", "grade", "speciality", "course", "cohort", "discipline")

            for row in rows:
                CRUD.executeCommand(CRUD.create, MySQLStudent, row)

            queried = CRUD.executeCommand(CRUD.read, PostgreSQLStudent, data_arr)
            global reader

            reader = Tk()
            table = Table(reader, headings=('id', 'name', 'grade', 'speciality', 'course', 'cohort', 'discipline'), rows=queried)
            table.pack(expand=tk.YES, fill=tk.BOTH)
        except Exception as err:
            print(f'Something went wrong because of: {err}')


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
