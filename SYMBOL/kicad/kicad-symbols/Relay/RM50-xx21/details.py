
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RM50-xx21"
    hexID = "SZKRELAYRM5XX21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FINDER-32.21-x300', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RM50-xx21', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_Finder_32.21-x300', 'kicadSymbolDatasheet': 'http://www.relpol.pl/en/content/download/13683/165953/file/e_RM50.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPST-NO', 'kicadSymbolki_description': 'RELPOL, Single Pole Relay SPST-NO, 6A', 'kicadSymbolki_fp_filters': 'Relay*SPST*Finder*32.21*x300*'}])
    newPart['name'].append('RM50-xx21')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

