
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RM84"
    hexID = "SZKRELAYRM84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FINDER-40.52', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RM84', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Finder_40.52', 'kicadSymbolDatasheet': 'http://www.relpol.pl/en/content/download/13766/168095/file/e_RM84.pdf', 'kicadSymbolki_keywords': 'Dual Pole Relay', 'kicadSymbolki_description': 'RELPOL Dual Pole Relay, 5mm Pitch, 8A', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Finder*40.52*'}])
    newPart['name'].append('RM84')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

