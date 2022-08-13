import json
import os

def tvs_to_json(tvs, fjosn):

    if os.path.isfile(tvs):

        arr = []
        file = open(tvs, 'r')
        a = file.readline()


        titles = [t.strip() for t in a.split('\t')]
        for line in file:
            d = {}
            for t, f in zip(titles, line.split('\t')):

                d[t] = f.strip()


            arr.append(d)

        with open(fjosn, 'w', encoding='utf-8') as fjosn:
             fjosn.write(json.dumps(arr ,indent=4))
        return print(1)
    else:
        return print(0)


tvs_to_json("tsv1.tsv", "tsv1.json")
