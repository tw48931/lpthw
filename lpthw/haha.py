#-*- coding:gbk -*-          
import codecs
import os
import shutil
path1 = 'C:'
path2 = 'C:'
def dirlist(path):
    filelist =  os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if filepath.endswith('.docx'):
                name = filepath.split('\\')[-1]
                print name
                shutil.copyfile(filepath, path2 + name.replace('.docx','.doc'))

dirlist(path1)