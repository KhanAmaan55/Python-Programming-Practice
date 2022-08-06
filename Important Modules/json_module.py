import json
data =' {"var1":"Amaan","var2": 55} '
print(data)
parsed = json.loads(data)
print(parsed)

data2 = {
    "Collage name":"SGGS college",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roll', 'cake'),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)