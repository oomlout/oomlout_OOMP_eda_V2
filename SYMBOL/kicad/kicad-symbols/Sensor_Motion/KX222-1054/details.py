
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "KX222-1054"
    hexID = "SZKSENMOTIONKX222154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KX022-1020', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KX222-1054', 'kicadSymbolFootprint': 'Package_LGA:LGA-12_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://kionixfs.kionix.com/en/datasheet/KX222-1054-Specifications-Rev-2.0.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer spi i2c mems', 'kicadSymbolki_description': '3-Axis Accelerometer, 8/16/32g range, 2048 byte buffer, I2C/SPI interface, LGA-12', 'kicadSymbolki_fp_filters': 'LGA*2x2mm*P0.5mm*'}])
    newPart['name'].append('KX222-1054')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

