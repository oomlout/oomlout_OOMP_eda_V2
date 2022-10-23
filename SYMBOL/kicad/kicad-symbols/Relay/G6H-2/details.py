
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G6H-2"
    hexID = "SZKRELAYG6H2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G6H-2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/C300/G6H%23OMR.pdf', 'kicadSymbolki_keywords': 'relay monostable', 'kicadSymbolki_description': 'Omron Ultracompact, Ultrasensitive DPDT Relay, Single-side Stable', 'kicadSymbolki_fp_filters': 'Relay*Omron*G6H?2*'}])
    newPart['name'].append('G6H-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

