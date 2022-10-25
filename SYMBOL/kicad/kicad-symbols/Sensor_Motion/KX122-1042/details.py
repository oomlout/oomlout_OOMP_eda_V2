
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "KX122-1042"
    hexID = "SZKSENMOTIONKX122142"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KX022-1020', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KX122-1042', 'kicadSymbolFootprint': 'Package_LGA:LGA-12_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://kionixfs.kionix.com/en/datasheet/KX112-1042-Specifications-Rev-6.0.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer spi i2c mems', 'kicadSymbolki_description': '3-Axis Accelerometer, 2/4/8g range, 2048 byte buffer, I2C/SPI interface, LGA-12', 'kicadSymbolki_fp_filters': 'LGA*2x2mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : KX122-1042')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

