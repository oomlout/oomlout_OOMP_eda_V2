
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "EL34"
    hexID = "SZKVAEL34"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EL34', 'kicadSymbolFootprint': 'Valve:Valve_Octal', 'kicadSymbolDatasheet': 'http://www.r-type.org/pdfs/el34.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'pentode valve', 'kicadSymbolki_description': 'pentode, 25W', 'kicadSymbolki_fp_filters': 'VALVE*OCTAL*'}])
    newPart['name'].append('EL34')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

