
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC2358-16"
    hexID = "SZKANALOGADCLTC235816"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2358-16', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/235816f.pdf', 'kicadSymbolki_keywords': '16bit Simultaneous Sampling ADC 8 Channels SPI buffered', 'kicadSymbolki_description': 'LTC2358 Buffered Octal, 16 bit, 200ksps/Ch Differential +-10.24V Simultaneous Sampling ADC, 30Vpp common mode range, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP?48*7x7mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : LTC2358-16')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

