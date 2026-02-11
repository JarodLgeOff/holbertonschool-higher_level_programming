#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data = []
        with open(csv_filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        with open("data.json", mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
