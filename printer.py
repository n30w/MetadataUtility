# Printer class for general printing of Excel sheets

class ListMe(object):
    # Title Numbers
    # 1. Commencement
    # 2. Baccalaureate
    # 3. Holoku
    # 4. Variety Show
    def print_year_list(self, title_num, output_selection, first_year, last_year):
        __first_year = first_year
        __data_range = last_year - __first_year
        __string_to_append = ""
        __titles = (
            "Commencement",
            "Baccalaureate",
            "Holoku",
            "Variety Show"
        )

        __col = []

        # Different cases for different selections
        # One selection is a different output case
        match output_selection:
            case "plus":  # title + year (ex. Holoku 2003)
                __x = f"{__titles[title_num]} {str(__first_year)}"
                for i in range(__data_range + 1):
                    __col.append(__x)
                    __first_year += 1
                    __x = f"{__titles[title_num]} {str(__first_year)}"
                return __col
            case "dash":  # year-year (ex. 1972-2010)
                __y = f"{str(__first_year)} {str(__first_year + 1)}"
                for i in range(__data_range):
                    __col.append(__y)
                    __first_year += 1
                    __y = f"{str(__first_year)} {str(__first_year + 1)}"
                return __col
            case _:
                return __col
