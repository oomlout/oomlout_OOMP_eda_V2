
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS7111S"
    hexID = "SZKPOWERMANAGEMENTAUIPS7111S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS7111S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips7111s.pdf?fileId=5546d462533600a4015355a7c94e1326', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Current Sense High Side Switch, 65V, 30A, D2PAK-5L', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('AUIPS7111S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

