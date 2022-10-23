
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS2041L"
    hexID = "SZKPOWERMANAGEMENTAUIPS241L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS1051L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS2041L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-AUIPS2041-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aae147a9d4c57', 'kicadSymbolki_keywords': 'low side switch', 'kicadSymbolki_description': 'Intelligent Power Low Side Switch, 68V, 5A, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('AUIPS2041L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

