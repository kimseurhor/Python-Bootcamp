def search_in_tuple(list, search):
    if search in list:
        print("Element found at index", list.index(search))
    else:
        print("Element not found in the tuple")
search_in_tuple((20,15,10,30),10)
