
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "6822"
    hexID = "SZKINTERFACE6822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6821', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '6822', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf1.alldatasheet.com/datasheet-pdf/view/135452/MOTOROLA/MC6822.html', 'kicadSymbolki_keywords': 'PIA', 'kicadSymbolki_description': 'Peripheral Interface Adapter 1MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface : 6822')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

