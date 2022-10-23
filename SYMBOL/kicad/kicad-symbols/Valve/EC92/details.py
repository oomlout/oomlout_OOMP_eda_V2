
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "EC92"
    hexID = "SZKVAEC92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EC92', 'kicadSymbolFootprint': 'Valve:Valve_Mini_P', 'kicadSymbolDatasheet': 'http://www.r-type.org/pdfs/ec92.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'triode valve', 'kicadSymbolki_description': 'single triode', 'kicadSymbolki_fp_filters': 'VALVE*MINI*P*'}])
    newPart['name'].append('EC92')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

