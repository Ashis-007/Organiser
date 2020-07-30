import sys
import os
import shutil

file_types = {
    "pdf": ["pdf"],
    "Image": ["jpg", "jpeg", "png", "gif", "svg"],
    "Video": ["mp4", "mkv"],
    "Audio": ["mp3"],
    "Document": ["doc","docx"],
    "Spreadsheet": ["xls", "xlxs"],
    "ppt": ["ppt", "pptx"],
    "Text": ["txt"],
    "zip": ["zip"]
}

path_name = repr(sys.argv[1]) 
print(path_name)

for file in os.listdir(path_name):
    file_name = file.lower()
    file_format = file_name.split(".")[-1]

    for category in file_types:
        if file_format in file_types[category]:
            if not os.path.exists(f"{path_name}\\{category}"):
                os.mkdir(f"{path_name}\\{category}")
        
            src = f"{path_name}\\{file}"
            dest = f"{path_name}\\{category}"
            shutil.move(src, dest)