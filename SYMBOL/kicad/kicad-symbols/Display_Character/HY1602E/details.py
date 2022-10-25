
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HY1602E"
    hexID = "SZKDICHARACTERHY162E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DS', 'kicadSymbolValue': 'HY1602E', 'kicadSymbolFootprint': 'Display:HY1602E', 'kicadSymbolDatasheet': 'http://www.icbank.com/data/ICBShop/board/HY1602E.pdf', 'kicadSymbolki_keywords': 'display LCD 7-segment', 'kicadSymbolki_description': 'LCD 16x2 Alphanumeric 16pin Blue/Yellow/Green Backlight, 8bit parallel, 5V VDD', 'kicadSymbolki_fp_filters': '*HY1602E*'}])
    newPart['name'].append('Display_Character : HY1602E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

