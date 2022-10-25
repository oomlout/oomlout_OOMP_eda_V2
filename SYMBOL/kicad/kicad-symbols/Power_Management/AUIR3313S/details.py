
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIR3313S"
    hexID = "SZKPOWERMANAGEMENTAUIR3313S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS7111S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIR3313S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auir3313.pdf?fileId=5546d462533600a4015355a83e2d1347', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Programmable Current Sense High Side Switch, 32V, 90A, D2PAK-5L', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Power_Management : AUIR3313S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

