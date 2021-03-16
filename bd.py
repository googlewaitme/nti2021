from models import *


class RegistrationApi:
    def check_email(self, email):
        """Возвращает список из двух элементов, примеры:
            (True, 'all okey'),
            (False, 'Не правильно введен эмейл')
            (False, 'Такой емэйл уже есть')
        """
        # TODO BULAT
        return (False, 'Такой email уже существует')

    def check_email_is_unique(self, email):
        users = User.select().where(User.email==email)
        return len(users) == 0

    def register_user(self, **params):
        """
        Пример исполльзования:
            register_user(name='Bulat', surname='Zaripov', father_name='Ruslanovi4',
                            email='bulat.zar-1203@yandex.ru', password='LALALALA')
        """
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
        # TODO BULAT
        pass

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
        # TODO
        pass

    def set_phone(self, phone):
        # TODO
        pass 

    def set_place_of_birth(self, place):
        # TODO 
        pass

    def set_need_of_dorm(self, need_of):
        # Нужно ли общежитие
        # TODO 
        pass

    def set_photo_of_anket(self, photo_path):
        # СМОТРИ photo.py
        # TODO 
        pass 


class PasportApi:
    """
        Здесь будут содержаться все модули взаимодействия с анкетными данными
        Только личные данные
    """
    def __init__(self, session):
        self.session = session

    def set_data(self, seria, number):
        # TODO 
        pass 

    def set_code(self, code):
        # код подразделения
        # TODO 
        pass

    def set_date_of_give(self, date):
        # TODO 
        pass

    def set_photo_of_pasport(self, photo):
        # TODO 
        pass

    def set_personal_data(self, photo):
        # согласие на обработку ПД
        # TODO 
        pass
