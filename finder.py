# Find and display get URL of YouTube videos
# Look for a YouTube video with a keyword,
# Using regex, it will find it and give you the URL
# The reason for creating this script is that the Punavision and
# Punahou website don't have the search functions enabled on the YouTube channels

from pytube import Channel
import pandas as pd
import pafy
import re
import xh


class FindMeVideo(object):
    def __init__(self):
        pass

    def _get_video_urls(self, channel):
        # Uses pytube library to get urls
        # https://pytube.io/en/latest/user/channel.html
        list_of_urls = []
        c = Channel(channel)
        for url in c.video_urls:
            list_of_urls.append(url)
            print("appending " + url)
        print("Found " + str(len(list_of_urls)) + " videos!")
        return list_of_urls

    def _get_video_titles(self, list_):
        title_list = []
        for u in list_:
            try:
                video = pafy.new(u)
                title_list.append(video.title)
                print("added " + video.title)
            except ValueError:
                print("Video Private or DNE")
                return
            except AttributeError:
                return
        return title_list

    # Returns a full list of found video names
    def full_vid_list(self, channel):
        url_list = self._get_video_urls(channel)
        titles_list = self._get_video_titles(url_list)
        found_list = []
        for i in range(len(url_list)):
            found_list.append([url_list[i], titles_list[i]])
        return found_list

    # Regex search for only a certain name or phrase of video
    def names(self, channel, field):
        url_list = self._get_video_urls(channel)
        titles_list = self._get_video_titles(url_list)
        found_list = []
        for i in range(len(field)):
            for j in range(len(titles_list)):
                match = re.search(field[i], titles_list[j], re.IGNORECASE)
                if match:
                    m = [titles_list[j], url_list[j]]
                    found_list.append(m)
        print(found_list)
        return found_list


class FindMeOccurrences(object):
    def __init__(self):
        self.x = xh.IngestMe()

        # Copy of DV Inventory sheet column names
        self.dv_names = ["Title",
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
                         "Faculty Included",
                         "Students Included"
                         ]

        # Main sheet column names
        self.main_names = ["Video Production Title",
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
                           "Names Notes",
                           ]

    # Collect relevant key terms and return to array
    def _collect_relevant(self, path, sn, col_name, keyword):
        df = self.x.from_path(path, sn)  # sn = sheet name
        collected = []
        shape = df.shape
        for i in range(shape[0]):
            row = df.iloc[i][col_name]  # accessed via [row][column]
            match = re.search(keyword, str(row), re.IGNORECASE)
            if match:
                collected.append(i)  # collected.append([i, row])
        print(str(len(collected)) + " entries found")
        return collected

    # Match DV Excel data to Main Excel document data
    def match_me(self, keyword):
        path1 = "/Users/neoalabastro/Desktop/MovingImages.xlsx"
        dv_data= {}
        main_data = {}
        df = self.x.from_path(path1, "dv")
        entry_list = self._collect_relevant(path1,
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
        df["Names Notes"] = df["Faculty Included"] + " " + df["Students Included"]
        print(df["Names Notes"])
        df.drop(columns=["Students Included", "Faculty Included"], inplace=True)
        dv_data = df.to_dict()

        # Get indices for list of the dv_data to iterate through
        keys_list = list(dv_data)
        # Populate main_data dictionary
        for i in range(len(self.main_names)):
            main_data[self.main_names[i]] = dv_data[keys_list[i]]
        return main_data
