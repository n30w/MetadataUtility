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
- [Python venv tutorial](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html)
- [Switching Terminal Between i386 and ARM](https://vineethbharadwaj.medium.com/m1-mac-switching-terminal-between-x86-64-and-arm64-e45f324184d9)

## Note About INTEL and ARM support
Support for intel and arm is weird. To get this to work in pycharm or even run this with the needed dependencies for this project, one must first open terminal, go to the venv bin directory of this project then type:

> env /usr/bin/arch -x86_64 /bin/zsh/
> conda deactivate
> source $(pwd)/activate
> python3 (path to main.py)

## Using anaconda venv to run this on M1 architecture
I used anaconda package manager to solve the issue of M1 problems regarding the system architecture, x86_64 and arm64. I installed *anaconda* and *miniforge*. I first installed anaconda-navigator, then installed miniforge via brew install miniforge. I then ran the command:

> conda create --name (name of environment) python=3.10
> conda activate (name of environment)
> conda install (package name)

Now that the conda venv is activated, you can then use pip3 to install pip3 packages like pafy, youtube_dl, or pytube. I used this new environment for the Python project.

### Note about JetBrains PyCharm IDE environment interpreter
To add the anconda environment, I went ot my project interpreter settings at the bottom right, and clicked add interpreter. I added a new conda environment, selected existing environment, and set the interpreter path to:

> /Users/(username)/opt/anaconda3/envs/(environment name)/bin/python

The environment name is the one created in the previous section, using the *conda create --name* command. I set the conda executable path to:

> /Users/(username)/opt/anaconda3/bin/conda

After adding, PyCharm should run the main.py flawlessly. 