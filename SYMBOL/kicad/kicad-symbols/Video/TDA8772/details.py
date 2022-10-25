
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "TDA8772"
    hexID = "SZKVIDEOTDA8772"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA8772', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.pa0qy.nl/pdf/TDA8772.PDF', 'kicadSymbolki_keywords': 'Video DAC Colour 8bit', 'kicadSymbolki_description': 'Triple 8bit Video DAC, QFP-44', 'kicadSymbolki_fp_filters': 'QFP*'}])
    newPart['name'].append('Video : TDA8772')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

