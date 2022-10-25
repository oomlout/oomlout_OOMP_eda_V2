
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD558JP"
    hexID = "SZKANALOGDACAD558JP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD558JP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD558.pdf', 'kicadSymbolki_keywords': '8bit DAC Reference Single Supply', 'kicadSymbolki_description': 'Single 8-bit DAC, Internal Reference, Output Amp, Single Supply, PLCC-20'}])
    newPart['name'].append('Analog_DAC : AD558JP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

