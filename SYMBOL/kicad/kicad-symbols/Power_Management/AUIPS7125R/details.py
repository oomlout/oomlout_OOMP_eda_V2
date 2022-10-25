
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS7125R"
    hexID = "SZKPOWERMANAGEMENTAUIPS7125R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS7121R', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS7125R', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips7125.pdf?fileId=5546d462533600a4015355a7d96a132a', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Current Sense High Side Switch, 65V, 50A, DPAK-5L', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Power_Management : AUIPS7125R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

