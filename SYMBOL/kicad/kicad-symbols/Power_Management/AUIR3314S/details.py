
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIR3314S"
    hexID = "SZKPOWERMANAGEMENTAUIR3314S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS7111S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIR3314S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auir3314.pdf?fileId=5546d462533600a4015355a846b8134a', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Programmable Current Sense High Side Switch, 32V, 58A, D2PAK-5L', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Power_Management : AUIR3314S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

