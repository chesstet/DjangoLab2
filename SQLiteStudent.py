from peewee import *
from module import Student

# змінна для доступу до БД
sqlite_db = SqliteDatabase('Lab2DB.db', pragmas={'journal_mode': 'wal', 'cache_size': -1 * 64000,
                                                 'foreign_keys': 1, 'ignore_check_constraints': 0,  'synchronous': 0})


# peewee model
class SQLiteStudent(Student):

    class Meta:
        database = sqlite_db
        order_by = 'id'
        db_table = 'students'
