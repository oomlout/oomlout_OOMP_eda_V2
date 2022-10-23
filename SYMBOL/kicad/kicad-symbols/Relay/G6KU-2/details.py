
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G6KU-2"
    hexID = "SZKRELAYG6KU2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G6KU-2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k.pdf', 'kicadSymbolki_keywords': 'Miniature Relay Dual Pole DPDT Omron', 'kicadSymbolki_description': 'Miniature 2-pole relay, Single-winding Latching', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Omron*G6K?2*Y*'}])
    newPart['name'].append('G6KU-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

