
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Fuse_Small"
    hexID = "SZKDEVICEFUSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'F', 'kicadSymbolValue': 'Fuse_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'fuse', 'kicadSymbolki_description': 'Fuse, small symbol', 'kicadSymbolki_fp_filters': 'SM*'}])
    newPart['name'].append('Device : Fuse_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

