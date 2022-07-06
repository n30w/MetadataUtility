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
    except:
        return "PRIVATE VIDEO"
    else:
        lenSeconds = video.length
        finals = []
        timecode = ""

        # Math calculations for timecode
        hour = math.floor(lenSeconds / 3600)
        finals.append(str(hour))
        min = math.floor(((lenSeconds/3600) - hour) * 60)
        finals.append(str(min))
        sec = math.floor(((((lenSeconds/3600) - hour) * 60) - min) * 60)
        finals.append(str(sec))

        # Populate array for timecode displaying
        for i in range(3):
            if int(finals[i]) < 10:
                finals[i] = "0"+str(finals[i])
            timecode += finals[i]+":"

        # [:-1] removes trailing colon
        return timecode[:-1]

# Opens links.txt file to read and returns list video timecodes
def createVidLengthList():
    timecodes = []
    f = "/Users/neoalabastro/Desktop/links.txt"
    with open(f) as file_in:
        for line in file_in:
            timecodes.insert(0, getVidLength(line))
            print(timecodes[0])
    return timecodes


if __name__ == '__main__':
    # printXlsx()
    printVidLength("Length", createVidLengthList())
    x = "Commencement"
    y = 1973
    # z = str(x)+"-"+str(x+1)
    # printNums(x, 2019 - y, y)
