
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM337_TO3"
    hexID = "SZKREGULATORLINEARLM337TO3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM337_TO3', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm337-n.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1.5A Negative', 'kicadSymbolki_description': 'Negative 1.5A 35V Adjustable Linear Regulator, TO-3', 'kicadSymbolki_fp_filters': 'TO?3*'}])
    newPart['name'].append('LM337_TO3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

