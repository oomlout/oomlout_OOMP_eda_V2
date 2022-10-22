
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ48_Shielded"
    hexID = "SZKCNRJ48SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8P4C_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ48_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '8P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 8P4C (8 positions 4 connected), Shielded', 'kicadSymbolki_fp_filters': '8P4C* RJ38* RJ48*'}])
    newPart['name'].append('RJ48_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

