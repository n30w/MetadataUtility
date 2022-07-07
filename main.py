import pandas as pd
import pafy
import youtube_dl
import math

# dr = datarange
# fy = first year
# st = string to append
def populateData(dr, fy, st):
    firstYear = fy
    col = []
    for i in range(dr):
        col.append(st)
        firstYear += 1
    return col

def printNums(name, dr, fy):
    firstYear = fy
    col = []
    x = "Commencement " + str(firstYear)
    y = str(firstYear)+"-"+str(firstYear+1)
    for i in range(dr):
        col.append(y)
        firstYear += 1
        y = str(firstYear) + "-" + str(firstYear + 1)

    FILEPATH = r"/Users/neoalabastro/Desktop/printer.xlsx"
    data = {name: col}
    df = pd.DataFrame(data, columns=[name])
    print(df)
    df.to_excel(FILEPATH, index=False, header=True)

def printVidLength(colName, fx):
    FILEPATH = r"/Users/neoalabastro/Desktop/data.xlsx"
    data = {colName: fx}
    df = pd.DataFrame(data, columns=[colName])
    df.to_excel(FILEPATH, index=False, header=True)

def getVidLength(url):
    try:
        video = pafy.new(url)
    except ValueError:
        return "Have Video, not posted"
    except:
        return "PRIVATE VIDEO"
    else:
        lenSeconds = video.length
        finals = []
        timecode = ""

        # Math calculations for timecode
        # Calculation from: https://www.inchcalculator.com/seconds-to-time-calculator/
        hour = math.floor(lenSeconds / 3600)
        finals.append(str(hour))
        min = math.floor(((lenSeconds/3600) - hour) * 60)
        finals.append(str(min))
        sec = math.floor(((((lenSeconds/3600) - hour) * 60) - min) * 60)
        finals.append(str(sec))

        # Populate array for timecode displaying
        for i in range(3):
            if int(finals[i]) < 10: # Add zero before number if less than 10
                finals[i] = "0"+str(finals[i])
            timecode += finals[i]+":"

        # [:-1] removes trailing colon
        return timecode[:-1]

# Opens links.txt file to read and returns list video timecodes
# Reverse order boolean to print out timecodes in reverse order or not
def createVidLengthList(reverseOrder):
    timecodes = []
    f = "/Users/neoalabastro/Desktop/links.txt"
    i = 0
    with open(f) as file_in:
        for line in file_in:
            li = getVidLength(line)
            if reverseOrder:
                timecodes.insert(0, li)
                print(str(i+1) + ". " +timecodes[0]+" written")
            else:
                timecodes.append(li)
                print(str(i+1) + ". " +timecodes[i]+" written")
            i += 1
    return timecodes


if __name__ == '__main__':
    #reverseOrder = True
    #printVidLength("Length", createVidLengthList(reverseOrder))
    printNums("sy", 2019-1970, 1971)
