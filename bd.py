from models import *


def give_all_users():
    return list(User.select())

class RegistrationApi:
    """
    a = RegistrationApi()
    a.register_user(params)
    
    """

    def __init__(self):
        pass

    def check_email_is_unique(self, email):
        users = User.select().where(User.email==email)
        return len(users) == 0

    def register_user(self, **params):
        """
        Пример исполльзования:
            register_user(name='Bulat', surname='Zaripov', father_name='Ruslanovi4',
                            email='bulat.zar-1203@yandex.ru', sex='M', password='LALALALA')
        """
        params['profile'] = Profile.create()
        User.create(**params)

    def user_is_exist(self, password, email):
        """
        Проверяет по введенным паролю и почте, что такой пользователь существует и может войти в аккаунт
        """
        users = User.select().where(User.password==password and User.email==email)
        return not len(users) == 0
    
    def user_get_session(self, password, email):
        """
        Возвращает аккаунт пользователя 
        И все связанные с ним обьекты
        """
        return User.get(User.password==password, User.email==email)


class PersonalDataApi:
    """
        Здесь будут содержаться все модули взаимодействия с анкетными данными
        Только личные данные и адресс
    """
    def __init__(self, session):
        self.session = session

    def set_adress(self, adress):
        # Устанавливает адресс пользователя
        # просто одна большая строка с адрессом
        self.session.profile.adress = adress
        self.session.save()

    def set_name(self, surname=None, name=None, father_name=None):
        """
            api.set_name(name='not Bulat')
            Если меняется только имя пользователя
        """
        self.session.name = name
        self.session.save()

    def set_email(self, email):
        self.session.email = email
        self.session.save()

    def set_password(self, password):
        self.session.password = password
        self.session.save()

    def set_sex(self, sex):
        self.session.sex = sex
        self.session.save()

    def set_birth_date(self, date):
        # Дата должна быть в формате datetime.date
        self.session.profile.birth_date = date 
        self.session.save() 

    def set_phone(self, phone):
        self.session.profile.phone = phone 
        self.session.save() 

    def set_place_of_birth(self, place):
        self.session.profile.place_of_birth = place
        self.session.save() 

    def set_need_of_dorm(self, need_of_dorm):
        # Нужно ли общежитие
        self.session.profile.need_of_dorm = need_of_dorm
        self.session.save() 

    def set_photo_of_anket(self, photo):
        # СМОТРИ photo.py
        self.session.profile.photo_of_anket = photo
        self.session.save() 


class PasportApi:
    """
        Здесь будут содержаться все модули взаимодействия с анкетными данными
        Только личные данные
    """
    def __init__(self, session):
        self.session = session

    def set_data(self, seria, number):
        self.session.profile.seria = seria
        self.session.profile.number = number
        self.session.save() 

    def set_place_of_pasport(self, place):
        self.session.profile.place_of_pasport = place
        self.session.save()

    def set_code(self, code):
        # код подразделения
        self.session.profile.code = code
        self.session.save() 


    def set_date_of_give(self, date):
        self.session.profile.date_of_give = date 
        self.session.save() 


    def set_photo_of_pasport(self, photo):
        self.session.profile.set_photo_of_pasport = photo
        self.session.save() 


    def set_personal_data(self, photo):
        # согласие на обработку ПД
        self.session.profile.personal_data = photo
        self.session.save() 


class SchoolDataApi:
    def __init__(self, session):
        self.session = session

    def set_attest(self, number, photo):
        self.session.profile.photo_of_attest = photo 
        self.session.profile.number_of_attest = number
        self.session.save() 


    def set_type_of_payment(self, type_of_payment):
        self.session.profile.type_of_payment = type_of_payment
        self.session.save() 


    def set_course(self, course):
        self.session.profile.course = course
        self.session.save() 


    def set_exams(self, rus=0, math=0, inf=0, phys=0):
        self.session.profile.exam_rus = rus 
        self.session.profile.exam_math = math 
        self.session.profile.exam_inf = inf
        self.session.profile.exam_phys = phys
        self.session.save() 

    def set_dop_points(self, sum_points):
        self.session.profile.dop_points = sum_points
        self.session.save() 

    def set_original_docs(self, original):
        self.session.profile.original_docs = original
        self.session.save() 
