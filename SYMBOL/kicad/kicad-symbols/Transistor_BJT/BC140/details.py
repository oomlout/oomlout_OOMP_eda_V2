
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC140"
    hexID = "SZKTRANSISTORBJTBC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '2N2219', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC140', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/296634.pdf', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '1A Ic, 40V Vce, NPN Transistor, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('BC140')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

