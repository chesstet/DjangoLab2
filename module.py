from peewee import *

#db =

class Student(Model):
    #"id", "name", "grade", "speciality", "course", "cohort", "discipline"
    id = PrimaryKeyField(unique=True)

    name = CharField()
    grade = IntegerField()
    speciality = IntegerField()
    course = IntegerField()
    cohort = CharField()
    discipline = CharField()


    class Meta:
        order_by = 'id'
        table_name = 'students'

# class postgreSQLStudent(Student):
#     class Meta:
#         database =
#
# class MySQLStudent(Student):
#     class Meta:
#         database =
#
# class SQLiteStudent(Student):
#     class Meta:
#         database =