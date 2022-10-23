
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-40.51"
    hexID = "SZKRELAYFINDER451"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-40.51', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Finder_40.51', 'kicadSymbolDatasheet': 'http://gfinder.findernet.com/assets/Series/353/S40EN.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay', 'kicadSymbolki_description': 'FINDER 40.51, Single Pole Relay, 5mm Pitch, 10A', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Finder*40.51*'}])
    newPart['name'].append('FINDER-40.51')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

