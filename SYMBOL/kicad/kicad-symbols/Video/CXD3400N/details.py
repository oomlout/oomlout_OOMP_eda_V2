
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "CXD3400N"
    hexID = "SZKVIDEOCXD34N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CXD3400N', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'videocxd3400n.pdf', 'kicadSymbolki_keywords': 'CCD Clock Driver', 'kicadSymbolki_description': '6-channel Vertical Clock Driver for CCD Image Sensor, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('Video : CXD3400N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

