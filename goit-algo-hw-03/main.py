import random
import re
import datetime


def get_days_from_today(date):
    try:
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # Парсимо дату з str в datetime.
        date_today = datetime.datetime.today().date()  # Отримуємо сьогодніню дату
        date_sub = (date_today - formatted_date).days  # Обчислюємо різницю між датами
        return date_sub
    except ValueError:
        print("Ви ввели неправильний формат або недійсну дату")


print(get_days_from_today('2024-02-02'))


def get_numbers_ticket(min, max, quantity):
    if min < 1 or min >= max or max > 1000 or quantity > (max - min + 1):  # Перевірка параметрів
        print("Ви ввели неправильні параметри")
        return []
    else:
        return sorted(random.sample(list(range(min, max + 1)), quantity))  # повертаємо список з вибраними унікальними числами


print(get_numbers_ticket(10, 20, 5))


dirty_phones = ["    +38(050)123-32-34",
                "     0503451234",
                "(050)8889900",
                "38050-111-22-22",
                "38050 111 22 11   "]


def normalize_phone(phone_number):
    patt = r'[\d\+]+'
    phone_number = ''.join(re.findall(patt, phone_number))
    if len(phone_number) == 10:
        phone_number = "+38" + phone_number
    elif len(phone_number) == 12:
        phone_number = "+" + phone_number
    return phone_number


for phone in dirty_phones:
    print(normalize_phone(phone))


users = [
    {"name": "John Doe", "birthday": "1985.02.03"},
    {"name": "Jane Smith", "birthday": "1990.02.04"}
]


def get_upcoming_birthdays(users=None):
    today_date = datetime.datetime.today().date()  # Беремо сьогоднішню дату
    birthdays = []  # Створюємо список для результатів
    for user in users:  # Перебираємо користувачів
        birthday_date = user["birthday"]  # Отримуємо дату народження людини в str
        birthday_date = str(today_date.year)+birthday_date[4:]  # Замінюємо рік на тепершіній
        birthday_date = datetime.datetime.strptime(birthday_date, "%Y.%m.%d").date()  # Перетворюємо дату народження в date
        week_day = birthday_date.isoweekday()  # Отримуємо день тижня (1-7)
        days_between = (birthday_date-today_date).days  # Рахуємо різницю між сьогодні і днем народження цього року та отримуємо дні
        if 0 <= days_between < 7:  # Якщо день народження відбудеться протягом 7 днів від сьогоднішньої дати
            if week_day < 6:  # Якщо понеділок-п'ятниця
                birthdays.append({'name': user['name'], 'birthday': birthday_date.strftime("%Y.%m.%d")})
                # Записуємо у список
            else:
                if (birthday_date+datetime.timedelta(days=1)).weekday() == 0:  # Якщо неділя
                    birthdays.append({'name': user['name'], 'birthday': (birthday_date+datetime.timedelta(days=1)).strftime("%Y.%m.%d")})
                    # Переносимо на понеділок. Записуємо у список.
                elif (birthday_date+datetime.timedelta(days=2)).weekday() == 0:  # Якщо субота
                    birthdays.append({'name': user['name'], 'birthday': (birthday_date+datetime.timedelta(days=2)).strftime("%Y.%m.%d")})
                    # Переносимо на понеділок. Записуємо у список.
    return birthdays


print(get_upcoming_birthdays(users))
