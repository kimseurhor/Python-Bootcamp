def read_file(y):
    try:
        f = open(y, 'r')
        print(str(f.read()))
        f.close()
    except:
        print("‘Invalid FILENAME’")

read_file('woff.txt')