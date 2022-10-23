
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-36.11"
    hexID = "SZKRELAYFINDER3611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-36.11', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Finder_36.11', 'kicadSymbolDatasheet': 'https://gfinder.findernet.com/public/attachments/36/EN/S36EN.pdf', 'kicadSymbolki_keywords': 'spdt relay', 'kicadSymbolki_description': 'FINDER 36.11, SPDT relay, 10A', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Finder*36.11*'}])
    newPart['name'].append('FINDER-36.11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

