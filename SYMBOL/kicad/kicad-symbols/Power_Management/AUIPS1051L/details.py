
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS1051L"
    hexID = "SZKPOWERMANAGEMENTAUIPS151L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS1051L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips1051.pdf?fileId=5546d462533600a4015355a4710712fc', 'kicadSymbolki_keywords': 'low side switch', 'kicadSymbolki_description': 'Intelligent Power Low Side Switch, 39V, 2.8A, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Power_Management : AUIPS1051L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

