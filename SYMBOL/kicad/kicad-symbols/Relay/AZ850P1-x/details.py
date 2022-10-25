
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "AZ850P1-x"
    hexID = "SZKRELAYAZ85P1X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AZ850-x', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'AZ850P1-x', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_FRT5', 'kicadSymbolDatasheet': 'http://www.azettler.com/pdfs/az850.pdf', 'kicadSymbolki_keywords': 'Miniature Polarised Relay Dual Pole Bistable', 'kicadSymbolki_description': 'American Zettler, Microminiature Polarised Dual Pole Relay Bistable', 'kicadSymbolki_fp_filters': 'Relay*DPDT*FRT5*'}])
    newPart['name'].append('Relay : AZ850P1-x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

