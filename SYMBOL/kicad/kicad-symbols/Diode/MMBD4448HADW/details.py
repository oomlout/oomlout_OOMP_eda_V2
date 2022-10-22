
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MMBD4448HADW"
    hexID = "SZKDIODEBD4448HADW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Rohm_UMP11N', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MMBD4448HADW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.diodes.com/datasheets/ds30153.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Fast Switching Diode Array 2 pair Com A', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('MMBD4448HADW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

