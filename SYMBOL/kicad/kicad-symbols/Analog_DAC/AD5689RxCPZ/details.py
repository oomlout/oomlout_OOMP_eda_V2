
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD5689RxCPZ"
    hexID = "SZKANALOGDACAD5689RXCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD5687BCPZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5689RxCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5689R_5687R.pdf', 'kicadSymbolki_keywords': 'dac 2nch 16bit spi', 'kicadSymbolki_description': 'Dual, 16-Bit nanoDAC+ with 2 ppm/°C Reference, SPI Interface, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : AD5689RxCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

