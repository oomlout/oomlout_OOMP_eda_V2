
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RSM822"
    hexID = "SZKRELAYRSM822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FINDER-40.52', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RSM822', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Finder_40.52', 'kicadSymbolDatasheet': 'http://www.relpol.pl/en/content/download/14975/202519/file/e_RSM822.pdf', 'kicadSymbolki_keywords': 'Dual Pole Relay', 'kicadSymbolki_description': 'RELPOL Dual Pole Relay, 5mm Pitch, 2A', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Finder*40.52*'}])
    newPart['name'].append('Relay : RSM822')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

