
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2N2647"
    hexID = "SZKTRANSISTORBJT2N2647"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '2N2646', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2N2647', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3', 'kicadSymbolDatasheet': 'http://www.bucek.name/pdf/2n2646,2647.pdf', 'kicadSymbolki_keywords': 'UJT', 'kicadSymbolki_description': 'Unijunction Transistor, TO-18', 'kicadSymbolki_fp_filters': 'TO?18*'}])
    newPart['name'].append('2N2647')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

