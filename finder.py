# Find and display get URL of YouTube videos
# Look for a YouTube video with a keyword,
# Using regex, it will find it and give you the URL
# The reason for creating this script is that the Punavision and
# Punahou website don't have the search functions enabled on the YouTube channels

from pytube import Channel
import pafy
import re


# Cooke, Librarians, Library, Learning Commons, Books, Reading, Campus

class FindMe(object):
    def __init__(self):
        pass

    def __get_video_urls(self):
        # Uses pytube library to get urls
        # https://pytube.io/en/latest/user/channel.html
        list_of_urls = []
        c = Channel("https://www.youtube.com/user/punavision/videos")
        for url in c.video_urls:
            list_of_urls.append(url)
            print("appending " + url)
        return list_of_urls

    def __get_video_titles(self, list_):
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

    # returns a full list of found video names
    def full_list(self):
        url_list = self.__get_video_urls()
        titles_list = self.__get_video_titles(url_list)
        found_list = []
        for i in range(len(url_list)):
            found_list.append([url_list[i], titles_list[i]])
        return found_list

    # Regex search for only a certain name or phrase of video
    def names(self, field):
        url_list = self.__get_video_urls()
        titles_list = self.__get_video_titles(url_list)
        found_list = []
        for i in range(len(field)):
            for j in range(len(titles_list)):
                match = re.search(field[i], titles_list[j])
                if match:
                    m = [titles_list[j], url_list[j]]
                    found_list.append(m)
        print(found_list)
        return found_list
