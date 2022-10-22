
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD5697RBCPZ"
    hexID = "SZKANALOGDACAD5697RBCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5697RBCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5697R.pdf', 'kicadSymbolki_keywords': 'dac 2nch 12bit i2c', 'kicadSymbolki_description': 'Dual, 12-Bit nanoDAC+ with 2 ppm/°C Reference, I2C Interface, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*3x3mm*P0.5mm*'}])
    newPart['name'].append('AD5697RBCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

