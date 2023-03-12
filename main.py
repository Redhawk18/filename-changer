import os
from pathlib import Path

print("Paste the ABSOLUTE PATH")
print("For windows users it starts with a letter then a colon")
dir = Path(input())

if not os.path.exists(dir):
    print("directory does not exist, exiting...")
    exit()

roms = []
bad_words = (
    "(nsw2u)", "(nsw2u.com)", "(nsw2u.xyz)", "Switch-xci.com"
)

#load all files in working dir into program
for file in dir.rglob("*"):
    roms.append(file)

for rom in roms:
    for bad_word in bad_words:
        if bad_word in rom.name:
            #split it, combine fragmented pieces
            file_name_parts = rom.name.split(bad_word)
            new_filename = file_name_parts[0] + file_name_parts[1]

            new_absolute_path = rom.parent.joinpath(new_filename)

            rom.rename(new_absolute_path)
