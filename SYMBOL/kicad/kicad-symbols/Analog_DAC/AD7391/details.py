
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD7391"
    hexID = "SZKANALOGDACAD7391"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD7390', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD7391', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7390_7391.pdf', 'kicadSymbolki_keywords': 'SPI 10 bit DAC', 'kicadSymbolki_description': 'Serial-Input Micropower 10-Bit DAC, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : AD7391')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

