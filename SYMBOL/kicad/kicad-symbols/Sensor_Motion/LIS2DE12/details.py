
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "LIS2DE12"
    hexID = "SZKSENMOTIONLIS2DE12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LIS2HH12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LIS2DE12', 'kicadSymbolFootprint': 'Package_LGA:LGA-12_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/lis2DE12.pdf', 'kicadSymbolki_keywords': '3-axis accelerometer spi mems', 'kicadSymbolki_description': '3-Axis Accelerometer, 2/4/8/16g range, I2C/SPI interface', 'kicadSymbolki_fp_filters': 'LGA*2x2mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : LIS2DE12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

