from docxtpl import DocxTemplate 
from constants import monthes

class Saver:
    # TODO
    """
        Смотри, мне кажется, что когда пользователь указывает нам фотографию,
        мы будем копировать её, куда-то в скрытую папке и в б/д хранить путь в секретке
        ---

        GUI -> Saver -> DB
           path      path
                to
           row       processed     
           photo     photo
    """
    pass


def generic_document(session):
    doc = DocxTemplate('static/template.docx')

    sl = {
        'name': user.name,
        'surname': user.surname, 
        'father_name': user.father_name,
        'date_of_give': user.profile.date_of_give,
        'place_of_pasport': user.profile.place_of_pasport,
        'day': date.today().day,
        'month': monthes[date.today().month - 1],
        'seria': user.profile.seria,
        'nomer': user.profile.nomer
    }
    doc.render(sl)
    doc.save('Перс_данные.docx')

if __name__ == '__main__':
    from models import *
    from datetime import date

    user = User(
        name='Bulat', 
        surname='Zaripov', 
        father_name='Ruslanovi4',
        email='bulat.zar-1203@yandex.ru',
        sex='M', 
        password='LALALALA',
        profile=Profile.create()
    )
    user.profile.seria = '8016'
    user.profile.nomer = '234234'
    user.profile.date_of_give = date(2016, 12, 3)
    user.profile.place_of_pasport = 'Mrakovo'
    user.save()
    generic_document(user)
