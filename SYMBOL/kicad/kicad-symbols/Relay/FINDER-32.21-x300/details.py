
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FINDER-32.21-x300"
    hexID = "SZKRELAYFINDER3221X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FINDER-32.21-x300', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_Finder_32.21-x300', 'kicadSymbolDatasheet': 'http://gfinder.findernet.com/assets/Series/355/S32EN.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPST-NO', 'kicadSymbolki_description': 'FINDER 32.21-x300, Single Pole Relay SPST-NO, 6A', 'kicadSymbolki_fp_filters': 'Relay*SPST*Finder*32.21*x300*'}])
    newPart['name'].append('Relay : FINDER-32.21-x300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

