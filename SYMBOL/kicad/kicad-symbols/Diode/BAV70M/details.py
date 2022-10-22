
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAV70M"
    hexID = "SZKDIODEBAV7M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAV70M', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-883', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAV70_SER.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Dual 100V 150mA high-speed switching diodes, common cathode, SOT-883', 'kicadSymbolki_fp_filters': 'SOT?883*'}])
    newPart['name'].append('BAV70M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

