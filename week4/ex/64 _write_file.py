import os.path
def write_file(filename, content):

    if os.path.exists(filename):
        while True:
            k = input(f"“Are you sure you want {filename} to replace ? [Y/N]”")
            if k.lower() == 'y':
                x = open(filename, 'w')
                print(1)
                return x.write(content)

            elif k.lower() == 'n':
                return print(0)
            else:
                print('“Invalid Option”')
    else:
        x = open(filename, 'w')
        print(1)
        return x.write(content)

write_file('woff.txt', 'Meow')