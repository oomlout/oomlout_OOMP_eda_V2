
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AudioPlug3"
    hexID = "SZKCNAUDIOPLUG3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AudioPlug3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'audio jack plug stereo headphones TRRS connector 2.5mm 3.5mm 6.35mm', 'kicadSymbolki_description': 'Audio Jack, 3 Poles (Stereo / TRS)', 'kicadSymbolki_fp_filters': 'Plug*'}])
    newPart['name'].append('Connector : AudioPlug3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

