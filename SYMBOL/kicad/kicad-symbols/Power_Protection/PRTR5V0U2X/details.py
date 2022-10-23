
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PRTR5V0U2X"
    hexID = "SZKPOWERPROTECTIONPRTR5VU2X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PRTR5V0U2X', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PRTR5V0U2X.pdf', 'kicadSymbolki_keywords': 'ESD protection diode', 'kicadSymbolki_description': 'Ultra low capacitance double rail-to-rail ESD protection diode, SOT-143', 'kicadSymbolki_fp_filters': 'SOT?143*'}])
    newPart['name'].append('PRTR5V0U2X')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

