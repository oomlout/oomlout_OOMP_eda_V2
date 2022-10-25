
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAW56S"
    hexID = "SZKDIODEBAW56S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Rohm_UMP11N', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAW56S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAV756S_BAW56_SER.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'High Speed Switching Diode Array 2 pair Com A', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Diode : BAW56S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

