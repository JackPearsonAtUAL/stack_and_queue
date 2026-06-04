"""
02/03/2026(UK)
Sorting Stored Data
Jack Pearson
"""

a = [("a", 30), ("b", 67), ("c", 79), ("d", 13), ("e", 81), ("f", 2)]

print(sorted(
    a, 
    key = lambda item: item[1]
    ))

def extractor(item):
    return item[1]

