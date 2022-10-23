
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIR3315S"
    hexID = "SZKPOWERMANAGEMENTAUIR3315S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS7111S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIR3315S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auir3315.pdf?fileId=5546d462533600a4015355a84eda134d', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Programmable Current Sense High Side Switch, 32V, 30A, D2PAK-5L', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('AUIR3315S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

