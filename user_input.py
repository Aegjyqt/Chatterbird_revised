import datasheet

class User_Input():
    """Governs user input"""

    def __init__(self, user_input: str):
        self.user_input = user_input
        self.process_simplify()
        self.process_declensions()

    def process_simplify(self):
        """changes text format to lowercase, gets rid of quotation marks"""
        temp = list(self.user_input.lower())
        for i in temp:
            if i == "\"":
                temp.remove(i)
        self.user_input = ''.join(temp)

    def process_declensions(self):
        """ process_declension: changes category-specific identifier words to the nominative case"""
        elements = self.user_input.split(' ')
        for category in datasheet._all_categories:
            temp_list = category.category_ids
            for i in range(0, len(elements) - 1):  # кажется, я что-то упускаю, можно проще?
                if elements[i] in temp_list:
                    elements[i] = category.name
        self.user_input = ' '.join(elements)

    def process_translate(self) -> str:
        """ process_translate: translates a string processed with the two of the above """
        if self.user_input in datasheet._translations_dict:
            return datasheet._translations_dict[self.user_input]





