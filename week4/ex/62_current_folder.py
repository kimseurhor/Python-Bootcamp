import os
def current_folder():

    obj = os.listdir()
    v = []
    for x in range (len(obj)):
        if os.path.isfile(obj[x]):
            v.append((obj[x], "file"))
            # k =  (f'({x.name}), file')
        elif os.path.isdir:
            v.append((obj[x], "folder"))
            # k = (f'({x.name}), folder')
        else:
            return v
    print(v)


current_folder()