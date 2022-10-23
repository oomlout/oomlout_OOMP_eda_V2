
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G6SU-2"
    hexID = "SZKRELAYG6SU2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G6SU-2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://omronfs.omron.com/en_US/ecb/products/pdf/en-g6s.pdf', 'kicadSymbolki_keywords': 'Miniature Relay Dual Pole DPDT Omron', 'kicadSymbolki_description': 'Compact, Industry-Standard 2-pole relay, designed to switch 2A Signal Loads, Single-winding Latching', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Omron*G6S?2*'}])
    newPart['name'].append('G6SU-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

