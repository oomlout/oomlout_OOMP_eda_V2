
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LIS2DH"
    hexID = "SZKSENMOTIONLIS2DH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LIS2DH', 'kicadSymbolFootprint': 'Package_LGA:LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y', 'kicadSymbolDatasheet': 'http://www.st.com/web/en/resource/technical/document/datasheet/DM00042751.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer spi mems LGA-14', 'kicadSymbolki_description': '3-Axis Accelerometer, 2/4/8/16g range, I2C/SPI interface, LGA-14', 'kicadSymbolki_fp_filters': 'LGA*2x2mm*P0.35mm*LayoutBorder3x4y*'}])
    newPart['name'].append('LIS2DH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

