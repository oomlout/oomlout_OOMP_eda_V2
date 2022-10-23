
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LIS3DH"
    hexID = "SZKSENMOTIONLIS3DH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LIS3DH', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/cd00274221.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer i2c spi mems', 'kicadSymbolki_description': '3-Axis Accelerometer, 2/4/8/16g range, I2C/SPI interface, LGA-16', 'kicadSymbolki_fp_filters': 'LGA*3x3mm*P0.5mm*LayoutBorder3x5y*'}])
    newPart['name'].append('LIS3DH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

