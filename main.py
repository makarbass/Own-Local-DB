from typing import Dict
from database import Database

DB = Database()
COMMAND_HANDLERS: Dict[str, callable] = {
        "SET": DB.set,
        "GET": DB.get,
        "UNSET": DB.unset,
        "COUNTS": DB.count,
        "FIND": DB.find,
        "BEGIN": DB.begin,
        "ROLLBACK": DB.rollback,
        "COMMIT": DB.commit,
    }


def main() -> None:
    while True:
        try:
            command = input("> ").split()
            if not command:
                continue
            command_name = command[0].upper()
            args = command[1:]
            if command_name in COMMAND_HANDLERS:
                handler = COMMAND_HANDLERS[command_name]
                if len(args) != handler.__code__.co_argcount - 1:
                    print(f"{command_name}: неверное число аргументов")
                else:
                    result = handler(*args)
                    if result is not None:
                        print(result)
            elif command_name == "END":
                break
            else:
                print("Неверная команда")
        except EOFError:
            break

if __name__ == "__main__":
    main()