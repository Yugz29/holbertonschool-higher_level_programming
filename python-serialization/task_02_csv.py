#!/usr/bin/env python3
"""Module that converts a CSV file to a JSON file.

This module defines a function `convert_csv_to_json` which:
- Reads a CSV file using the `csv` module.
- Converts its rows into a list of dictionaries using `DictReader`.
- Serializes the list into JSON format and writes it to `data.json`.

The function returns True if succeeds, or False if an error
"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file into a JSON file named 'data.json'.

    Returns:
        bool: True if is successful, False if the file isn't found or an error.
    """
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open("data.json", "w") as jsonfile:
            json.dump(data, jsonfile)
        return True
    except FileNotFoundError:
        return False
