
# JSON = JavaScript Object Notation
# Schnelles und einfaches verwalten von Datensätzen

import json


ECTS_dict = {'ECTS_main': ["120"],
         'ECTS_ux' : ["0"],
         'ECTS_inovation': ["4"],
            "ECTS_information": ["4"],
            "ECTS_sozial": ["4"] }

print(ECTS_dict)

with open('Speicher_ECTS.json', 'w') as f:
    json.dump(ECTS_dict, f, indent=4, separators=(',', ':'), sort_keys=True)

