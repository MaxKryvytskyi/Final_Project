from datetime import datetime as dt
from datetime import *

flag = 0
today = None
next_week = None
weekday_list = None 
birthday_list = None 

# Функція яка перевіряє в кого день народження на протязі наступної кількості днів.
def get_birthdays_per_week(users):
    for user, birthday in users.items():

        date_u = birthday
        date = datetime(year=today.year, month=date_u.month, day=date_u.day)

        if date > today and date < next_week: # Перевіряє чи є впродовж тижня в цієї людини день народження.
            if weekday_list[str(date.weekday())] not in ["Saturday", "Sunday"]: # Перевіряє чи випадає день народження на суботу неділю.
                birthday_list[weekday_list[str(date.weekday())]].append(user)
            else: # Якщо випадає на суботу/неділю додає до понеділка.
                birthday_list[weekday_list["0"]].append(user)
    return output_of_results(birthday_list)

# Функція яка є частиною output_of_results. 
def fix(weekday, result, text):
    global flag
    flag += 1
    if len(result) != 0:
        if flag > 1: text += '| {:^11} : {:<59}|'.format(' ' * len(weekday), ', '.join(result)) + "\n"
        else: text += '| {:^11} : {:<59}|'.format(weekday, ', '.join(result)) + "\n"
    return text

# Функція яка виводить результат. 
def output_of_results(birthday_list):
    sums = 0
    result = []
    text = ""
    text += '{:^11} '.format(" " + "_"*74 + " ") + "\n"
    text += '|{:^74}| '.format("Birthday") + "\n"
    text += '{:^11} '.format("|" + "_"*74 + "|") + "\n"
    for weekday, names in birthday_list.items():
        global flag
        if names == []: continue
        for name in names:
            sums += len(name)
            result.append(name)
            if sums > 30:   
                text = fix(weekday, result, text)
                result.clear()
                sums = 0
        if True:
            text = fix(weekday, result, text)
            result.clear()
        
        flag = 0
        text += '{:^11} '.format("|" + "_"*74 + "|") + "\n"
    return text

def main(adress_book, days=7):
    global today, next_week, weekday_list, birthday_list
    weekday_list = { "0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday", "6": "Sunday"}
    birthday_list = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}
    today = dt.now()
    next_week = today + timedelta(days)
    users = {}
    users = dict(map(lambda i: (adress_book[i].name.value, adress_book[i].birthday.value), adress_book.keys()))
    return get_birthdays_per_week(users)