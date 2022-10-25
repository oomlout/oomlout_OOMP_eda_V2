
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1594CS"
    hexID = "SZKANALOGADCLTC1594CS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1594CS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/15948fb.pdf', 'kicadSymbolki_keywords': '12bit ADC 4 Channel', 'kicadSymbolki_description': 'Micropower 12-bit 4 Channel ADC, Serial IO, SOIC-16', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('Analog_ADC : LTC1594CS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

