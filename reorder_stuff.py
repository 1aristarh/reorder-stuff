import os
import shutil

switch = {
    'txt': 'text',
    'pdf': 'pdf',
    'jpg': 'image',
    'jpeg': 'image',
    'png': 'image',
    'gif': 'image',
    'mp3': 'audio',
    'wav': 'audio',
    'mp4': 'video',
    'avi': 'video',
    'mkv': 'video',
    'zip': 'compressed',
    'rar': 'compressed',
    'tar': 'compressed',
    'exe': 'executable',
    'msi': 'executable',
    'apk': 'executable',
    'doc': 'document',
    'docx': 'document',
    'ppt': 'presentation',
    'pptx': 'presentation',
    'xls': 'spreadsheet',
    'xlsx': 'spreadsheet'
}

def reorder_stuff():
    print("Starting to reorder files...")  # Debug statement
    for file in os.listdir():
        print(f"Found: {file}")  # Debug statement
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            print(f"Processing file: {file}, extension: {extension}")  # Debug statement
            if extension in switch:
                folder = switch[extension]
                if not os.path.exists(folder):
                    os.mkdir(folder)
                    print(f"Created folder: {folder}")  # Debug statement
                shutil.move(file, folder)
                print(f"Moved {file} to {folder}")  # Debug statement
            else:
                if not os.path.exists('others'):
                    os.mkdir('others')
                    print(f"Created folder: others")  # Debug statement
                shutil.move(file, 'others')
                print(f"Moved {file} to others")  # Debug statement
        elif os.path.isdir(file):
            os.chdir(file)
            reorder_stuff()
            os.chdir('..')
    print("Reordering complete.")  # Debug statement

# Call the function to start processing
if __name__ == "__main__":
    reorder_stuff()
