#FIRST STEP: LIST ALL FILES RECURSIVELY FROM A FOLDER -- DONE
#1.1: PRINT HOW MANY SUBFOLDERS AND FILES THE FOLDER HAS --DONE
#SECOND STEP: GET THE EXTENSION FROM EACH FILE -- DONE 
#THIRD STEP: MAKE A DICTIONARY IN WHICH THE KEYS ARE THE EXTENSIONS AND THE VALUES ARE THE FREQUENCIES OF THE EXTENSIONS -- DONE
#3.1: CALCULATE (AND PRINT) THE PROPORTION OF EACH FILE TYPE (EACH EXTENSION) AS A NUMBER -- DONE
#3.2: + its size (for each extension what is the size occupied) -- DONE
#FOURTH STEP: MAKE THE BAR PLOT USING MATPLOTLIB -- DONE
#FIFTH STEP: EXTEND IT TO A PARTITION (pana aici testez doar pe un folder ca sa vad daca e bine ce face) -- DONE

import os
import matplotlib.pyplot as matplt

foldersNumber = 0
filesNumber = 0
extension_dict = {}
size_dict = {}

for (root, directories, files) in os.walk("D:\\"): #C:\\Users\\Stefania\\OneDrive\\Desktop\\Proiect
    foldersNumber += len(directories)
    filesNumber += len(files)

    for fullFileName in files:
        file_name, file_extension = os.path.splitext(fullFileName)
        extension_dict[file_extension] = extension_dict.get(file_extension, 0) + 1

        file_path = os.path.join(root, fullFileName)
        file_size = os.path.getsize(file_path)
        file_size_in_kb = file_size / 1024 # Convert bytes to kilobytes

        size_dict[file_extension] = size_dict.get(file_extension, 0) + file_size_in_kb 

print(f"Total number of subfolders: {foldersNumber}")
print(f"Total number of files: {filesNumber}")

print("\nExtension frequencies and proportions:")
for extension, frequency in extension_dict.items():
    proportion = (frequency / filesNumber) * 100
    print(f"{extension}: {frequency} files ({proportion:.2f}% of total)")

print("\nExtension sizes:")
for extension, size in size_dict.items():
    print(f"{extension}: {size:.2f} KB")

# Extensions Frequency Bar Plot
frequency_labels = list(extension_dict.keys())
frequency_values = list(extension_dict.values())

matplt.figure(figsize=(10, 6))
matplt.bar(frequency_labels, frequency_values, color ='maroon', width = 0.6)
matplt.xlabel('File Type')
matplt.ylabel('Frequency')
matplt.title('File Type Frequencies')
matplt.xticks(rotation=60, ha='right')  # rotim etichetele de pe axa ox ca sa se vada mai bine
matplt.show()

# Extension sizes
size_labels = list(size_dict.keys())
size_values = list(size_dict.values())

# Plotting the bar chart for extension sizes
matplt.figure(figsize=(10, 6))
matplt.bar(size_labels, size_values, color ='maroon', width = 0.6)
matplt.xlabel('File Extension')
matplt.ylabel('Size (KB)')
matplt.title('File Extension Sizes')
matplt.xticks(rotation=60, ha='right')  # rotim etichetele de pe axa ox ca sa se vada mai bine
matplt.show()