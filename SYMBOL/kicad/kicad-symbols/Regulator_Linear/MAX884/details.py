
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX884"
    hexID = "SZKREGULATORLINEARMAX884"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX883', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX884', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX882-MAX884.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator', 'kicadSymbolki_description': '200mA Linear LDO Regulator, Fixed Output 3.3V or Adjustable with Shutdown Mode, 0C to +70C, DIP-8/SO-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : MAX884')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

