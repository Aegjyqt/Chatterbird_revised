import datasheet


class UserInput:
    """Governs user input"""

    def __init__(self) -> None:
        pass

    def get_simplified_string(self, string_for_prcocessing: str) -> str:
        """changes text format to lowercase, gets rid of quotation marks"""
        return string_for_prcocessing.lower().replace("\"", "")

    def get_string_with_nominative_identifier(self, user_input: str) -> str:
        """ process_declension: changes category-specific identifier words to the nominative case"""
        user_input_elements = user_input.split(' ')
        for category in datasheet.Datasheet().get_all_categories():
            category_ids_list = category.get_ids()
            for word in user_input_elements:
                if word in category_ids_list:
                    user_input_elements[user_input_elements.index(word)] = category.sheet_data[1]
        return ' '.join(user_input_elements)

    def get_translation(self, user_input: str) -> str:
        """ process_translate: translates a string processed with the two of the above """
        pre_processed_str = self.get_string_with_nominative_identifier(user_input)
        if pre_processed_str in datasheet.Datasheet().get_translations_entire_dict():
            return datasheet.Datasheet().get_translations_entire_dict()[pre_processed_str]
