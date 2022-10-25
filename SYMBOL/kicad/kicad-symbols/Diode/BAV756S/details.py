
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAV756S"
    hexID = "SZKDIODEBAV756S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAV756S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAV756S_BAW56_SER.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'Diode', 'kicadSymbolki_description': 'High-speed switching diodes, dual common anode/common cathode, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Diode : BAV756S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

