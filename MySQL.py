from peewee import *
from module import Student

# змінна для доступу до БД
mysql_db = MySQLDatabase('Lab2DB', user='root', password='admin', host='127.0.0.1')


# peewee model
class MySQLStudent(Student):

    class Meta:
        database = mysql_db
        order_by = 'id'
        db_table = 'students'
