
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7305"
    hexID = "SZKANALOGDACAD735"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7305', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7304_7305.pdf', 'kicadSymbolki_keywords': 'dac 4ch 8bit parallel', 'kicadSymbolki_description': '3V/5V, Rail-to-Rail, Quad, 8-Bit DAC, Parallel Interface, SOIC-20/TSSOP-20', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x12.8mm*P1.27mm* TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : AD7305')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

