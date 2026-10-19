import os
import shutil

folder_path = r"FOLDER PATH HERE"  # Replace with the path to your folder

file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
}

for file in os.listdir(folder_path):
    filename, ext = os.path.splitext(file)
    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            category_path = os.path.join(folder_path, category)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(
                os.path.join(folder_path, file),
                os.path.join(category_path, file),
            )