
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "WC1602A"
    hexID = "SZKDICHARACTERWC162A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DS', 'kicadSymbolValue': 'WC1602A', 'kicadSymbolFootprint': 'Display:WC1602A', 'kicadSymbolDatasheet': 'http://www.wincomlcd.com/pdf/WC1602A-SFYLYHTC06.pdf', 'kicadSymbolki_keywords': 'display LCD dot-matrix', 'kicadSymbolki_description': 'LCD 16x2 Alphanumeric , 8 bit parallel bus, 5V VDD', 'kicadSymbolki_fp_filters': '*WC*1602A*'}])
    newPart['name'].append('Display_Character : WC1602A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

