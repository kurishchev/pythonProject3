# Если строки recipient и sender не содержит "@" или
# не оканчивается на ".com"/".ru"/".net", то вывести
# на экран(в консоль) строку: "Невозможно отправить
# письмо с адреса <sender> на адрес <recipient>".
def check_email(adress):
    x = (adress.endswith('.com') or adress.endswith('.ru') or adress.endswith('.net')) and (adress.find('@') > 0)
    return x

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if (check_email(recipient) and check_email(sender)) and (recipient != sender) and (sender == 'university.help@gmail.com'):
        print('Письмо успешно отправлено с адреса ',sender , ' на адрес ',recipient, '.')
    elif not (check_email(recipient) and check_email(sender)):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, '.')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ',sender , 'на адрес ', recipient,'.')



send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
