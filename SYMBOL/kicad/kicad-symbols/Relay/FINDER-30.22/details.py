
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-30.22"
    hexID = "SZKRELAYFINDER322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-30.22', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Finder_30.22', 'kicadSymbolDatasheet': 'http://gfinder.findernet.com/assets/Series/354/S30EN.pdf', 'kicadSymbolki_keywords': 'Dual Pole Relay', 'kicadSymbolki_description': 'FINDER 30.52, Dual Pole Relay, Subminiature 5mm Pitch, 2A', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Finder*30.22*'}])
    newPart['name'].append('Relay : FINDER-30.22')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

