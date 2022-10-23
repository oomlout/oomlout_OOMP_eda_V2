
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LSM303DLHC"
    hexID = "SZKSENMOTIONLSM33DLHC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LSM303DLHC', 'kicadSymbolFootprint': 'Package_LGA:LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y', 'kicadSymbolDatasheet': 'http://www.st.com/web/en/resource/technical/document/datasheet/DM00027543.pdf', 'kicadSymbolki_keywords': 'Accelerometer Magnetometer MEMS', 'kicadSymbolki_description': '[not recommended for new designs] I2C, 3D Accelerometer and 3D Magnetometer', 'kicadSymbolki_fp_filters': 'LGA*3x5mm*P0.8mm*LayoutBorder1x6y*'}])
    newPart['name'].append('LSM303DLHC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

