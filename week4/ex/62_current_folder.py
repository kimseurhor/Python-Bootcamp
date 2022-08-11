import os
def current_folder():

    obj = os.listdir()
    v = []
    for x in range (len(obj)):
        if os.path.isfile(obj[x]):
            v.append((obj[x], "file"))
            # k =  (f'({x.name}), file')
        else:
            v.append((obj[x], "folder"))
            # k = (f'({x.name}), folder')
    print(v)


current_folder()