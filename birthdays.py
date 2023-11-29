from collections import defaultdict
from datetime import datetime, timedelta, time, date
from calendar import isleap, day_name


def get_birthdays_per_week(users, detailed_info=False, today=None):
    days = defaultdict(list)
    if not today:
        today = datetime.today().date()
    if detailed_info:
        print("Today:", today)
    for user in users:
        birthday = user["birthday"].date()
        if (
            not isleap(today.year)
            and birthday.month == 2
            and birthday.day == 29
        ):
            if not isleap(birthday.year):
                # looks like an error
                # it is impossible to have a BD at 29-Feb in non leap year
                # let's just skip this record for now
                continue
            # if User has BD at 29-Feb, usually he/she celebrates at 28-Feb if non-leap year
            birthday = birthday.replace(day=28)
        birthday_this_year = birthday.replace(year=today.year)
        delta_days = (birthday_this_year - today).days

        # According to the updated information about this task:
        #   we need users for the next 7 days, but
        #   if some BDs are on the nearest weekend: shift them forward to Monday
        #   if today is Monday:
        #       take BDs from the past weekend
        #       and BDs on next weekend are out of 7 days and will be celebrated next Monday

        is_monday = today.weekday() == 0
        min_delta = 0
        if is_monday:
            # on Mondays we want to congrats Users from Saturday and Sunday
            min_delta = -2

        if delta_days < min_delta:
            if delta_days < -(366 - 7):
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1
                )
                delta_days = (birthday_this_year - today).days
            else:
                # there is no reason to handle passed BD if today is not Dec
                # and if BD later than 6-Jan even if today is 31-Dec of leap year
                continue
        elif delta_days >= 363 and is_monday:
            # if today is 1..2-Jan Monday
            birthday_this_year = birthday_this_year.replace(
                year=today.year - 1
            )
            delta_days = (birthday_this_year - today).days

        if min_delta <= delta_days < min_delta + 7:
            congrats_at = birthday_this_year.weekday()
            if congrats_at > 4:
                # BD at weekend (days 5 and 6) will congrats at Monday (day 0)
                congrats_at = 0
            if detailed_info:
                print(
                    "BD at {}, in {:>2} days ({:>9}), congrats at {:>9}".format(
                        user["birthday"].date(),
                        delta_days,
                        day_name[birthday_this_year.weekday()],
                        day_name[congrats_at],
                    )
                )
            days[congrats_at].append(user["name"])
    for day in range(7):
        if len(days[day]) > 0:
            print("{}: {}".format(day_name[day], ", ".join(sorted(days[day]))))


if __name__ == "__main__":
    from faker import Faker
    from random import randint

    def __find_years(month, day, weekday, is_leap_year=None):
        years = []
        for i in range(2024, 1899, -1):
            if type(is_leap_year) is bool and isleap(i) != is_leap_year:
                continue
            if date(i, month, day).weekday() == weekday:
                years.append(f"{'*' if isleap(i) else ''}{i}")
        return years

    def __generate_user_birthdays_test_data(
        num: int, add_corner_cases=False, today=None
    ):
        data = []
        fake = Faker()
        for i in range(num):
            d = {
                "name": fake.name(),
                "birthday": datetime.combine(
                    fake.date_between("-80y"), time()
                ),
            }
            data.append(d)
        if add_corner_cases:
            # add users with BD in a range -3..15 days from today
            if today is None:
                today = datetime.today().date()
            for i in range(-3, 15):
                for iters in range(randint(1, 3)):
                    new_date = date(2000, today.month, today.day) + timedelta(
                        days=i
                    )
                    fake_year = int(fake.year())
                    while (
                        new_date.month == 2
                        and new_date.day == 29
                        and not isleap(fake_year)
                    ):
                        fake_year = int(fake.year())
                    new_date = new_date.replace(year=fake_year)
                    d = {
                        "name": fake.name(),
                        "birthday": datetime.combine(new_date, time()),
                    }
                    data.append(d)
        return data

    fake_today = None
    # fake_today = date(2024, 1, 1) # Monday,     leap year
    # fake_today = date(2024, 1, 2) # Tuesday,    leap year
    # fake_today = date(1999, 3, 1) # Monday, non-leap year
    # fake_today = date(1976, 3, 1) # Monday,     leap year
    # fake_today = date(1998, 3, 2) # Monday, non-leap year
    users = __generate_user_birthdays_test_data(1000, True, today=fake_today)
    get_birthdays_per_week(users, True, today=fake_today)
