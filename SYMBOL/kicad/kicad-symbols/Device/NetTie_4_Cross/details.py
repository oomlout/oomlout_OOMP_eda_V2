
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "NetTie_4_Cross"
    hexID = "SZKDEVICENT4CROSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'NT', 'kicadSymbolValue': 'NetTie_4_Cross', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'net tie short', 'kicadSymbolki_description': 'Net tie, 4 pins, cross', 'kicadSymbolki_fp_filters': 'Net*Tie*'}])
    newPart['name'].append('Device : NetTie_4_Cross')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

