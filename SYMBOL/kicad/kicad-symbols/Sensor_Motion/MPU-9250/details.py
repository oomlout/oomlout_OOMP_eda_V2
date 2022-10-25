
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "MPU-9250"
    hexID = "SZKSENMOTIONMPU925"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPU-9250', 'kicadSymbolFootprint': 'Sensor_Motion:InvenSense_QFN-24_3x3mm_P0.4mm', 'kicadSymbolDatasheet': 'https://store.invensense.com/datasheets/invensense/MPU9250REV1.0.pdf', 'kicadSymbolki_keywords': 'mems magnetometer', 'kicadSymbolki_description': 'InvenSense 9-Axis Motion Sensor, Accelerometer, Gyroscope, Compass, I2C/SPI', 'kicadSymbolki_fp_filters': '*QFN*3x3mm*P0.4mm*'}])
    newPart['name'].append('Sensor_Motion : MPU-9250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

