
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "LTC2451xTS8"
    hexID = "SZKANALOGADCLTC2451XTS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2451xTS8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-8', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/2451fg.pdf', 'kicadSymbolki_keywords': 'analog to digital converter adc i2c twi single channel delta sigma 16 bit', 'kicadSymbolki_description': 'Analog to Digital Converter, Single Channel, 16-Bit, 30/60 SPS, 2.7V to 5.5V, I2C interface, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Analog_ADC : LTC2451xTS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

