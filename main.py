from typing import Callable, List


def create_handlers(callback: Callable) -> List:
    handlers = [lambda step=step: step for step in callback(range(5))]
    return handlers


def execute_handlers(handlers: List) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        print(handler())


if __name__ == '__main__':
    execute_handlers(create_handlers(lambda x: x))
