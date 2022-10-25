
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LSM6DS3"
    hexID = "SZKSENMOTIONLSM6DS3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LSM6DS3', 'kicadSymbolFootprint': 'Package_LGA:LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/lsm6ds3.pdf', 'kicadSymbolki_keywords': 'Accelerometer Gyroscope MEMS', 'kicadSymbolki_description': 'I2C/SPI, iNEMO inertial module: always-on 3D accelerometer and 3D gyroscope', 'kicadSymbolki_fp_filters': 'LGA*3x2.5mm*P0.5mm*LayoutBorder3x4y*'}])
    newPart['name'].append('Sensor_Motion : LSM6DS3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

