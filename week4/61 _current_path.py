import os
def current_path():
    w = (os.getcwd())
    return str(w)
print(f'Current path: {current_path()}')
