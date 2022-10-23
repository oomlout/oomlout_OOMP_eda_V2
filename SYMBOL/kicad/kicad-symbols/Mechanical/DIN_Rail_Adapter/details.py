
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Mechanical"
    oIndex = "DIN_Rail_Adapter"
    hexID = "SZKMECHANICALDINRAILADAPTER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DRA', 'kicadSymbolValue': 'DIN_Rail_Adapter', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Mounting holes, DIN rail adapter', 'kicadSymbolki_description': 'DIN Rail adapter universal, mounting holes without connection', 'kicadSymbolki_fp_filters': 'DINRailAdapter?3xM3* DINRailAdapter?2xM3*'}])
    newPart['name'].append('DIN_Rail_Adapter')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

