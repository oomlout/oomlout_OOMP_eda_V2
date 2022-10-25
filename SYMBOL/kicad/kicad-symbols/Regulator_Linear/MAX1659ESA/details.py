
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX1659ESA"
    hexID = "SZKREGULATORLINEARMAX1659ESA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX1658ESA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1659ESA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX1658-MAX1659.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator 350mA 5V', 'kicadSymbolki_description': '350mA Linear LDO Regulator, Fixed Output 5V, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : MAX1659ESA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

