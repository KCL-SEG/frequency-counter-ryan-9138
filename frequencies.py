"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    string_items = [str(element) for element in items]
    frequencies = {}
    for i in range(0,len(string_items)):
        count = string_items.count(string_items[i])
        frequencies[string_items[i]] = count
    return frequencies

