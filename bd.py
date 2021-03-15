import peewee


database = SqliteDatabase('nti.db')


class BaseModel(Model):
    class Mate:
        database = database
