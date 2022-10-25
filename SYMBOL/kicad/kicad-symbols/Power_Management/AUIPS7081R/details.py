
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS7081R"
    hexID = "SZKPOWERMANAGEMENTAUIPS781R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS6011R', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS7081R', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips7081.pdf?fileId=5546d462533600a4015355a7b8d5131e', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Intelligent Power High Side Switch, 70V, 5A, DPAK-5L', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Power_Management : AUIPS7081R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

