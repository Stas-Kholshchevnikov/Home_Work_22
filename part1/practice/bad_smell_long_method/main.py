# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    """
    Получение списка пользователей
    """
    data = _read(csv)
    result = _sort(data)
    return _filter(result)


def _read(csv):
    """
    Чтение из файла
    """
    return [item.split(";") for item in csv.split("\n")]


def _sort(data):
    """
    Сортировка списка
    """
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    """
    Фильтрация списка по заданному условию
    """
    return [item for item in data if int(item[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
