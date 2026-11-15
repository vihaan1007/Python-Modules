import pickle

b = {"name": "A", "age": 9}

with open("data.pkl", "wb") as a:
    pickle.dump(b, a)

with open("data.pkl", "rb") as f:
    data = pickle.load(f)

print(data)

dat = {"x": 10, "y": 20}

c = pickle.dumps(dat)
print(c)
print(type(c))

da = {"x": 10, "y": 20}

b = pickle.dumps(da)
original = pickle.loads(b)

print(original)
print(type(original))
