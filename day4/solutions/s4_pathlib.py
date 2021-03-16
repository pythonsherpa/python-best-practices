"""
Exercise 1
Import the 'pathlib' module and try out the different
methods described in:
https://docs.python.org/3/library/pathlib.html#methods
What does .with_stem(stem) do?

# Exercise 2
Replace the actions in the code snippet below with the pathlib module.
Docs: https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module
"""

# Exercise 1
from pathlib import Path
print(Path.cwd())
print(Path.home())
...  # etc

# .with_stem() changes the name of the file without
# changing the extension or the location
file = Path('C:/Downloads/draft.txt')
print(file.with_stem('final'))  # prints C:/Downloads/final.txt


# Exercise 2
import os
os.mkdir("exercise_mkdir")
print(os.path.exists("exercise_mkdir"))

# With 'pathlib' instead of 'os'
p = Path("exercise_mkdir")
p.mkdir(exist_ok=True)  # notice the `exist_ok` argument, very useful!
print(p.exists())
