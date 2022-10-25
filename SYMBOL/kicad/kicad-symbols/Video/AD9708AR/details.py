
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "AD9708AR"
    hexID = "SZKVIDEOAD978AR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9708AR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD9708.pdf', 'kicadSymbolki_keywords': 'DAC CNA VIDEO', 'kicadSymbolki_description': 'Video DAC (32 MHz), SOIC/TSSOP-28'}])
    newPart['name'].append('Video : AD9708AR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

