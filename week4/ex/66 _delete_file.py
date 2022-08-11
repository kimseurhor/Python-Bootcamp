import os
import shutil
def delete_file(filename):
    if os.path.exists(filename) and os.path.isfile(filename) or os.path.isdir(filename):

        while True:
            k = input(f"“Are you sure you want to delete {filename} ? [Y/N]”")
            if k.lower() == 'y':
                if os.path.isfile(filename):
                    os.remove(filename)
                    print(1)
                    return
                elif os.path.isdir(filename):
                    shutil.rmtree(filename)
                    return print(1)
            elif k.lower() == 'n':

                return print(0)
            else:
                print('“Invalid Option”')

    else:
        return print('File not exist')

delete_file("folder1")