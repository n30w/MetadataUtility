import pandas as pd
import video
import printer


# Excel exporting and data manipulation handler
class ExcelHandler(object):
    def __init__(self):
        pass

    # Turn the data into excel file
    def excel_it(self, path, data):
        df = pd.DataFrame(data)
        df.to_excel(path, index=False, header=True)

    def export_found_to_file(self, list_, path):
        title = []
        url = []
        for i in range(len(list_)):
            title.append(list_[i][0])
            url.append(list_[i][1])
        data = {"title": title,
                "url": url
                }
        # data = {col_name: lists}
        self.excel_it(path, data)

    def export_timecode_to_file(self, path):
        timecodes = video.VidHandler().return_vid_timecode_list("/Users/neoalabastro/Desktop/links.txt", False)
        data = {"timecodes": timecodes}
        self.excel_it(path, data)

    def export_printer_to_file(self, path):
        data = {"school years": printer.ListMe().print_year_list(0, "dash", 1973, 2010)}
        self.excel_it(path, data)


class IngestMe(object):
    pass
