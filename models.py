from peewee import *


database = SqliteDatabase('nti.db')


def create_tables():
    database.create_tables([User, Profile])


class BaseModel(Model):
    class Meta:
        database = database



class Profile(BaseModel):
    birth_date = DateField(null=True)
    phone = CharField(null=True)
    place_of_birth = CharField(null=True)
    need_of_dorm = BooleanField(null=True)
    photo_of_anket= CharField(null=True)
    seria = CharField(null=True)
    number = CharField(null=True)
    code = CharField(null=True)
    photo_of_pasport = CharField(null=True)
    personal_data = CharField(null=True)
    date_of_give = DateField(null=True)



class User(BaseModel):
    """
        Статусы: 
         1) student
         2) worker
         3) decanat
    """
    name = CharField()
    surname = CharField()
    father_name = CharField()
    sex = CharField(choices=((0, 'M'), (1, 'F')))
    email = CharField()
    password = CharField(null=True)
    status = CharField(default="student")
    profile = ForeignKeyField(Profile)



if __name__ == '__main__':
    create_tables()
    user = User.create(name='Feodot', surname='Feofanov', 
        father_name='FFF', sex='G', 
        email='feodot@mail.ru', password='lala', 
        status='student', profile=Profile.create())

