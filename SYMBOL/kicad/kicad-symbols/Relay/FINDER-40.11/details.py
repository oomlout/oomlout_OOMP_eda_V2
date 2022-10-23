
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-40.11"
    hexID = "SZKRELAYFINDER411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-40.11', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Finder_40.11', 'kicadSymbolDatasheet': 'https://www.finder-relais.net/de/finder-relais-serie-40.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPDT Finder', 'kicadSymbolki_description': 'PCB SPDT relay, 10A', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Finder*40.11*'}])
    newPart['name'].append('FINDER-40.11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

