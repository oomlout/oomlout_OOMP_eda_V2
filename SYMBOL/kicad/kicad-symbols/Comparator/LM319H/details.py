
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LM319H"
    hexID = "SZKCOMPARATORLM319H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM319H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-100-10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm319-n.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp open collector', 'kicadSymbolki_description': 'High Speed Dual Comparator, TO-100-10', 'kicadSymbolki_fp_filters': 'TO?100*'}])
    newPart['name'].append('LM319H')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

