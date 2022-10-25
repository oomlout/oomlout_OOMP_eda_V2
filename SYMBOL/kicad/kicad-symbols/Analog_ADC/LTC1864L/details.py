
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC1864L"
    hexID = "SZKANALOGADCLTC1864L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1864L', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/18645lfs.pdf', 'kicadSymbolki_keywords': 'sigma-delta adc spi 1ch', 'kicadSymbolki_description': 'Single channel 16-bit Analog to Digital Converter, 3V supply, differential input, 150ksps, SPI interface', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Analog_ADC : LTC1864L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

