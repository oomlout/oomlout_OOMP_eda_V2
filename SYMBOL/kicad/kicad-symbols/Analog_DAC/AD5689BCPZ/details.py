
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD5689BCPZ"
    hexID = "SZKANALOGDACAD5689BCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD5687BCPZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5689BCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5689_5687.pdf', 'kicadSymbolki_keywords': 'dac 2nch 16bit spi', 'kicadSymbolki_description': 'Dual, 16-Bit nanoDAC+ with SPI Interface, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : AD5689BCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

