
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "ADXL343"
    hexID = "SZKSENMOTIONADXL343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADXL343', 'kicadSymbolFootprint': 'Package_LGA:LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL343.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer i2c spi mems', 'kicadSymbolki_description': '3-Axis MEMS Accelerometer, 2/4/8/16g range, I2C/SPI, LGA-14', 'kicadSymbolki_fp_filters': '*LGA*3x5mm*P0.8mm*'}])
    newPart['name'].append('ADXL343')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

