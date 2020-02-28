import os
rootdir = 'C:/Users/03039339/Work Folders'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path=os.path.join(subdir.replace('\\','/'), file).replace('\\','/')
        size=os.stat(path).st_size
        if size>10000000:
            print(size, path)
