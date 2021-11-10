from peewee import *


# peewee model
class Student(Model):
    id = PrimaryKeyField(unique=True)

    name = CharField()
    grade = IntegerField()
    speciality = IntegerField()
    course = IntegerField()
    cohort = CharField()
    discipline = CharField()

    def getDataBase(self):
        return self._meta.database

    class Meta:
        order_by = 'id'
        table_name = 'students'
