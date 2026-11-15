import json

a={
    "name" : "A",
    "age" : 9
}

json_string = json.dumps(a)
print(json_string)

json_str = '{"x" : 10, "y" : 20}'
print(json.loads(json_str))

data = {
    'city' : "Delhi",
    'Pin' : 482002
}

with open("data.json", "w") as f:
    json.dump(data, f)

#with open("data2.json", "w") as b:
#   json.load(f) json -> Python

#json.dump(data, f, indent=4, sort_keys=True) indent=4 readable sort_keys=True alphabetical order
