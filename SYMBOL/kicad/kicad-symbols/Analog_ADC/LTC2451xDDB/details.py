
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC2451xDDB"
    hexID = "SZKANALOGADCLTC2451XDDB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2451xDDB', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x3mm_P0.5mm_EP0.56x2.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/2451fg.pdf', 'kicadSymbolki_keywords': 'analog to digital converter adc i2c twi single channel delta sigma 16 bit', 'kicadSymbolki_description': 'Analog to Digital Converter, Single Channel, 16-Bit, 30/60 SPS, 2.7V to 5.5V, I2C interface, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x3mm*P0.5mm*'}])
    newPart['name'].append('LTC2451xDDB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

