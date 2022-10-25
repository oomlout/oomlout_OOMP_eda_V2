
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIR33402S"
    hexID = "SZKPOWERMANAGEMENTAUIR3342S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIR33402S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auir33402s.pdf?fileId=5546d462533600a4015355a88074135c', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Protected High Side Switch, 18V, 33A, D2PAK-7L', 'kicadSymbolki_fp_filters': 'TO?263*TabPin4*'}])
    newPart['name'].append('Power_Management : AUIR33402S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

