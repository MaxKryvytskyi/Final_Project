from datetime import datetime as dt
from datetime import *
from rich.table import Table


today = None
next_week = None
birthday_list = None 

# Функція яка перевіряє в кого день народження на протязі наступної кількості днів.
def get_birthdays_per_week(users, days):
    print("")
    table = Table(title=f"All Birthday {days} days")
    table.add_column("Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Birthday", justify="center", style="cyan", no_wrap=True)
    table.add_column("Days to birthday ", justify="center", style="cyan", no_wrap=True)

    for user, birthday in users.items():
        if birthday.value == "none": continue
        date_u = datetime.strptime(birthday.value, "%d.%m.%Y")
        date = datetime(year=today.year, month=date_u.month, day=date_u.day)

        if date > today and date < next_week:
            table.add_row(f"{user}", 
                            f"{birthday.value}",
                            f"{birthday.days_to_birthday()}")
        else:
            date = datetime(year=today.year+1, month=date_u.month, day=date_u.day)
            if date > today and date < next_week: 
                table.add_row(f"{user}", 
                              f"{birthday.value}",
                              f"{birthday.days_to_birthday()}")
    return table


def main(adress_book, days=7):
    global today, next_week, birthday_list
    birthday_list = []
    today = dt.now()
    next_week = today + timedelta(days)
    users = {}
    users = dict(map(lambda i: (adress_book[i].name.value, adress_book[i].birthday if adress_book[i].birthday else "none"), adress_book.keys()))
    return get_birthdays_per_week(users, days)