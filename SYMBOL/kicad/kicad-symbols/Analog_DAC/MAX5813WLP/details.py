
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5813WLP"
    hexID = "SZKANALOGDACMAX5813WLP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5813WLP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX5813-MAX5815.pdf', 'kicadSymbolki_keywords': 'DA 8 Bit 4 ch', 'kicadSymbolki_description': 'Digital to analog, 8 Bit, 4 ch, 2.7 - 5.5 VDD, I2C, TSSOP-14, Maxim_WLP-12', 'kicadSymbolki_fp_filters': '*Maxim*WLP*12*'}])
    newPart['name'].append('Analog_DAC : MAX5813WLP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

