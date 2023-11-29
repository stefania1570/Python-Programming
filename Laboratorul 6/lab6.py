import os
import sys
# ex1
def read_files_in_directory(directory_path, file_extension):
    try:
        # Validate directory path
        if not os.path.isdir(directory_path):
            raise ValueError("Invalid directory path")

        # Iterate over files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file with the specified extension
            if os.path.isfile(file_path) and filename.endswith(file_extension):
                try:
                    # Read and print the contents of the file
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}\n{'='*30}")
                except Exception as e:
                    print(f"Error reading {filename}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Check if both directory path and file extension are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_files_in_directory(directory_path, file_extension)

#ex2

def rename_files(directory_path):
    try:
        # Check if the specified directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Get a list of all files in the directory
        files = os.listdir(directory_path)

        # Rename each file with a sequential number prefix
        for index, file_name in enumerate(files, start=1):
            old_path = os.path.join(directory_path, file_name)
            new_name = f"file{index}.{file_name.split('.')[-1]}"  # Add sequential number prefix
            new_path = os.path.join(directory_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed: {file_name} -> {new_name}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = "D:/Test"

# Call the function to rename files
rename_files(directory_path)

#ex3

def calculate_total_size(directory_path):
    total_size = 0

    try:
        # Check if the specified directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Iterate through all files in the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Get the size of the file and add it to the total size
                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Permission denied to access files in '{directory_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a directory path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
        sys.exit(1)

    # Get the directory path from the command line argument
    directory_path = sys.argv[1]

    # Call the function to calculate the total size
    calculate_total_size(directory_path)

#ex4
def count_files_by_extension(directory_path):
    try:
        # Check if the specified directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Check if the specified path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")

        # Get a list of all files in the directory
        files = os.listdir(directory_path)

        # Check if the directory is empty
        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        # Initialize a dictionary to store the counts of each file extension
        extension_counts = {}

        # Iterate through all files in the directory
        for file_name in files:
            _, file_extension = os.path.splitext(file_name)
            extension = file_extension.lower()  # Convert to lowercase to handle case-insensitivity

            # Update the count for the file extension
            extension_counts[extension] = extension_counts.get(extension, 0) + 1

        # Print the counts of each file extension
        print(f"File counts by extension in '{directory_path}':")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Permission denied to access files in '{directory_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a directory path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
        sys.exit(1)

    # Get the directory path from the command line argument
    directory_path = sys.argv[1]

    # Call the function to count files by extension
    count_files_by_extension(directory_path)
