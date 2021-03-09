from scale_zip_7 import ScaleZip
from zip_replace_7 import ZipReplace

# --------
# ScaleZip
# --------
archive_name = input("Enter arcvive name: ")
width = input("Input width: ")
height = input("Input height: ")

if height.isdigit() and width.isdigit():
    width = int(width) # 140-7680
    height = int(height) # 192-4800

    if width in range(140, 7681) and height in range(192, 4801):
        ScaleZip(archive_name, width, height).process_zip()
        #ScaleZip("lab4_1.zip", 1024, 768).process_zip()
        print("Successfully converted.")
    else:
        print("Height must be in range from 192 to 4800 and width must be from 140 to 7680.")
else:
    print("Input proper value!")


# ----------
# ZipReplace
# ----------
archive_name = input("Name of archive: ") # 'text.zip'
file_name = input("Name of file which you want to change: ") # 'text.txt'
what_to_change = input("Text, which you want to change: ") # 'dogs'
replacement = input("Change text to this: ") # 'cats'
# 'text.zip' -> 'text.txt' -> 'dogs' -> 'cats'

try:
    ZipReplace(archive_name, file_name, what_to_change, replacement).zip_find_replace()
    # ZipReplace('text.zip', 'text.txt', 'dogs', 'cats').zip_find_replace()
    print("Successfully changed.")
except Exception:
    print("There are some problems with your input. Try again.")
