# QuickPrint
Automation for Digital Archives 2022, written in python. Interpretes data from text files and writes to excel file for easy copy and paste into master google sheet.

### Required dependencies
<li>Pandas</li>
<li>openpyxl</li>
<li>youtube-dl</li>

### Notes
I'm using the Jetbrains PyCharm IDE. Installed dependencies in the project folder's venv folder.

Since Youtube removed dislikes being shown, I edited the youtube-dl, *backend_youtube_dl.py* and commented out

self._likes = self._ydl_info['like_count']

self._dislikes = self._ydl_info['dislike_count']

self._rating = self._ydl_info['average_rating']