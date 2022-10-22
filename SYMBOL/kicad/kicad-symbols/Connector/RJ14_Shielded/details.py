
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ14_Shielded"
    hexID = "SZKCNRJ14SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6P4C_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ14_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P4C (6 positions 4 connected), Shielded', 'kicadSymbolki_fp_filters': '6P4C* RJ13* RJ14*'}])
    newPart['name'].append('RJ14_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

