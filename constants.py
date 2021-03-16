
class Cource:
    def __init__(self, name, subject, is_budjet, is_payment):
        self.name = name
        self.subject = subject
        self.is_payment = is_payment
        self.is_budjet = is_budjet


physic = 1
inform = 0


cources = [ 
    Cource('Прикладная математика', inform, True, True), 
    Cource('Информатика и вычислительная техника', inform, True, True),
    Cource('Автоматизация управления в технических системах', inform, False, True),
    Cource('Инфокоммуникационные технологии', physic, True, True),
    Cource('Защищенные сети и системы', physic, False, True)
]

# Все достижения оцениваются в 10 баллов
achievments = [
    'ГТО',
    'Аттестат с отличием (или диплом СПО)',
    'Всероссийская олимпиада по профильному предмету или математике',
    'Предпрофессиональный экзамен'
]

# https://yandex.ru/support/mail/mail-clients/others.html
univer_email = 'info.sgu@yandex.ru'
univer_password = 'infosgu2021'
