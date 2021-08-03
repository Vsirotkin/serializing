import json
import pickle

with open('group.json', 'r') as f:
    result = json.load(f)

print(result)


with open('group.pickle', 'rb') as f:
    result = pickle.load(f)

print(result)
