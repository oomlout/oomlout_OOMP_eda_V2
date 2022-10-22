
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX11615"
    hexID = "SZKANALOGADCMAX11615"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX11614', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX11615', 'kicadSymbolFootprint': 'Package_SO:QSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX11612-MAX11617.pdf', 'kicadSymbolki_keywords': 'adc i2c 8ch', 'kicadSymbolki_description': '8-channel single-ended or 4-channel, differential, 12-bit ADC, I2C, 2.048V internal reference, 16-QSOP package', 'kicadSymbolki_fp_filters': 'QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('MAX11615')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

