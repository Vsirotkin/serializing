import json
import pickle


my_favourite_group = {
    'name': 'Jethro Tull',
    'tracks': ['Aquarius'],
    'Albums': [{'name': 'Aquarius', 'year': 2016}]
}


# print(my_favourite_group)
# print(type(my_favourite_group))


# json_group = json.dumps(my_favourite_group)
# print(json_group)
# print(type(json_group))


# picke_group = pickle.dumps(my_favourite_group)
# print(picke_group)
# print(type(picke_group))


with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
