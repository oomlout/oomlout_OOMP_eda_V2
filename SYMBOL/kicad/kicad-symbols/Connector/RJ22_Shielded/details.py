
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ22_Shielded"
    hexID = "SZKCNRJ22SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '4P4C_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ22_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '4P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 4P4C (4 positions 4 connected), Shielded', 'kicadSymbolki_fp_filters': '4P4C* RJ9* RJ10* RJ22*'}])
    newPart['name'].append('RJ22_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

