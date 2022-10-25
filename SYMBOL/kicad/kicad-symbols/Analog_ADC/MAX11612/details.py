
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX11612"
    hexID = "SZKANALOGADCMAX11612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX11612', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX11612-MAX11617.pdf', 'kicadSymbolki_keywords': 'adc i2c 4ch', 'kicadSymbolki_description': '4-channel single-ended or 2-channel, differential, 12-bit ADC, I2C, 4.096V internal reference, 8-MSOP package', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_ADC : MAX11612')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

