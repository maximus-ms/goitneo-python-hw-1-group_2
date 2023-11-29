invalid_cmd_msg = "Invalid command."


def add(phone_book, args):
    if len(args) < 2:
        return invalid_cmd_msg
    name = tuple(args[:-1])
    if name in phone_book:
        return "Contact already exists."
    number = args[-1]
    phone_book[name] = number
    return "Contact added."


def update(phone_book, args):
    if len(args) < 2:
        return invalid_cmd_msg
    name = tuple(args[:-1])
    if not name in phone_book:
        return "Contact doesn't exist."
    number = args[-1]
    phone_book[name] = number
    return "Contact updated."


def get(phone_book, args):
    if len(args) == 0:
        return invalid_cmd_msg
    name = tuple(args)
    return phone_book.get(name, "Contact doesn't exist.")


def get_all(phone_book):
    if len(phone_book) == 0:
        return "No contacts."
    ret = []
    for user in phone_book:
        ret.append(f"{' '.join(user)}: {phone_book[user]}")
    return "\n".join(ret)


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def run_phone_book_bot(phone_book):
    print("Welcome to the assistant bot!")
    while True:
        cmd, args = parse_input(input("Enter a command: "))
        if cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add(phone_book, args))
        elif cmd == "change":
            print(update(phone_book, args))
        elif cmd == "phone":
            print(get(phone_book, args))
        elif cmd == "all":
            print(get_all(phone_book))
        elif cmd in ("close", "exit"):
            print("Good bye!")
            break
        else:
            print(invalid_cmd_msg)


def main():
    local_phone_book = dict()
    run_phone_book_bot(local_phone_book)


if __name__ == "__main__":
    main()
