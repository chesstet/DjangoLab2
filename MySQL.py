from peewee import *
from module import Student

mysql_db = MySQLDatabase('Lab2DB')


class MySQLStudent(Student):

    class Meta:
        database = mysql_db
        order_by = 'id'
        db_table = 'students'
