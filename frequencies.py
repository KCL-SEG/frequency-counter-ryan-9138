"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    string_items = [str(element) for element in items]
    frequencies = Counter(string_items)
    return frequencies
