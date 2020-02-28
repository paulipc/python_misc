import os
rootdir = 'C:/Users/03039339/Work Folders'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path=os.path.join(subdir.replace('\\','/'), file).replace('\\','/')
        size=int(os.stat(path).st_size/1000000)
        if size>10:
            print(str(size)+';'+path)
