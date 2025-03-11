#!/usr/bin/python3

def find_the_redheads(dict):
    return list(filter(lambda x: dict[x] == "red", dict))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))