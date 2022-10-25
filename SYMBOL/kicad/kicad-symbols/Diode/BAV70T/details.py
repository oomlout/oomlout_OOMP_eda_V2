
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAV70T"
    hexID = "SZKDIODEBAV7T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAV70T', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-416', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAV70_SER.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Dual 100V 150mA high-speed switching diodes, common cathode, SOT-416', 'kicadSymbolki_fp_filters': 'SOT?416*'}])
    newPart['name'].append('Diode : BAV70T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

