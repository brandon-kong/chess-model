import os
import zipfile

def extract_zip(zip_file, dest_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

def create_zip(zip_file, source_dir):
    with zipfile.ZipFile(zip_file, 'w') as zip_ref:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zip_ref.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

