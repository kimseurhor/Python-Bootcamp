def message_conerter(mes):
    acc = [ord(k) for k in mes]
    hexa = [hex(l) for l in acc]
    fin = "".join(hexa).replace("0x", "")
    print(fin.upper())



message_conerter("i hate this and i wanna die")