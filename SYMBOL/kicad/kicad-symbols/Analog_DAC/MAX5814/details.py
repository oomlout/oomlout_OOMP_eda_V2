
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5814"
    hexID = "SZKANALOGDACMAX5814"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5813', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5814', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX5813-MAX5815.pdf', 'kicadSymbolki_keywords': 'DA 10 Bit 4 ch', 'kicadSymbolki_description': 'Digital to analog, 10 Bit, 4 ch, 2.7 - 5.5 VDD, I2C, TSSOP-14', 'kicadSymbolki_fp_filters': '*TSSOP*14*4.4*'}])
    newPart['name'].append('Analog_DAC : MAX5814')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

