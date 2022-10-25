
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HC273"
    hexID = "SZK74XX74HC273"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS273', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HC273', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74HC_HCT273.pdf', 'kicadSymbolki_keywords': 'HCMOS DFF DFF8', 'kicadSymbolki_description': '8-bit D Flip-Flop, reset', 'kicadSymbolki_fp_filters': 'DIP?20* SO?20* SOIC?20*'}])
    newPart['name'].append('74xx : 74HC273')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

