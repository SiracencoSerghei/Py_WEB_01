from datetime import date, datetime, timedelta

def update_birthday(birthday: datetime, current_date: date) -> datetime:
    """update birthday year"""
    # Порівнюємо рік дня народження з поточним роком
    is_birthday_month = birthday.month < current_date.month
    is_birthday_day = (birthday.month == current_date.month and birthday.day < current_date.day)
    if is_birthday_month or is_birthday_day:
        # Якщо день народження вже минув у поточному році, збільшуємо рік на 1
        birthday = birthday.replace(year=current_date.year + 1)
    else:
        # Інакше залишаємо рік без змін
        birthday = birthday.replace(year=current_date.year)
    return birthday

def calc_current_period(current_date):
    """calculate current period of week"""
    current_date_index = current_date.weekday()
    if current_date_index == 0:
        start_period = current_date - timedelta(2)
        end_period = current_date +timedelta(4)
    elif current_date_index >0:
        start_period = current_date
        end_period = current_date + timedelta(6)
    return start_period, end_period

def get_birthdays_per_week(users):
    """main function"""
    # Реалізуйте тут домашнє завдання
    # Створення порожнього словника для зберігання інформації про дні народження
    birthdays = {}
    # Поточна дата
    current_date = date.today()
    start_period, end_period = calc_current_period(current_date)
    users_to_congratulate = []
    for user in users:
        birthday = update_birthday(user['birthday'], current_date)
        if start_period <= birthday <= end_period:
            users_to_congratulate.append(user)
    if not users_to_congratulate:
        print('No users to congratulate')
        return {}
    for user in users_to_congratulate:
        current_birthday = update_birthday(user['birthday'], current_date)
        day_of_the_week = current_birthday.strftime('%A')
        if day_of_the_week in ('Saturday','Sunday'):
            day_of_the_week = 'Monday'
        birthdays[day_of_the_week] = birthdays.get(day_of_the_week, [])
        birthdays[day_of_the_week].append(user['name'])
    return birthdays

def print_week_bdays(users_list):
    result = get_birthdays_per_week(users_list)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    
    