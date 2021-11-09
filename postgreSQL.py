from peewee import *
from module import Student

pg_db = PostgresqlDatabase(database='Lab2DB', user='postgres', password="admin", host="127.0.0.1")

class PostgreSQLStudent(Student):

    class Meta:
        database = pg_db
        order_by = 'id'
        table_name = 'students'