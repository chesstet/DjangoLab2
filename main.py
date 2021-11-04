from peewee import *
from postgreSQL import *
import CRUD

if __name__ == '__main__':
    #"id", "name", "grade", "speciality", "course", "cohort", "discipline"
    with pg_db:
        pass
        #pg_db.create_tables([PostgreSQLStudent])

    testdata = ['Good Student', 80, 123, 3, 'IV-91', 'Sport']

    with pg_db:
        CRUD.create(PostgreSQLStudent, testdata)