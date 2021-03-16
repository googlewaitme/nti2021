import peewee


database = SqliteDatabase('nti.db')


class BaseModel(Model):
    class Mate:
        database = database


class User(BaseModel):
    """
        Статусы: # TODO 
    """

    name = CharField()
    surname = CharField()
    father_name = CharField()
    sex = CharField(choices=((0, 'M'), (1, 'F')))
    email = CharField()
    password = CharField(Null=True)
    status = CharField(default="student")


