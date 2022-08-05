import datasheet


class DatabaseMaker:
    """Governs the making of a database from sheets"""

    def __init__(self, datasheets: list, workbook: str) -> None:
        """Adds the wb and sheet parameters"""
        self.datasheets = datasheets
        self.workbook = workbook

    def make_database(self):
        """uses the above parameters for making a complete database from a specific workbook and its sheets"""
        for category_name in self.datasheets:
            new_category = datasheet.Datasheet()
            new_category.specify_sheet_data(self.workbook, category_name)
            new_category.get_ids()
            new_category.get_category_dict()