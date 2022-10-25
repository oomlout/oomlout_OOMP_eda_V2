
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX603"
    hexID = "SZKREGULATORLINEARMAX63"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX603', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX603-MAX604.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator 500mA 5V fixed', 'kicadSymbolki_description': '500mA Linear LDO Regulator, Fixed Output 5V, DIP-8/SO-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : MAX603')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

