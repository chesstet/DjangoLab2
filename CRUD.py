from peewee import *

def create(className, data):
    try:
        row = className.insert(name=data[0], grade=data[1], speciality=data[2], course=data[3],
                               cohort=data[4], discipline=data[5]).execute()
    except BaseException as err:
        print('Something went wrong, because of: {}'.format(err))
