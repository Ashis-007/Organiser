import sys
import os
import shutil

file_types = {
    "PDF": ["pdf"],
    "Image": ["jpg", "jpeg", "png", "gif", "svg", "ico", "tif", "tiff", "bmp", "psd"],
    "Video": ["mp4", "mkv", "3gp", "avi", "m4v", "mpg", "mpeg", "wmv"],
    "Audio": ["mp3", "wav", "wma",],
    "Document": ["doc","docx", "odt", "rtf"],
    "Spreadsheet": ["xls", "xlxs"],
    "PPT": ["ppt", "pptx"],
    "Text": ["txt"],
    "zip": ["zip", "7z", "rar"],
    "Fonts": ["ttf", "otf", "fnt", "fon"],
    "Programming" : ["js", "cpp", "java", "py", "c", "cs", "css", "html", "php"]
}

path_name = repr(sys.argv[1]) 

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