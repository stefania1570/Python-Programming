#FIRST STEP: LIST ALL FILES RECURSIVELY FROM A FOLDER -- DONE
#1.1: PRINT HOW MANY SUBFOLDERS AND FILES THE FOLDER HAS --DONE
#SECOND STEP: GET THE EXTENSION FROM EACH FILE -- DONE 
#THIRD STEP: MAKE A DICTIONARY IN WHICH THE KEYS ARE THE EXTENSIONS AND THE VALUES ARE THE FREQUENCIES OF THE EXTENSIONS -- DONE
#3.1: CALCULATE (AND PRINT) THE PROPORTION OF EACH FILE TYPE (EACH EXTENSION) AS A NUMBER -- DONE
#3.2: + its size (for each extension what is the size occupied) -- DONE
#FOURTH STEP: MAKE THE BAR PLOT USING MATPLOTLIB
#FIFTH STEP: EXTEND IT TO A PARTITION (pana aici testez doar pe un folder ca sa vad daca e bine ce face)

import os

foldersNumber = 0
filesNumber = 0
extension_dict = {}
size_dict = {}

for (root, directories, files) in os.walk("C:\\Users\\Stefania\\OneDrive\\Desktop\\Proiect"):
    foldersNumber += len(directories)
    filesNumber += len(files)

    for fullFileName in files:
        file_name, file_extension = os.path.splitext(fullFileName)
        extension_dict[file_extension] = extension_dict.get(file_extension, 0) + 1

        file_path = os.path.join(root, fullFileName)
        file_size = os.path.getsize(file_path)

        size_dict[file_extension] = size_dict.get(file_extension, 0) + file_size

print(f"Total number of subfolders: {foldersNumber}")
print(f"Total number of files: {filesNumber}")

print("\nExtension frequencies and proportions:")
for extension, frequency in extension_dict.items():
    proportion = (frequency / filesNumber) * 100
    print(f"{extension}: {frequency} file(s) ({proportion:.2f}% of total)")

print("\nExtension sizes:")
for extension, size in size_dict.items():
    size_in_kb = size / 1024  # Convert bytes to kilobytes
    print(f"{extension}: {size_in_kb:.2f} KB")
