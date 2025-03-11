#!/usr/bin/python3

def famous_births(dict):
    dob = sorted(dict.values(), key=lambda x: x['date_of_birth'])
    for x in dob:
        print(f"{x["name"]} is a great scientist born in {x["date_of_birth"]}")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)