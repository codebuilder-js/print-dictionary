def printDictionary(title, list, leftWidth, rightWidth):
    print(f'{title}'.center(leftWidth + rightWidth, '-'))

    for k, v in list.items():
        print(f'{k.ljust(leftWidth, '.')}{str(v).rjust(rightWidth)}')

picnicList = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookeis': 8000}

printDictionary('PICNIC ITEMS', picnicList, 12, 5)
printDictionary('PICNIC ITEMS', picnicList, 20, 6)