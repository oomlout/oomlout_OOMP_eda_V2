
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "LTC1257"
    hexID = "SZKANALOGDACLTC1257"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1257', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1257fc.pdf', 'kicadSymbolki_keywords': 'DAC 12-bit', 'kicadSymbolki_description': 'Single Supply 12-bit DAC with Internal Reference Voltage, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*'}])
    newPart['name'].append('Analog_DAC : LTC1257')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

