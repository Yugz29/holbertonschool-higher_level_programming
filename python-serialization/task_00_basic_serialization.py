#!/usr/bin/env python3
"""
Module providing basic functions for JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object and save it to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""
    with open(filename, "r") as f:
        loaded = json.load(f)
    return loaded
