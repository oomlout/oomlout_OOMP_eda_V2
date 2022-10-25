
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD5687RBRUZ"
    hexID = "SZKANALOGDACAD5687RBRUZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD5687BRUZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5687RBRUZ', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5689R_5687R.pdf', 'kicadSymbolki_keywords': 'dac 2nch 12bit spi', 'kicadSymbolki_description': 'Dual, 12-Bit nanoDAC+ with 2 ppm/°C Reference, SPI Interface, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : AD5687RBRUZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

