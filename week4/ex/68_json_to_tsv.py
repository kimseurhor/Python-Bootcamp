import json
import csv
import os
def json_to_tsv(fjson,tsv):
    while True:
        if os.path.exists(fjson):
            v = open(fjson)
            k = json.load(v)
            with open(tsv, 'w') as output_file:
                dw = csv.DictWriter(output_file, sorted(k[0].keys()), delimiter='\t')
                dw.writeheader()
                dw.writerows(k)
            return print(1)
        else:
            return print(0)


json_to_tsv("meow.json", "tsvmeow.tsv")