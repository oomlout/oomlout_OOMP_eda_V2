
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LIS331HH"
    hexID = "SZKSENMOTIONLIS331HH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LIS331HH', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00250937.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer spi i2c mems', 'kicadSymbolki_description': '3-Axis Accelerometer, 6/12/24g range, 1000Hz, I2C and SPI interface', 'kicadSymbolki_fp_filters': 'LGA-*3x3mm*P0.5mm*LayoutBorder3x5y*'}])
    newPart['name'].append('Sensor_Motion : LIS331HH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

