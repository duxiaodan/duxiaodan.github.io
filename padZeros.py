import os
import glob
from pathlib import Path

# for file_path in Path('./').glob('**/*.jpg'):
#     # print(file_path)
#     strpath = str(file_path)
#     newpath = strpath[:-5]+'00'+strpath[-5:]
#     os.rename(file_path,newpath)

for file_path in Path('./').glob('**/*.png'):
    # print(file_path)
    strpath = str(file_path)
    newpath = strpath[:-5]+'00'+strpath[-5:]
    os.rename(file_path,newpath)