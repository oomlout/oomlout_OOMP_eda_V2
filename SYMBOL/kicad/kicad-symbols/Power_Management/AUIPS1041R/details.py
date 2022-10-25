
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS1041R"
    hexID = "SZKPOWERMANAGEMENTAUIPS141R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS1041R', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-AUIPS1041-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aae14a0524c63', 'kicadSymbolki_keywords': 'low side switch', 'kicadSymbolki_description': 'Intelligent Power Low Side Switch, 39V, 4.5A, DPAK-5L', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Power_Management : AUIPS1041R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

