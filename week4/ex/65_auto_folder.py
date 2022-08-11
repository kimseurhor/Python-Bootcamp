import os
import shutil
def auto_folder(name):
    if os.path.exists(name):
        while True:
            k = input(f"“Are you sure you want to {name} replace ? [Y/N]”")
            if k.upper() == 'Y':
                shutil.rmtree(name)

                print(1)
                return os.mkdir(name)
            elif k.upper() == 'N':
                print(0)
                return
            else:
                print('“Invalid Option”')

    else:

        print(1)
        return os.mkdir(name)

auto_folder('Sharkyi')
