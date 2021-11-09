from functools import reduce

from peewee import *
import operator

def executeCommand(fn, class_name, *data):
    with class_name.getDataBase(class_name):
        return fn(class_name, *data)


def create(class_name, data):
    try:
        row = class_name.insert(name=data[0], grade=data[1], speciality=data[2], course=data[3],
                               cohort=data[4], discipline=data[5]).execute()
    except Exception as err:
        print('Something went wrong, because of: {}'.format(err))

def delete(class_name, id):
    try:
        deleted_row = class_name.delete().where(class_name.id == id).execute()
    except Exception as err:
        print('Something went wrong, because of: {}'.format(err))

#"id", "name", "grade", "speciality", "course", "cohort", "discipline"

def update(class_name, data, id):
    try:
        fields = [class_name.name, class_name.grade, class_name.speciality, class_name.course, class_name.cohort, class_name.discipline]
        fields_change = {}
        for i in range(len(data)):
            if data[i] != None:
                fields_change |= {fields[i]:data[i]}
        updated_row = class_name.update(fields_change).where(class_name.id == id).execute()
    except Exception as err:
        print('Something went wrong, because of: {}'.format(err))

def read(class_name, data):
    try:
        int_fields = [class_name.grade, class_name.speciality, class_name.course]
        clauses = [
            (class_name.name ** f'%{data[0]}%'),
            (class_name.cohort ** f'%{data[4]}%'),
            (class_name.cohort ** f'%{data[4]}%')
        ]
        for i in range(3):
            if data[i+1] != '':
                clauses.append((int_fields[i] == data[i+1]))

        query = class_name.select().where(reduce(operator.and_, clauses))

        result = [(item.name, item.grade, item.speciality, item.grade, item.cohort, item.discipline) for item in query]
        print(f'result :{result}')
        return result
    except Exception as err:
        print('Something went wrong, because of: {}'.format(err))