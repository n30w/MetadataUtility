# classes to handle excel sorting of two files: Main and DV
import pafy
import math


# Populate data functions

class VidHandler(object):
    def _get_video_timecode(self, url):
        try:
            video = pafy.new(url)
        except ValueError:
            return "Have Video, not posted"
        except:
            return "PRIVATE VIDEO"
        else:
            len_seconds = video.length
            finals = []
            timecode = ""

            # Math calculations for timecode
            # Calculation from: https://www.inchcalculator.com/seconds-to-time-calculator/
            hour = math.floor(len_seconds / 3600)
            finals.append(str(hour))
            mins = math.floor(((len_seconds / 3600) - hour) * 60)
            finals.append(str(mins))
            secs = math.floor(((((len_seconds / 3600) - hour) * 60) - mins) * 60)
            finals.append(str(secs))

            # Populate array for timecode displaying
            for i in range(3):
                if int(finals[i]) < 10:  # Add zero before number if less than 10
                    finals[i] = "0" + str(finals[i])
                timecode += finals[i] + ":"

            # [:-1] removes trailing colon
            return timecode[:-1]

    # Opens links.txt file to read and returns list video timecodes
    # respect_order boolean to print out timecodes in respected order from original file, or not
    def return_vid_timecode_list(self, path, respect_order):
        timecodes = []
        i = 0
        with open(path) as file_in:
            for line in file_in:
                li = self._get_video_timecode(line)
                if not respect_order:
                    timecodes.insert(0, li)
                    print(str(i + 1) + ". " + timecodes[0] + " written")
                else:
                    timecodes.append(li)
                    print(str(i + 1) + ". " + timecodes[i] + " written")
                i += 1
        return timecodes
