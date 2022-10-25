
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_TVS_Dual_AAC"
    hexID = "SZKDEVICEDTVSDUALAAC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_TVS_Dual_AAC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'diode TVS thyrector', 'kicadSymbolki_description': 'Bidirectional dual transient-voltage-suppression diode, center on pin 3'}])
    newPart['name'].append('Device : D_TVS_Dual_AAC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

