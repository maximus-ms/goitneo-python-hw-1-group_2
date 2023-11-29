from collections import defaultdict
from datetime import datetime, timedelta, time, date
from calendar import isleap, day_name


def get_birthdays_per_week(users, detailed_info=False):
    days = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        birthday = user["birthday"].date()
        # if User has BD at 29-Feb, usually he/she selebrates it at 28-Feb of non-leap year
        if not isleap(today.year) and birthday.month == 2 and birthday.day == 29:
            birthday = birthday.replace(day=28)
        birthday_this_year = birthday.replace(year=today.year)
        delta_days = (birthday_this_year - today).days
        if delta_days < 0:
            if today.month == 12 and (-366 < delta_days < -(366 - 13)):
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                delta_days = (birthday_this_year - today).days
            else:
                # there is not reason to handle passed BD if today is not Dec
                # and if BD later than 11-Jan even if today is 31-Dec Monday of leap year
                continue
        # accordint to the task: we need users for the next week, including ones whos BD is on this weekend
        # The NEXT week, BUT NOT THE NEAREST 7 days!
        bd_for_next_week_starts_in_days = (
            7 - today.weekday() - 2
        )  # this weekend goes to the next week
        bd_for_next_week_ends_in_days = bd_for_next_week_starts_in_days + 7
        if (
            bd_for_next_week_starts_in_days
            <= delta_days
            < bd_for_next_week_ends_in_days
        ):
            congrats_at = birthday_this_year.weekday()
            if (
                congrats_at > 4
            ):  # BD at weekend (days 5 and 6) will congratulate at Monday (day 0)
                congrats_at = 0
            if detailed_info:
                print(
                    f"BD at {user['birthday'].date()}, in {delta_days:>2} days ({day_name[birthday_this_year.weekday()]:>9}), congrats at {day_name[congrats_at]:>9}"
                )
            days[congrats_at].append(user["name"])
    for day in range(7):
        if len(days[day]) > 0:
            print("{}: {}".format(day_name[day], ", ".join(sorted(days[day]))))


if __name__ == "__main__":
    from faker import Faker
    from random import randint

    def __generate_user_birthdays_test_data(num: int, add_corner_cases=False):
        data = []
        fake = Faker()
        for i in range(num):
            d = {
                "name": fake.name(),
                "birthday": datetime.combine(fake.date_between("-80y"), time()),
            }
            data.append(d)
        if add_corner_cases:
            # add users with BD in a range -3..15 days from today
            today = datetime.today().date()
            for i in range(-3, 15):
                for iters in range(randint(1, 3)):
                    date = today.replace(year=int(fake.year()))
                    date = date + timedelta(days=i)
                    d = {
                        "name": fake.name(),
                        "birthday": datetime.combine(date, time()),
                    }
                    data.append(d)
        return data

    users = __generate_user_birthdays_test_data(1000)
    get_birthdays_per_week(users)
