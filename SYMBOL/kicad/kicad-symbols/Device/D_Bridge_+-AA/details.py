
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Bridge_+-AA"
    hexID = "SZKDEVICEDBRIDGE+AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Bridge_+-AA', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'rectifier ACDC', 'kicadSymbolki_description': 'Diode bridge, +ve/-ve/AC/AC', 'kicadSymbolki_fp_filters': 'D*Bridge* D*Rectifier*'}])
    newPart['name'].append('Device : D_Bridge_+-AA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

