import pandas as pd
import finder
import video
import printer


# Excel exporting and data manipulation handler
class ExcelHandler(object):
    def __init__(self):
        pass

    # Turn the data into Excel file
    def excel_it(self, path, data):
        df = pd.DataFrame(data)
        df.to_excel(path, index=False, header=True)

    def export_found_to_file(self, list_, path):
        title = []
        url = []
        for i in range(len(list_)):
            title.append(list_[i][1])
            url.append(list_[i][0])
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
        data = {"school years": printer.ListMe().print_year_list(0, "dash", 1987, 2019)}
        self.excel_it(path, data)

    def export_collected_to_file(self, path, keyword):
        f = finder.FindMeOccurrences()
        data = f.match_me(keyword)
        self.excel_it(path, data)


# Ingest Excel file and transfer to panda dataframe
class IngestMe(object):
    def __init__(self):
        pass

    def from_path(self, path, sn):
        df = pd.read_excel(path, sheet_name=sn)
        return df
