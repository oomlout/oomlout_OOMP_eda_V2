
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LSM9DS1"
    hexID = "SZKSENMOTIONLSM9DS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LSM9DS1', 'kicadSymbolFootprint': 'Package_LGA:LGA-24L_3x3.5mm_P0.43mm', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/1e/3f/2a/d6/25/eb/48/46/DM00103319.pdf/files/DM00103319.pdf/jcr:content/translations/en.DM00103319.pdf', 'kicadSymbolki_keywords': 'I2C SPI IMU accelerometer gyroscope magnetometer', 'kicadSymbolki_description': 'I2C SPI 9 axis IMU accelerometer gyroscope magnetometer', 'kicadSymbolki_fp_filters': 'LGA*3x3.5mm*P0.43mm*'}])
    newPart['name'].append('LSM9DS1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

