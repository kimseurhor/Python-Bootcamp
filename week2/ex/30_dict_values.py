def dict_values(diction):
    for dictionkey, dictionvalue in diction.items():
        print(dictionkey, ":", *dictionvalue)
        print('*****')
dict_values(({120:("Visal", "Borey", "Sovann"), 130:("Hout", "Mouyleng", "Pidor"), 140:("Nary", "Misora","Masaki")}))