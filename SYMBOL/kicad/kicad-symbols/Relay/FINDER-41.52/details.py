
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-41.52"
    hexID = "SZKRELAYFINDER4152"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FINDER-40.52', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-41.52', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Finder_40.52', 'kicadSymbolDatasheet': 'http://gfinder.findernet.com/assets/Series/357/S41EN.pdf', 'kicadSymbolki_keywords': 'Dual Pole Relay', 'kicadSymbolki_description': 'FINDER 41.52, Dual Pole Relay, 5mm Pitch, 8A', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Finder*40.52*'}])
    newPart['name'].append('FINDER-41.52')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

