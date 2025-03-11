#!/usr/bin/python3

def array_of_names(dict):
    array = [f"{x.capitalize()} {dict[x].capitalize()}" for x in dict]
    return array

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))