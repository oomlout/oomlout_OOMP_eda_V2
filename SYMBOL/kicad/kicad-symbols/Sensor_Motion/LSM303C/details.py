
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LSM303C"
    hexID = "SZKSENMOTIONLSM33C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LSM303C', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/lsm303c.pdf', 'kicadSymbolki_keywords': 'Accelerometer Magnetometer MEMS', 'kicadSymbolki_description': 'I2C/SPI, 3D Accelerometer and 3D Magnetometer', 'kicadSymbolki_fp_filters': 'LGA*2x2mm*P0.5mm*'}])
    newPart['name'].append('LSM303C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

