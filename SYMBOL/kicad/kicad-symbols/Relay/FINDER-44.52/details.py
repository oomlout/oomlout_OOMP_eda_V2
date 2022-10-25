
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-44.52"
    hexID = "SZKRELAYFINDER4452"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FINDER-40.52', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-44.52', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Finder_40.52', 'kicadSymbolDatasheet': 'http://gfinder.findernet.com/assets/Series/359/S44EN.pdf', 'kicadSymbolki_keywords': 'Dual Pole Relay', 'kicadSymbolki_description': 'FINDER 44.52, Dual Pole Relay, 5mm Pitch, 6A', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Finder*40.52*'}])
    newPart['name'].append('Relay : FINDER-44.52')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

