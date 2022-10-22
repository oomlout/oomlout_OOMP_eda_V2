
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX11614"
    hexID = "SZKANALOGADCMAX11614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX11614', 'kicadSymbolFootprint': 'Package_SO:QSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX11612-MAX11617.pdf', 'kicadSymbolki_keywords': 'adc i2c 8ch', 'kicadSymbolki_description': '8-channel single-ended or 4-channel, differential, 12-bit ADC, I2C, 4.096V internal reference, 16-QSOP package', 'kicadSymbolki_fp_filters': 'QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('MAX11614')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

