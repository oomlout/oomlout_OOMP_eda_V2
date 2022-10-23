
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38512TJ-1.8"
    hexID = "SZKREGULATORLINEARLP38512TJ18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38512TJ-1.8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Texas_NDQ', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp38512.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '1.5A Fast-Transient Response Low-Dropout Linear Voltage Regulator with Error Flag, 1.8V Output, NDQ', 'kicadSymbolki_fp_filters': 'Texas*NDQ*'}])
    newPart['name'].append('LP38512TJ-1.8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

