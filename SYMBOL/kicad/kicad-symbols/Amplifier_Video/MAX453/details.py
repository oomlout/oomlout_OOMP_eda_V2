
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Video"
    oIndex = "MAX453"
    hexID = "SZKAMPLIFIERVIDEOMAX453"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX453', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX452-MAX455.pdf', 'kicadSymbolki_keywords': 'amplifier', 'kicadSymbolki_description': 'CMOS video amplifier with input multiplexer, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Video : MAX453')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

