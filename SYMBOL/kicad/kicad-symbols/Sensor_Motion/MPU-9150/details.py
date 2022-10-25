
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "MPU-9150"
    hexID = "SZKSENMOTIONMPU915"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPU-9150', 'kicadSymbolFootprint': 'Sensor_Motion:InvenSense_QFN-24_4x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.invensense.com/wp-content/uploads/2015/02/MPU-9150-Datasheet.pdf', 'kicadSymbolki_keywords': 'mems magnetometer', 'kicadSymbolki_description': 'InvenSense 9-Axis Motion Sensor, Accelerometer, Gyroscope, Compass, I2C', 'kicadSymbolki_fp_filters': '*QFN-24*4x4mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : MPU-9150')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

