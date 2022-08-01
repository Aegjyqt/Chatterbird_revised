import openpyxl

_all_categories = []  # лучше наверное set, но получаю unresolved attribute reference 'append' for class '()', add тоже
_translations_dict = {}  # они нужны мне как переменные класса, но это не работает. Почему?


class Datasheet:
    """ Governs essential data fom a specific sheet """

    def __init__(self, wb: str, name: str) -> None:
        self.wb = openpyxl.load_workbook(wb, read_only=True)
        self.name = name  # я могу как-то сразу ввести переменную sheet? у меня не получилось, пришлось в функциях
        self.category_ids = []
        self.category_dict = {}

    def get_ids(self) -> None:
        sheet = self.wb[self.name]
        for row in range(2, sheet.max_row):  # почему не получается с просто range(sheet.max_row)?
            self.category_ids.append(sheet[row][1].value)
        _all_categories.append(self)

    def get_category_dict(self) -> None:
        sheet = self.wb[self.name]
        keys = []
        items = []
        for i in range(2, sheet.max_row):
            temp = list(sheet[i][3].value.lower())
            for n in temp:
                if n == '\"':
                    temp.remove(n)
            key = ''.join(temp)
            keys.append(key)
            items.append(sheet[i][4].value)
            self.category_dict[key] = items[keys.index(key)] + f", актуальность: {sheet[i][2].value}"
        _translations_dict.update(self.category_dict)



departments = Datasheet('lists_for_translator.xlsx', 'управление')
departments.get_ids()  # эти вызовы можно как-то сократить?  если не в конструкторе? или так надежнее?
departments.get_category_dict()
faculties = Datasheet('lists_for_translator.xlsx', 'факультет')
faculties.get_ids()
faculties.get_category_dict()




