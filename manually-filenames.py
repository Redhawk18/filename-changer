import os
from pathlib import Path

print("Paste the ABSOLUTE PATH")
print("For windows users it starts with a letter then a colon")
dir = Path(input())

if not os.path.exists(dir):
    print("directory does not exist, exiting...")
    exit()

files = []

# load all files in working dir into program
for file in dir.rglob("*"):
    files.append(file)

files.sort()

for i, file in enumerate(files):
    file_name_parts = file.name.split("Total Drama")
    new_filename = f"S01E{i + 1:02}" + " Total Drama" + file_name_parts[1]

    new_absolute_path = file.parent.joinpath(new_filename)
    # print(new_filename)

    file.rename(new_absolute_path)
