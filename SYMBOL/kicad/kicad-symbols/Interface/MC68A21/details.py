
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "MC68A21"
    hexID = "SZKINTERFACEMC68A21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6821', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68A21', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/motorola/6821.pdf', 'kicadSymbolki_keywords': 'PIA', 'kicadSymbolki_description': 'Peripheral Interface Adapter 1.5MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface : MC68A21')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

