import openpyxl
from aiogram.utils.markdown import hcode
from collections import namedtuple


class Datasheet:
    """ Governs essential data fom a specific sheet """  # ввести указания на columns как переменные
    _all_categories = []  # как реализовать это как set?
    _translations_entire_dict = {}

    def __init__(self) -> None:  # вынеси наполнение конструктора в функции, не жадничай. Тогда проблемы не будет
        self.category_dict = {}
        self.sheet_data = ()
        self._all_categories.append(self)

    def specify_sheet_data(self, wb: str, name: str) -> (str, str):
        Sheet_data = namedtuple('Sheet_data', ['workbook', 'sheet_name'])
        this_sheet_data = Sheet_data(wb, name)
        self.sheet_data = this_sheet_data

    def get_ids(self) -> list:
        """ Gets category IDs from a specific sheet, appends the complete list of categories """
        wb = openpyxl.load_workbook(self.sheet_data.workbook)
        sheet = wb[self.sheet_data.sheet_name]
        category_ids = []
        for row in range(2, sheet.max_row):  # почему не получается с просто range(sheet.max_row)?
            category_ids.append(sheet[row][1].value)
        return category_ids

    def get_category_dict(self) -> None:
        """ Gets keys and items for a category dictionary, updates complete translation dictionary """
        wb = openpyxl.load_workbook(self.sheet_data.workbook)
        sheet = wb[self.sheet_data.sheet_name]
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
            final_item = [hcode(items[keys.index(key)]), f"актуальность: {sheet[i][2].value}"]
            self.category_dict[key] = final_item
        self._translations_entire_dict.update(self.category_dict)

    def get_all_categories(self) -> list:
        return self._all_categories

    def get_translations_entire_dict(self) -> dict:
        return self._translations_entire_dict


departments = Datasheet()
departments.specify_sheet_data('lists_for_chatterbird.xlsx', 'управление')
departments.get_ids()  # эти вызовы можно как-то сократить? => попробуй сделать класс
departments.get_category_dict()
faculties = Datasheet()
faculties.specify_sheet_data('lists_for_chatterbird.xlsx', 'факультет')
faculties.get_ids()
faculties.get_category_dict()

