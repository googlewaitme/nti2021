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
    
    adress = CharField(null=True)
    seria = CharField(null=True)
    number = CharField(null=True)
    code = CharField(null=True)
    photo_of_pasport = CharField(null=True)
    place_of_pasport = CharField(null=True)
    
    personal_data = CharField(null=True)
    date_of_give = DateField(null=True)

    photo_of_attest = CharField(null=True)
    number_of_attest = CharField(null=True)

    # budjet of payment
    type_of_payment = CharField(null=True)
    course = CharField(null=True)

    exam_rus = IntegerField(default=0)
    exam_math = IntegerField(default=0)
    exam_inf = IntegerField(default=0)
    exam_phys = IntegerField(default=0)

    dop_points = IntegerField(default=0)

    original_docs = BooleanField(default=False)

    anket_status = CharField(default='new') # in_work, full, full_no_orig



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
