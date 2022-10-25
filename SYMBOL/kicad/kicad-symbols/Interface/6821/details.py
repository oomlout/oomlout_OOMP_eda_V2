
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "6821"
    hexID = "SZKINTERFACE6821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '6821', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/motorola/6821.pdf', 'kicadSymbolki_keywords': 'PIA', 'kicadSymbolki_description': 'Peripheral Interface Adapter 1MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface : 6821')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

