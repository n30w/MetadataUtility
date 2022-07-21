# Printer class for general printing of Excel sheets

class ListMe(object):
    def __int__(self):
        pass

    # Title Numbers
    # 1. Commencement
    # 2. Baccalaureate
    # 3. Holoku
    # 4. Variety Show
    def print_year_list(self, title_num, output_selection, first_year, last_year) -> list:
        _first_year = first_year
        _data_range = last_year - _first_year
        _string_to_append = ""
        _titles = (
            "Commencement",
            "Baccalaureate",
            "Holoku",
            "Variety Show"
        )

        _col = []

        # Different cases for different selections
        # One selection is a different output case
        match output_selection:
            case "plus":  # title + year (ex. Holoku 2003)
                _x = f"{_titles[title_num]} {str(_first_year)}"
                for i in range(_data_range + 1):
                    _col.append(_x)
                    _first_year += 1
                    _x = f"{_titles[title_num]} {str(_first_year)}"
                return _col
            case "dash":  # year-year (ex. 1972-2010)
                _y = f"{str(_first_year)} {str(_first_year + 1)}"
                for i in range(_data_range):
                    _col.append(_y)
                    _first_year += 1
                    _y = f"{str(_first_year)} {str(_first_year + 1)}"
                return _col
            case _:
                return _col
