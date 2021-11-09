from peewee import *
import postgreSQL
from postgreSQL import PostgreSQLStudent
import CRUD

if __name__ == '__main__':




    testdata = ['', 100, '', '', '', '']

    print(CRUD.executeCommand(CRUD.read, PostgreSQLStudent, testdata))
