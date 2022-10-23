
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "MPU-6050"
    hexID = "SZKSENMOTIONMPU65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPU-6050', 'kicadSymbolFootprint': 'Sensor_Motion:InvenSense_QFN-24_4x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://store.invensense.com/datasheets/invensense/MPU-6050_DataSheet_V3%204.pdf', 'kicadSymbolki_keywords': 'mems', 'kicadSymbolki_description': 'InvenSense 6-Axis Motion Sensor, Gyroscope, Accelerometer, I2C', 'kicadSymbolki_fp_filters': '*QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('MPU-6050')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

