import datetime
now = datetime.datetime.now()

current_time = now.strftime("%D:%M:%Y  %H:%M:%S")
def append_file(file):
    while True:
        x = input("$:")
        if x == 'EXIT':
            break

        else:
            append = open(file, 'a')
            append.write(f'\n[{current_time}] {x}')



append_file("Append.txt")