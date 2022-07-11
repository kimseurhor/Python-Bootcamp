paragraph = str(input("Please input a paragraph:"))
search = str(input("Please input a Search String:"))
count = paragraph.count(search)
print(f"There are {count} occurrences")
meow= str(input("Do you want to replace the text[Y/N]"))

if meow== 'Y' and 'y':
    change = str(input("Please input a replacement string:"))
    numchange = int(input("How many words would you want to replace?"))
    print(f"{numchange} words has been replaced from the paragraph")
    print(paragraph.replace(search, change,numchange))
elif meow== 'N' and 'n':
    woff = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
    while True:
        if  woff == 'N' and 'n':
            break
        elif woff == 'Y' and 'y':
            paragraph = str(input("Please input a paragraph:"))
            search = str(input("Please input a replacement string:"))
            count = paragraph.count(search)
            print(f"There are {count} occurrences")
            meow= str(input("Do you want to replace the text[Y/N]"))
            if meow== 'Y' and 'y' :
                change = str(input("Enter word to replace"))
                print(f"{count} words has been replaced from the paragraph")
                print(paragraph.replace(search, change))
                break

else:
    print('"Please give a proper input"')
    meow= str(input("Do you want to replace the text[Y/N]"))
    if meow== 'N':
        woff = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
        if woff == 'Y':
            paragraph = str(input("Please input a paragraph:"))
            search = str(input("Please input a replacement string:"))
            count = paragraph.count(search)
            print(f"There are {count} occurrences")
            meow= str(input("Do you want to replace the text[Y/N]"))
            if meow== 'Y' and 'y' :
                change = str(input("Please input a replacement string:"))
                numchange = int(input("How many words would you want to replace?"))
                print(f"{numchange} words has been replaced from the paragraph")
                print(paragraph.replace(search, change, numchange))