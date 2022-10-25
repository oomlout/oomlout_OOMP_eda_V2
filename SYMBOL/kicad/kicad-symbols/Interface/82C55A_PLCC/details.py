
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "82C55A_PLCC"
    hexID = "SZKINTERFACE82C55APLCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '82C55A_PLCC', 'kicadSymbolFootprint': 'Package_LCC:PLCC-44', 'kicadSymbolDatasheet': 'http://jap.hu/electronic/8255.pdf', 'kicadSymbolki_keywords': '8255 PPI', 'kicadSymbolki_description': 'CHMOS Programmable Peripheral Interface, PLCC-44', 'kicadSymbolki_fp_filters': '*PLCC?44*'}])
    newPart['name'].append('Interface : 82C55A_PLCC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

