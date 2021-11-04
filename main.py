from peewee import *
import postgreSQL
from postgreSQL import PostgreSQLStudent
import CRUD

if __name__ == '__main__':
    #"id", "name", "grade", "speciality", "course", "cohort", "discipline"
    # with db:
    #     pg_db.create_tables([PostgreSQLStudent])

    testdata = ['Test Student', 75, 126, 3, 'IK-12', 'Programming']

    print(CRUD.executeCommand(CRUD.update, PostgreSQLStudent, postgreSQL.pg_db, testdata))
