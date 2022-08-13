import os
class FileLib:
    def inspect(self):
        obj = os.listdir()
        v = []
        for x in range(len(obj)):
            if os.path.isfile(obj[x]):
                v.append((obj[x], "file"))
                # k =  (f'({x.name}), file')
            elif os.path.isdir:
                v.append((obj[x], "folder"))
                # k = (f'({x.name}), folder')
            else:
                return
        print(v)

    def current_path(self):
        w = (os.getcwd())
        return print(str(w))

    def read(self, filename):
            f = open(filename, 'r')
            print(str(f.read()))
            f.close()

    def write(self, filename, content):

        x = open(filename, 'w')
        x.write(content)
        print("Text added")

    def append(self, filename, content):
        import datetime
        now = datetime.datetime.now()

        current_time = now.strftime("%D:%M:%Y  %H:%M:%S")
        print("Text appended")

        append = open(filename, 'a')
        append.write(f'\n[{current_time}] {content}')
    def remove(self, filename):
        os.remove(filename)
        print("File removed")

    def create_folder(self, folder_list):
        os.mkdir(folder_list)
        print("Folder created")
        # if os.path.exists(folder_list):
        #     import shutil
        #     while True:
        #         k = input(f"“Are you sure you want to {folder_list} replace ? [Y/N]”")
        #         if k.upper() == 'Y':
        #             shutil.rmtree(folder_list)
        #
        #             print(1)
        #             return os.mkdir(folder_list)
        #         elif k.upper() == 'N':
        #             print(0)
        #             return
        #         else:
        #             print('“Invalid Option”')
        #
        # else:
        #
        #     print(1)
        #     return os.mkdir(folder_li

FileLib().inspect()
FileLib().current_path()
FileLib().read('woff.txt')
FileLib().write("orange.txt", "Hello world")
FileLib().append("libappend.txt", "Welcome")
FileLib().remove("oooo.py")
FileLib().create_folder("hello")

