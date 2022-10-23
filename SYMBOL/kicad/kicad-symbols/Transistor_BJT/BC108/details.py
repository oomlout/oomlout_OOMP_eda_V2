
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC108"
    hexID = "SZKTRANSISTORBJTBC18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC107', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC108', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3', 'kicadSymbolDatasheet': 'http://www.b-kainka.de/Daten/Transistor/BC108.pdf', 'kicadSymbolki_keywords': 'NPN low noise transistor', 'kicadSymbolki_description': '0.1A Ic, 30V Vce, Low Noise General Purpose NPN Transistor, TO-18', 'kicadSymbolki_fp_filters': 'TO?18*'}])
    newPart['name'].append('BC108')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

