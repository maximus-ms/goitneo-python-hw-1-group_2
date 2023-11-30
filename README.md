## GoIT Python HW-1

### Task 1: Birthdays
Prints list of Users who has birthday in nearest 7 days, per working weekday.
All BDs on weekend - to Monday's group
If today is Monday, all BDs from last weekend - to today's group.
If BD is 29-Feb - shift it to 28-Feb if currently is not leap year.

##### Usage:
```python
from birthdays import get_birthdays_per_week
# For example today is 2023-11-30
users = [
    {'name': 'Madison Jones',   'birthday': datetime(2009, 12,  6, 0, 0)},
    {'name': 'Darrell Brown',   'birthday': datetime(2022, 12,  7, 0, 0)},
    {'name': 'Hannah Burgess',  'birthday': datetime(2015, 12,  2, 0, 0)},
    {'name': 'Michael Calhoun', 'birthday': datetime(2008, 12,  5, 0, 0)},
    {'name': 'Michael Davis',   'birthday': datetime(1983, 12,  1, 0, 0)},
    {'name': 'Wendy Coleman',   'birthday': datetime(2012, 11, 28, 0, 0)},
    {'name': 'Valerie Walsh',   'birthday': datetime(1984, 12,  4, 0, 0)},
    {'name': 'Tracy Orr',       'birthday': datetime(2021, 11, 30, 0, 0)},
    {'name': 'Martin Hensley',  'birthday': datetime(1991, 11, 29, 0, 0)},
    {'name': 'Jennifer Frost',  'birthday': datetime(1986, 12,  3, 0, 0)},
]

get_birthdays_per_week(users)
# Monday: Hannah Burgess, Jennifer Frost, Valerie Walsh
# Tuesday: Michael Calhoun
# Wednesday: Madison Jones
# Thursday: Tracy Orr
# Friday: Michael Davis
```

###
##### Debug usage:
```bash
$python birthday.py -h

    Usage:
        python ./birthday.py [<fake_today_ix>]|[<year month day>] [filename] [--users_number=<N>] [--print_users_only]

        <fake_today_ix>:    Use fake date but not today
                                List of fake_todays = [
                                    0: date(2024, 1, 1) # Monday,     leap year
                                    1: date(2024, 1, 2) # Tuesday,    leap year
                                    2: date(1999, 3, 1) # Monday, non-leap year
                                    3: date(1976, 3, 1) # Monday,     leap year
                                    4: date(1998, 3, 2) # Monday, non-leap year
                                ]

        <year month day>:   Use custom Year Month Day (2000 12 1)

        --print_users_only: Print list of user dicts (1000+ items), and exit
        --users_number=<N>: Generate <N> entries + corner cases, not used if [filename], default is 1000 + corner cases
        -h, --help:         Show this message

    Example:
        $python ./birthday.py                       # to run for today with autogenerated input data
        $python ./birthday.py ./users.txt           # to run for today with data from the file
        $python ./birthday.py 3                     # to run for 1999-Mar-1 with autogenerated input data
        $python ./birthday.py 2001 12 4 ./users.txt # to run for 2001-Dec-4 with data from the file
        $python ./birthday.py 2 --users_number=10   # to run for 1999-Mar-1 with autogenerated input data (10 entries + corner cases)
```

###### Requirements:
 - Faker==18.13.0
 - python-dateutil==2.8.2
 - six==1.16.0
 - typing_extensions==4.7.1

##
### Task 2: Bot-assistant
A simple CLI Bot-assistant for a phone-book.
List of supported commands:
 - "hello"
 - "add"
 - "change"
 - "phone"
 - "all"
 - "close"
 - "exit"
