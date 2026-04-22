# Task 3: automate a task

import os
import shutil

try:
    source_folder = input("Enter folder path: ").strip()

    if not os.path.exists(source_folder):
        raise FileNotFoundError("Folder does not exist")

    if not os.path.isdir(source_folder):
        raise NotADirectoryError("Given path is not a folder")

    file_types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    for file in os.listdir(source_folder):
        try:
            file_path = os.path.join(source_folder, file)

            if os.path.isfile(file_path):
                moved = False

                for folder, extensions in file_types.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        target_folder = os.path.join(source_folder, folder)

                        os.makedirs(target_folder, exist_ok=True)

                        shutil.move(file_path, os.path.join(target_folder, file))
                        moved = True
                        break

                if not moved:
                    target_folder = os.path.join(source_folder, "Others")
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))

        except PermissionError:
            print(f"Permission denied: {file}")

        except shutil.Error:
            print(f"File already exists or cannot move: {file}")

        except Exception as e:
            print(f"Error processing file {file}: {e}")

    print("Files organized successfully!")

except FileNotFoundError:
    print("Folder not found. Please enter a valid path.")

except NotADirectoryError:
    print("The path is not a folder.")

except PermissionError:
    print("Permission denied. Try running as administrator.")

except Exception as e:
    print(f"Unexpected error: {e}")