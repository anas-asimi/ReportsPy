import json


def line_to_obj(line):
    my_dict = dict()
    keys = [
        "TIMESTAMP",
        "RECORD",
        "Batterie",
        "Temperature",
        "Temperature_Min",
        "Temperature_Max",
        "Humidite",
        "Humidite_Min",
        "Humidite_Max",
        "Temp_rosee",
        "Temp_rosee_Min",
        "Temp_rosee_Max",
        "Vitesse",
        "Direction",
        "Dir_Ecart_type",
        "Rafale",
        "Temps_Rafale",
        "Dir_Rafale",
        "Rayonnement",
        "Durree_Insolation",
        "Pluie",
        "ET0",
    ]
    values = line.split(",")
    for i in range(min(len(keys), len(values))):
        my_dict[keys[i]] = values[i].strip('"')
    return my_dict


def save_dict(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
# my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}
# save_dict_to_json(my_dict, "output.json")
