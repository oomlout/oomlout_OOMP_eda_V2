
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7226KP"
    hexID = "SZKANALOGDACAD7226KP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7226KP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD7226.pdf', 'kicadSymbolki_keywords': '4CH DAC 8bit', 'kicadSymbolki_description': 'Quad 8bit DAC, 4 Channel, Single Reference Voltage, PLCC-20', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('Analog_DAC : AD7226KP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

