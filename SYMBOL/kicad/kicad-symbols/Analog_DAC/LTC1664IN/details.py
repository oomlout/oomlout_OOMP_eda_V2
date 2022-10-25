
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "LTC1664IN"
    hexID = "SZKANALOGDACLTC1664IN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1664CGN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1664IN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1664fa.pdf', 'kicadSymbolki_keywords': 'Quad DAC Micropower 10bit 4ch', 'kicadSymbolki_description': 'Quad Micropower 10-bit DAC, Industrial, DIP-16', 'kicadSymbolki_fp_filters': '*SSOP*'}])
    newPart['name'].append('Analog_DAC : LTC1664IN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

