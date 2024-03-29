# Find and display get URL of YouTube videos
# Look for a YouTube video with a keyword,
# Using regex, it will find it and give you the URL
# The reason for creating this script is that the Punavision and
# Punahou website don't have the search functions enabled on the YouTube channels
import pandas
from pytube import Channel
import pandas as pd
import pafy
import re
import xh
import os


class FindMeFilePaths(object):
    def __int__(self):
        pass

    # get path locations from paths.txt file in main directory
    @staticmethod
    def get_paths() -> dict:
        # List of file directories
        file_dirs: list[str] = []
        # Initialize path variable
        path: str

        # check if path file exists, if not create it
        try:
            path = os.getcwd() + "/paths.txt"
        except FileNotFoundError:
            f = open("paths.txt", "w")
            path = os.getcwd() + "/paths.txt"

        with open(path) as file_in:
            for line in file_in:
                file_dirs.append(line)

        # Rather inefficient but that's okay, I guess
        # The [:-1] is to remove trailing \n
        file_dict: dict[str, str] = {
            "links": file_dirs[0][:-1],
            "MovingImages": file_dirs[1][:-1],
            "Desktop": file_dirs[2]
        }

        return file_dict


class FindMeVideo(object):
    def __init__(self):
        pass

    # Returns a full list of found video names
    def full_vid_list(self, channel: str) -> list:
        url_list: list[str] = self._get_video_urls(channel)
        titles_list: list[str] = self._get_video_titles(url_list)
        found_list: list[list[str]] = []
        for i in range(len(url_list)):
            found_list.append([url_list[i], titles_list[i]])
        return found_list

    # Regex search for only a certain name or phrase of video title
    def find_from_channel(self, channel: str, field: list) -> list:
        url_list = self._get_video_urls(channel)
        titles_list = self._get_video_titles(url_list)
        found_list: list[list[str]] = []

        for i in range(len(field)):
            for j in range(len(titles_list)):
                match: object = re.search(field[i], titles_list[j], re.IGNORECASE)
                if match:
                    m: list[str] = [titles_list[j], url_list[j]]
                    found_list.append(m)

        print(found_list)
        return found_list

    # Path is path to Excel file, sn is sheet name, field are the search terms
    @staticmethod
    def find_from_excel(path: str, sn: str, field: list) -> list:
        found_list: list[list[str]] = []
        excel_rows: pandas.DataFrame = xh.IngestMe().from_path(path, sn)
        for i in range(len(field)):
            for j in range(len(excel_rows)):
                match: object = re.search(field[i], excel_rows.iloc[j][0], re.IGNORECASE)
                if match:
                    print(f"matched: {match}!")
                    m: list[str] = [excel_rows.iloc[j][1], excel_rows.iloc[j][0]]
                    found_list.append(m)
        print(found_list)
        return found_list

    # Return list of video URLs via input of a Channel URL
    @staticmethod
    def _get_video_urls(channel_url: str) -> list:
        # Uses pytube library to get urls
        # https://pytube.io/en/latest/user/channel.html
        list_of_urls: list[str] = []
        c = Channel(channel_url)

        for url in c.video_urls:
            list_of_urls.append(url)
            print(f"appending {url}")
        print(f"Found {str(len(list_of_urls))} videos!")

        return list_of_urls

    # Return list of video titles via input of a list of URLs
    @staticmethod
    def _get_video_titles(list_: list[str]) -> list | None:
        title_list: list[str] = []
        for u in list_:
            try:
                vt = pafy.new(u).title  # Video title
                title_list.append(vt)
                print(f"added {vt}")
            except ValueError:
                print("Video Private or DNE")
                return
            except AttributeError:
                return
        return title_list


class FindMeOccurrences(object):
    def __init__(self):
        self.x = xh.IngestMe()

        # Copy of DV Inventory sheet column names
        self.dv_names = [
            "Title",
            "Date of Event",
            "Class Years",
            "Grades",
            "Director",
            "Location",
            "Length (TRT) (HH:MM:SS)",
            "Original Format",
            "Physical Format",
            "Transfer Notes",
            "Notes",
            "DV Number",
            "Faculty Included",
            "Students Included"
        ]

        # Main sheet column names
        self.main_names = [
            "Video Production Title",
            "Date",
            "Class Year",
            "Grade",
            "Contributor(s)",
            "Punahou Location",
            "Video Length (##:##:##)",
            "Original Format Type",
            "Derivative Format Type",
            "Transfer Notes",
            "General Notes",
            "Original Digital ID",
            "Names Notes",
        ]

    # Collect relevant key terms and return to array
    def _collect_relevant(
            self,
            path: str,
            sn: str,
            col_name: str,
            keyword: str
    ) -> list:
        df = self.x.from_path(path, sn)  # sn = sheet name
        collected = []
        for i in range(df.shape[0]):
            row = df.iloc[i][col_name]  # accessed via [row][column]
            match = re.search(keyword, str(row), re.IGNORECASE)
            if match:
                collected.append(i)  # collected.append([i, row])

        print(f"{str(len(collected))} entries of \"{keyword}\" found")

        if len(collected) == 0:
            return

        return collected

    # Match DV Excel data to Main Excel document data
    def match_me(self, keyword: str) -> dict:
        p: dict[str, str] = FindMeFilePaths().get_paths()
        path1: str = p["MovingImages"]
        dv_data: dict[str, list] = {}
        main_data: dict[str, list] = {}
        df = self.x.from_path(path1, "dv")
        entry_list = self._collect_relevant(
            path1,
            "dv",
            "Title",
            keyword
        )

        # First for loop is to access each column
        for i in range(len(self.dv_names)):
            dv_data[self.dv_names[i]] = []
            # Second for loop is for each row
            for j in range(len(entry_list)):
                # Access and store column data
                f = df[self.dv_names[i]][entry_list[j]]
                dv_data[self.dv_names[i]].append(f)

        # Combine Students Included and Faculty Included
        df = pd.DataFrame(dv_data)
        for i in range(df.shape[0]):
            if not df.iloc[i]["Students Included"] == "":
                df["Names Notes"] = df["Faculty Included"].astype(str) + "; " + df["Students Included"].astype(str)
            else:
                df["Names Notes"] = df["Faculty Included"]

        df.drop(columns=["Students Included", "Faculty Included"], inplace=True)

        for i in range(df.shape[0]):
            x = str(df.iloc[i]["Names Notes"])
            if not x == "nan":
                for j in range(len(x)):
                    x = x.replace(",", ";")
            else:
                continue
            df.iloc[i]["Names Notes"] = x

        dv_data: dict[str, list] = df.to_dict()

        # Get indices for list of the dv_data to iterate through
        keys_list: list = list(dv_data)
        # Populate main_data dictionary
        for i in range(len(self.main_names)):
            main_data[self.main_names[i]] = dv_data[keys_list[i]]
        return main_data
