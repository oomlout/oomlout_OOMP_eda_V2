
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7228ABN"
    hexID = "SZKANALOGDACAD7228ABN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7228ABN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7228.pdf', 'kicadSymbolki_keywords': '8bit DAC 8CH', 'kicadSymbolki_description': '8bit DAC 8 Channel, Single Reference, DIP-24', 'kicadSymbolki_fp_filters': 'PDIP* DIP*'}])
    newPart['name'].append('Analog_DAC : AD7228ABN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

