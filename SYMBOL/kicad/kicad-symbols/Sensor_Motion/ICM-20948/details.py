
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "ICM-20948"
    hexID = "SZKSENMOTIONICM2948"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICM-20948', 'kicadSymbolFootprint': 'Sensor_Motion:InvenSense_QFN-24_3x3mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.invensense.com/wp-content/uploads/2016/06/DS-000189-ICM-20948-v1.3.pdf', 'kicadSymbolki_keywords': 'mems magnetometer', 'kicadSymbolki_description': 'InvenSense 9-Axis Motion Sensor, Accelerometer, Gyroscope, Compass, I2C/SPI, QFN-24', 'kicadSymbolki_fp_filters': 'InvenSense?QFN*3x3mm*P0.4mm*'}])
    newPart['name'].append('ICM-20948')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

