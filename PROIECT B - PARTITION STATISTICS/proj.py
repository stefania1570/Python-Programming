#FIRST STEP: LIST ALL FILES RECURSIVELY FROM A FOLDER -- DONE
#1.1: PRINT HOW MANY SUBFOLDERS AND FILES THE FOLDER HAS --DONE
#SECOND STEP: GET THE EXTENSION FROM EACH FILE -- DONE 
#THIRD STEP: MAKE A DICTIONARY IN WHICH THE KEYS ARE THE EXTENSIONS AND THE VALUES ARE THE FREQUENCIES OF THE EXTENSIONS
#3.1: CALCULATE (AND PRINT) THE PROPORTION OF EACH FILE TYPE (EACH EXTENSION) AS A NUMBER + its size (for each extension what is the size occupied)
#FOURTH STEP: MAKE THE BAR PLOT USING MATPLOTLIB
#FIFTH STEP: EXTEND IT TO A PARTITION (pana aici testez doar pe un folder ca sa vad daca e bine ce face)

import os
foldersNumber = 0
filesNumber = 0

for (root,directories,files) in os.walk("C:\\Users\\Stefania\\OneDrive\\Desktop\\Proiect"):
    foldersNumber += len(directories)
    filesNumber += len(files)

    for fullFileName in files:
        file_name, file_extension = os.path.splitext(fullFileName) #extragem extensia fisierului
        print(file_extension)

print(f"Total number of subfolders: {foldersNumber}")
print(f"Total number of files: {filesNumber}")