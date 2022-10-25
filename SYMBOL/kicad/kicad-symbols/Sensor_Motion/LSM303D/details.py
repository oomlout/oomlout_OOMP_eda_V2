
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LSM303D"
    hexID = "SZKSENMOTIONLSM33D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LSM303D', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/web/en/resource/technical/document/datasheet/DM00057547.pdf', 'kicadSymbolki_keywords': 'Accelerometer Magnetometer MEMS', 'kicadSymbolki_description': '[not recommended for new designs] I2C/SPI, 3D Accelerometer and 3D Magnetometer', 'kicadSymbolki_fp_filters': 'LGA*'}])
    newPart['name'].append('Sensor_Motion : LSM303D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

