#!/usr/bin/env python3
"""
Module containing functions for serializing and deserializing
Python dictionaries to and from XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a dictionary.

    Returns:
        dict: A dictionary containing the data parsed from the XML file.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
