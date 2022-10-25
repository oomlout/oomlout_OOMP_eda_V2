
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD390KD"
    hexID = "SZKANALOGDACAD39KD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD390JD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD390KD', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD390MIL.pdf', 'kicadSymbolki_keywords': '4ch DAC 12bit', 'kicadSymbolki_description': 'Quad 12bit DAC, 2LSB Gain Error, DH-28'}])
    newPart['name'].append('Analog_DAC : AD390KD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

