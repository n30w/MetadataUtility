# QuickPrint
Automation for Digital Archives 2022, written in python. Interprets data from text files and writes to Excel file for easy copy and paste into master google sheet.

### Required dependencies
- pandas
- openpyxl
- youtube-dl
- pafy
- pytube

### Notes
I'm using the Jetbrains PyCharm IDE. Installed dependencies in the project folder's venv folder.

Since YouTube removed dislikes being shown, I edited the youtube-dl, *backend_youtube_dl.py* and commented out:

- self._likes = self._ydl_info['like_count']
- self._dislikes = self._ydl_info['dislike_count']
- self._rating = self._ydl_info['average_rating']

### Useful Links
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Pafy Documentation](https://pythonhosted.org/pafy/#)
- [Pandas DataFrame to Excel File](https://datatofish.com/export-dataframe-to-excel/)
- [Pandas Remove/Drop Columns](https://stackoverflow.com/questions/40389018/dropping-multiple-columns-from-a-data-frame-using-python)
- [Pandas DataFrame Tutorial](https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm)
- [PEP8 Style Guide](https://peps.python.org/pep-0008/#prescriptive-naming-conventions)
- [Python Regex Library](https://docs.python.org/3.10/library/re.html#match-objects)
- [Python Dictionary Update](https://www.w3schools.com/python/python_dictionaries_add.asp)
- [Python Typing Example](https://github.com/ActivityWatch/aw-core/blob/master/aw_core/models.py)
- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator)
- [Python Decorators](https://www.codingem.com/at-symbol-in-python/)
- [Class vs Static Method Tutorial](https://www.youtube.com/watch?v=BNFDOLE4Q5c)