
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-34.51"
    hexID = "SZKRELAYFINDER3451"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-34.51', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Finder_34.51_Vertical', 'kicadSymbolDatasheet': 'https://gfinder.findernet.com/public/attachments/34/EN/S34USAEN.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPDT', 'kicadSymbolki_description': 'Ultra-slim 1 Pole - 6A SPDT relay', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Finder*34.51*'}])
    newPart['name'].append('FINDER-34.51')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

