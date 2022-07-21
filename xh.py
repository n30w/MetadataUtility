import pandas
import pandas as pd
import finder
import video
import printer


# Excel exporting and data manipulation handler
class ExcelHandler(object):
    def __init__(self):
        pass

    def export_found_to_file(self, list_: list, path: str) -> None:
        title: list[str] = []
        url: list[str] = []

        for i in range(len(list_)):
            title.append(list_[i][1])
            url.append(list_[i][0])

        data: dict[str, list] = {
            "title": title,
            "url": url
        }
        # data = {col_name: lists}
        self._excel_it(path, data)

    def export_timecode_to_file(self, path: str, respect_order: bool) -> None:
        p: dict = finder.FindMeFilePaths().get_paths()
        timecodes: list = video.VidHandler().return_vid_timecode_list(p["links"], respect_order)
        data: dict[str, list] = {"timecodes": timecodes}
        self._excel_it(path, data)

    def export_printer_to_file(self, path: str) -> None:
        data: dict[str, list] = {
            "school years": printer.ListMe().print_year_list(0, "dash", 1987, 2019)
        }
        self._excel_it(path, data)

    def export_collected_to_file(self, path: str, keyword: str) -> None:
        f = finder.FindMeOccurrences()
        data: dict[str, list] = f.match_me(keyword)
        self._excel_it(path, data)

    # Turn the DataFrame into Excel file
    @staticmethod
    def _excel_it(path: str, data: dict) -> None:
        df = pd.DataFrame(data)
        df.to_excel(path, index=False, header=True)


# Ingest Excel file and transfer to panda dataframe
class IngestMe(object):
    def __init__(self):
        pass

    @staticmethod
    def from_path(path: str, sn: str) -> pandas.DataFrame:
        df = pd.read_excel(path, sheet_name=sn)
        return df
