"""
Demo pathlib module
"""
from pathlib import Path

# Home
print(Path.home())

# Cwd
print(Path.cwd())

# Path objects
home = Path.home()

# Data folder (joinpath)
data_folder = Path.home().joinpath("data")
print(data_folder)
# Data folder (new way)
data_folder = Path.home() / "data"
print(data_folder)
# Data file (new way)
file = Path.home() / "data" / "output.csv"
print(file)

# output_file example
print(file.exists())   # true/false
print(file.name)       # filename
print(file.stem)       # filename without extension
print(file.suffix)     # extension
print(file.parent)     # the parent directory
print(file.resolve())  # full path

# Glob
path = Path("day4/demos/")
print(list(path.glob("*.py")))
# Recursive glob
path = Path("day4")
print(list(path.rglob("*.py")))


# Optional
# Reading & writing
text_file = Path("zen.txt")
text_file.write_text("Simple is better than complex")
print(text_file.read_text())

# With context manager
file = Path("zen.txt")
with open(file, "w") as f:
    f.write("Simple is better than complex")
