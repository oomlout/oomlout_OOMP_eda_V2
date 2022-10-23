
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC161"
    hexID = "SZKTRANSISTORBJTBC161"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC160', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC161', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/1697389.pdf', 'kicadSymbolki_keywords': 'power PNP Transistor', 'kicadSymbolki_description': '1A Ic, 60V Vce, Power PNP Transistor, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('BC161')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

